# Copyright (c) 2017 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sys  #neede for publish thumbnail creation
import pprint
import traceback
import glob
import shutil
import re
import sgtk
from sgtk.platform.qt5 import QtCore, QtGui, QtWidgets
from sgtk.util.filesystem import copy_file, ensure_folder_exists

packages_path = r'\\192.168.1.204\Dane\Shotgun\python_packages\py2'
if packages_path not in sys.path:
    sys.path.append(packages_path)

import numpy as np
import cv2

HookBaseClass = sgtk.get_hook_baseclass()
current_engine = sgtk.platform.current_engine()  # take current used engine
sg = current_engine.shotgun  # get shotgun API from engine
tk = current_engine.sgtk

class BasicFilePublishPlugin(HookBaseClass):
    """
    Plugin for creating generic publishes in Shotgun.

    This plugin is typically configured to act upon files that are dragged and
    dropped into the publisher UI. It can also be used as a base class for
    other file-based publish plugins as it contains standard operations for
    validating and registering publishes with Shotgun.

    Once attached to a publish item, the plugin will key off of properties that
    drive how the item is published.

    The ``path`` property, set on the item, is the only required property as it
    informs the plugin where the file to publish lives on disk.

    The following properties can be set on the item via the collector or by
    subclasses prior to calling methods on the base class::

        ``sequence_paths`` - If set in the item properties dictionary, implies
            the "path" property represents a sequence of files (typically using
            a frame identifier such as %04d). This property should be a list of
            files on disk matching the "path". If the ``work_template`` property
            is set, and corresponds to the listed frames, fields will be
            extracted and applied to the publish_template (if set) and copied to
            that publish location.

        ``work_template`` - If set in the item properties dictionary, this
            value is used to validate ``path`` and extract fields for further
            processing and contextual discovery. For example, if configured and
            a version key can be extracted, it will be used as the publish
            version to be registered in Shotgun.

    The following properties can also be set by a subclass of this plugin via
    :meth:`Item.properties` or :meth:`Item.local_properties`.

        publish_template - If set, used to determine where "path" should be
            copied prior to publishing. If not specified, "path" will be
            published in place.

        publish_type - If set, will be supplied to SG as the publish type when
            registering "path" as a new publish. If not set, will be determined
            via the plugin's "File Type" setting.

        publish_path - If set, will be supplied to SG as the publish path when
            registering the new publish. If not set, will be determined by the
            "published_file" property if available, falling back to publishing
            "path" in place.

        publish_name - If set, will be supplied to SG as the publish name when
            registering the new publish. If not available, will be determined
            by the "work_template" property if available, falling back to the
            ``path_info`` hook logic.

        publish_version - If set, will be supplied to SG as the publish version
            when registering the new publish. If not available, will be
            determined by the "work_template" property if available, falling
            back to the ``path_info`` hook logic.

        publish_dependencies - A list of files to include as dependencies when
            registering the publish. If the item's parent has been published,
            it's path will be appended to this list.

        publish_user - If set, will be supplied to SG as the publish user
            when registering the new publish. If not available, the publishing
            will fall back to the :meth:`tank.util.register_publish` logic.

        publish_fields - If set, will be passed to
            :meth:`tank.util.register_publish` as the ``sg_fields`` keyword
            argument. A dictionary of additional fields that should be used
            for the publish entity in Shotgun.

        publish_kwargs - If set, will be used to update the dictionary of kwargs
            passed to :meth:`tank.util.register_publish`. Because this
            dictionary updates the kwargs built from other ``property``
            and ``local_property`` values, any kwargs set in this property will
            supersede those values.

    NOTE: accessing these ``publish_*`` values on the item does not necessarily
    return the value used during publish execution. Use the corresponding
    ``get_publish_*`` methods which include fallback logic when no property is
    set. For example, if a ``work_template`` is used, the publish version and
    name might be extracted from the template fields in the fallback logic.

    This plugin will also set an ``sg_publish_data`` property on the item during
    the ``publish`` method which may be useful for child items.

        ``sg_publish_data`` - The dictionary of publish information returned
            from the tk-core register_publish method.

    NOTE: If you have multiple plugins acting on the same item, and you need to
    access or operate on the publish data, you can extract the
    ``sg_publish_data`` from the item after calling the base class ``publish``
    method in your plugin subclass.
    """

    @property
    def icon(self):
        """
        Path to an png icon on disk
        """

        # look for icon one level up from this hook's folder in "icons" folder
        return os.path.join(self.disk_location, "icons", "publish.png")

    @property
    def name(self):
        """
        One line display name describing the plugin
        """
        return "Publish to Shotgun"

    @property
    def description(self):
        """
        Verbose, multi-line description of what the plugin does. This can
        contain simple html for formatting.
        """

        loader_url = "https://support.shotgunsoftware.com/hc/en-us/articles/219033078"

        return """
        Publishes the file to Shotgun. A <b>Publish</b> entry will be
        created in Shotgun which will include a reference to the file's current
        path on disk. Other users will be able to access the published file via
        the <b><a href='%s'>Loader</a></b> so long as they have access to
        the file's location on disk.

        <h3>File versioning</h3>
        The <code>version</code> field of the resulting <b>Publish</b> in
        Shotgun will also reflect the version number identified in the filename.
        The basic worklfow recognizes the following version formats by default:

        <ul>
        <li><code>filename.v###.ext</code></li>
        <li><code>filename_v###.ext</code></li>
        <li><code>filename-v###.ext</code></li>
        </ul>

        <br><br><i>NOTE: any amount of version number padding is supported.</i>

        <h3>Overwriting an existing publish</h3>
        A file can be published multiple times however only the most recent
        publish will be available to other users. Warnings will be provided
        during validation if there are previous publishes.
        """ % (
            loader_url,
        )

    @property
    def settings(self):
        """
        Dictionary defining the settings that this plugin expects to recieve
        through the settings parameter in the accept, validate, publish and
        finalize methods.

        A dictionary on the following form::

            {
                "Settings Name": {
                    "type": "settings_type",
                    "default": "default_value",
                    "description": "One line description of the setting"
            }

        The type string should be one of the data types that toolkit accepts
        as part of its environment configuration.
        """
        settings = super(BasicFilePublishPlugin, self).settings
        settings['File Types'] = {
                "type": "list",
                "default": [
                    ["Alias File", "wire"],
                    ["Alembic Cache", "abc"],
                    ["3dsmax Scene", "max"],
                    ["NukeStudio Project", "hrox"],
                    ["Houdini Scene", "hip", "hipnc"],
                    ["Maya Scene", "ma", "mb"],
                    ["Motion Builder FBX", "fbx"],
                    ["Nuke Script", "nk"],
                    ["Photoshop Image", "psd", "psb"],
                    ["VRED Scene", "vpb", "vpe", "osb"],
                    ["Rendered Image", "dpx", "exr"],
                    ["Texture", "tiff", "tx", "tga", "dds"],
                    ["Image", "jpeg", "jpg", "png"],
                    ["Movie", "mov", "mp4"],
                    ["PDF", "pdf"],
                ],
                "description": (
                    "List of file types to include. Each entry in the list "
                    "is a list in which the first entry is the Shotgun "
                    "published file type and subsequent entries are file "
                    "extensions that should be associated."
                ),
            }

        settings['Publish Template'] = {
            'type': 'list',
            'default': []
        }
        return settings

    @property
    def item_filters(self):
        """
        List of item types that this plugin is interested in.

        Only items matching entries in this list will be presented to the
        accept() method. Strings can contain glob patters such as *, for example
        ["maya.*", "file.maya"]
        """
        return ["file.*"]

    ############################################################################
    # standard publish plugin methods

    def accept(self, settings, item):
        """
        Method called by the publisher to determine if an item is of any
        interest to this plugin. Only items matching the filters defined via the
        item_filters property will be presented to this method.

        A publish task will be generated for each item accepted here. Returns a
        dictionary with the following booleans:

            - accepted: Indicates if the plugin is interested in this value at
                all. Required.
            - enabled: If True, the plugin will be enabled in the UI, otherwise
                it will be disabled. Optional, True by default.
            - visible: If True, the plugin will be visible in the UI, otherwise
                it will be hidden. Optional, True by default.
            - checked: If True, the plugin will be checked in the UI, otherwise
                it will be unchecked. Optional, True by default.

        :param settings: Dictionary of Settings. The keys are strings, matching
            the keys returned in the settings property. The values are `Setting`
            instances.
        :param item: Item to process

        :returns: dictionary with boolean keys accepted, required and enabled
        """
        super(BasicFilePublishPlugin, self).accept(settings, item)
        return {"accepted": True}

    def validate(self, settings, item):
        is_valid = True
        task = item.context.task
        publish_template = self._get_publish_template(settings, item)
        item.properties['publish_template'] = publish_template
        destination_path, version = self._get_destination_path(settings, item)
        publish_name = self.get_publish_name_from_path(destination_path, settings, item)
        item.properties['destination_path'] = destination_path
        item.properties['version'] = version
        item.properties['item_new_name'] = publish_name

        filter = [
            ['task', 'is', task],
            ['name', 'is', publish_name],
            ['version_number', 'is', version],
        ]
        conflicting_entity = sg.find_one('PublishedFile', filter)
        if conflicting_entity:
            self.logger.error('There is conflicting entity: %s' % str(conflicting_entity))
            is_valid = False

        if publish_template is None:
            self.logger.error('No valid template')
            is_valid = False

        if destination_path is None:
            self.logger.error('Cannot generate valid destination path')
            is_valid = False

        if task is None:
            self.logger.error('No task selected')
            is_valid = False

        return is_valid

    def publish(self, settings, item):
        """
        Executes the publish logic for the given item and settings.

        :param settings: Dictionary of Settings. The keys are strings, matching
            the keys returned in the settings property. The values are `Setting`
            instances.
        :param item: Item to process
        """

        publisher = self.parent

        # ---- determine the information required to publish

        # We allow the information to be pre-populated by the collector or a
        # base class plugin. They may have more information than is available
        # here such as custom type or template settings.

        # publish_version = item.properties['publish_version']
        publish_type = self.get_publish_type(settings, item)
        publish_dependencies_paths = self.get_publish_dependencies(settings, item)
        publish_user = self.get_publish_user(settings, item)
        publish_fields = self.get_publish_fields(settings, item)
        publish_kwargs = self.get_publish_kwargs(settings, item)
        publish_path = item.properties['destination_path']
        publish_version = item.properties['version']
        publish_name = item.properties['item_new_name']
        orginal_publish_name = self.get_publish_name(settings, item)
        publish_description = item.description
        publish_description = 'Source name: %s, %s' % (orginal_publish_name, publish_description)
        item.description = publish_description

        # if the parent item has publish data, get it id to include it in the list of
        # dependencies
        publish_dependencies_ids = []
        if 'sg_publish_data' in item.parent.properties:
            publish_dependencies_ids.append(
                item.parent.properties.sg_publish_data['id']
            )
        # coping files according to templates
        self._copy_work_to_publish(publish_path, settings, item)

        # arguments for publish registration
        self.logger.info('Registering publish...')
        publish_data = {
            'tk': publisher.sgtk,
            'context': item.context,
            'comment': item.description,
            'path': publish_path,
            'name': publish_name,
            'created_by': publish_user,
            'version_number': publish_version,
            'thumbnail_path': self.get_thumbnail_as_path(settings, item),
            'published_file_type': publish_type,
            'dependency_paths': publish_dependencies_paths,
            'dependency_ids': publish_dependencies_ids,
            'sg_fields': publish_fields,
        }

        # add extra kwargs
        publish_data.update(publish_kwargs)

        # log the publish data for debugging
        self.logger.debug(
            'Populated Publish data...',
            extra={
                'action_show_more_info': {
                    'label': 'Publish Data',
                    'tooltip': 'Show the complete Publish data dictionary',
                    'text': '<pre>%s</pre>' % (pprint.pformat(publish_data),),
                }
            },
        )

        # create the publish and stash it in the item properties for other
        # plugins to use.
        item.properties.sg_publish_data = sgtk.util.register_publish(**publish_data)
        self.logger.info('Publish registered!')
        self.logger.debug(
            'Shotgun Publish data...',
            extra={
                'action_show_more_info': {
                    'label': 'Shotgun Publish Data',
                    'tooltip': 'Show the complete Shotgun Publish Entity dictionary',
                    'text': '<pre>%s</pre>'
                    % (pprint.pformat(item.properties.sg_publish_data),),
                }
            },
        )

        if publish_data['thumbnail_path']:
            if os.path.isfile(publish_data['thumbnail_path']):
                os.remove(publish_data['thumbnail_path'])

    def _get_seq_format(self, settings, item):
        if item.type == 'file.image.sequence':
            seq_format = self.get_publish_path(settings, item)
            seq_format = seq_format.split('.')[-2]
            self.logger.info('Sequence format: %s' % seq_format)
        else:
            seq_format = None
        return seq_format

    def get_publish_name_from_path(self, path, settings, item):
        publish_name = os.path.split(path)[-1]
        publish_name = publish_name.split('.')
        publish_name_head = publish_name[0].split('_')
        publish_name_head = '_'.join(publish_name_head[:-1])
        seq_format = self._get_seq_format(settings, item)
        if seq_format:
            seq_format = seq_format % 1
            seq_format = map(lambda x: '#', seq_format)
            seq_format = list(seq_format)
            seq_format = ''.join(seq_format)
        if len(publish_name) == 3:
            publish_name = '%s.%s.%s' % (publish_name_head, seq_format, publish_name[-1])
        else:
            publish_name = '%s.%s' % (publish_name_head, publish_name[-1])
        return publish_name

    def _get_destination_path(self, settings, item):
        template = item.properties['publish_template']
        fields = self.get_fields(template, item)
        name = self._get_name(settings, item)
        # version = self.get_publish_version(name, settings, item)
        #item.properties['publish_name'] = name
        fields['name'] = name
        fields['version'] = 1
        destination_path = template.apply_fields(fields)
        publish_file_name = os.path.split(destination_path)[-1]
        self.logger.warning('Przed wersjowaniem %s' % fields['version'])
        version = self.get_publish_version(publish_file_name, settings, item)
        self.logger.warning('Po wersjowaniu %s' % version)

        if version != fields['version']:
            fields['version'] = version
            destination_path = template.apply_fields(fields)
        if template.validate(destination_path) is False:
            destination_path = None
        # item.properties['publish_version'] = fields['version']
        self.logger.info('Destination path: %s' % destination_path)
        return destination_path, version

    def _get_name(self, settings, item):
        file_name = self.get_publish_name(settings, item)
        file_name = file_name.split('.')
        if item.get_property('publish_version'):
            file_name = file_name[0]
        else:
            file_name = file_name[0]
            file_name = file_name.split('_')
            file_name = '_'.join(file_name[:-1])
        file_name = self._get_name_from_publish_name(file_name, item)
        return file_name

    def get_publish_version(self, name, settings, item):
        """
        Get the publish version for the supplied settings and item.

        :param settings: This plugin instance's configured settings
        :param item: The item to determine the publish version for

        Extracts the publish version via the configured work template if
        possible. Will fall back to using the path info hook.
        """

        # publish version explicitly set or defined on the item
        publish_version = item.get_property('publish_version')
        if publish_version:
            return publish_version

        # fall back to the template/path_info logic
        publisher = self.parent
        path = item.properties.path

        work_template = item.properties.get('work_template')
        work_fields = None
        publish_version = None

        if work_template:
            if work_template.validate(path):
                self.logger.debug('Work file template configured and matches file.')
                work_fields = work_template.get_fields(path)

        if work_fields:
            # if version number is one of the fields, use it to populate the
            # publish information
            if 'version' in work_fields:
                publish_version = work_fields.get('version')
                self.logger.debug('Retrieved version number via work file template.')

        else:
            self.logger.debug('Using path info hook to determine publish version.')
            publish_version = publisher.util.get_version_number(path)
            if item.type == 'file.image.sequence':
                publish_version = self._get_sequence_version_from_name(settings, item)
            if publish_version is None:
                publish_version = self._get_unversioned_file_version(name, settings, item)
        return publish_version

    def _get_sequence_version_from_name(self, settings, item):
        name = self.get_publish_name(settings, item)
        version = name.split('.')[0]
        version = version. split('_')[-1]
        version = re.findall(r'\d+', version)
        if not version:
            return None
        return int(version[0])

    def _get_name_from_publish_name(self, name, item):
        name_template= self._get_name_template(item)
        name = self._convert_publish_name_to_fields_list(name)
        name = self._check_name_fields(name, name_template, item)
        return name

    def _convert_publish_name_to_fields_list(self, name):
        self.logger.info(name)
        name = name.split('_')
        if len(name) != 4:
            name = False
            self.logger.warning('Wrong file name, check if shot name is in convention: "sequence_shot"')
        else:
            name[1] = '%s_%s' % (name[0], name[1])
            name.pop(0)
        return name

    def _get_name_template(self, item):
        name_template = item.properties['publish_template']
        name_template = name_template.definition
        name_template = os.path.split(name_template)[-1]
        name_template = name_template.split('.')[0]
        self.logger.info('name template _get_name_template %s' % name_template)
        name_template = name_template.split('_')
        self.logger.info('name template _get_name_template %s' %name_template)
        step_code_start_index = name_template.index('{step')
        step_code_end_index = name_template.index('code}')
        name_template[step_code_start_index] = '{step_code}'
        name_template.pop(step_code_end_index)
        for index, element in enumerate(name_template):
            element = element.replace('{', '')
            element = element.replace('}', '')
            name_template[index] = element
        return name_template

    def _check_name_fields(self, name, name_template, item):
        context_step_name = item.context.step
        context_step_name = sg.find_one('Step', [['id', 'is', context_step_name['id']]], ['short_name'])
        context_step_name = context_step_name['short_name']
        context_shot_name = item.context.entity['name']
        fields = {}

        if name is False:
            fields['Shot'] = context_shot_name
            fields['step_code'] = context_step_name
            file_name = self._prompt_window_rename(fields, item)
            return file_name

        bad_file_name = False
        shot_index = name_template.index('Shot')
        step_index = name_template.index('step_code')
        name_index = name_template.index('name')
        file_shot_name = name[shot_index]
        file_step_name = name[step_index]
        file_name = name[name_index]

        #it is important to keep if's according to template
        if file_shot_name != context_shot_name:
            bad_file_name = True
            self.logger.warning('File name "shot" segment differ from selected context.')
            fields['Shot'] = context_shot_name
        else:
            fields['Shot'] = file_shot_name

        if file_step_name != context_step_name:
            bad_file_name = True
            self.logger.warning('File name "step_code" segment differ from selected context.')
            fields['step_code'] = context_step_name
        else:
            fields['step_code'] = file_step_name

        if not file_name.isalnum():
            self.logger.warning('File name "name" segment is not alphanumeric')
            bad_file_name = True
        else:
            fields['name'] = file_name

        if bad_file_name:
            file_name = self._prompt_window_rename(fields, item)

        return file_name

    def _generate_file_name(self, item):
        name = item.name
        name = name.split('.')[0]
        regex = re.search('v\d\d\d', name)
        name = name.split('_')
        if len(name) == 1:
            name = name[0]
        elif regex:
            name = name[-3]
        else:
            name = name[-2]
        name = re.sub('[^A-Za-z0-9]+', '', name)
        return name

    def get_thumbnail_as_path(self, settings, item):
        publish_path = item.properties['destination_path']
        file_format = publish_path.split('.')[-1]
        if file_format == 'exr':
            thumbnail = self._generate_thumbnail(publish_path, settings, item)
        else:
            thumbnail = item.get_thumbnail_as_path()
        return thumbnail

    def _generate_thumbnail(self, publish_path, settings, item):
        seq_format = self._get_seq_format(settings, item)
        publish_path = publish_path.replace(seq_format, '*')
        publish_path = glob.glob(publish_path)[0]
        gamma = 1 / 2.2
        img = cv2.imread(publish_path, cv2.IMREAD_UNCHANGED)
        img = self._format_dtype_as_uint8(img, gamma)
        thumbnail = 'thumbnail.jpg'
        publish_path = os.path.split(publish_path)[0]
        thumbnail = os.path.join(publish_path, thumbnail)
        cv2.imwrite(thumbnail , img)
        return thumbnail

    def _format_dtype_as_uint8(self, img, gamma):
        if img.dtype == 'uint16':
            img = self._convert_uint16_to_uint8(img)
        if img.dtype == 'float32':
            img = self._convert_float32_to_uint8(img, gamma)
        return img

    @staticmethod
    def _convert_uint16_to_uint8(img):
        img = img.astype(img.dtype) / img.max()
        img = img * 255
        img = img.astype('uint8')
        return img

    @staticmethod
    def _convert_float32_to_uint8(img, gamma):
        img = np.power(img, gamma)
        img[img > 1] = 1
        img = img * 255
        img = img.astype('uint8')
        return img

    def _copy_work_to_publish(self, file_destiny, settings, item):
        file_source = self.get_publish_path(settings, item)
        # file_destiny = item.properties['destination_path']
        if item.type == 'file.image.sequence':
            self._copy_sequence(file_source, file_destiny, settings, item)
        else:
            self._check_if_path_exist(file_destiny)
            shutil.copy2(file_source, file_destiny)

    def _copy_sequence(self, file_source, file_destiny, settings, item):
        # seq_format = self._get_seq_format(settings, item)
        """
        z powodu  ze template ma sekwencje jako %04d  przy skladaniu sciezki zawsze sekwencja jest widziana jak %04d
        """
        file_source = self._change_path_seq_format(file_source, settings, item)
        files = glob.glob(file_source)
        for file in files:
            file_seq_number = file.split('.')[-2]
            #file_destination = file_destiny.replace(seq_format, file_seq_number)
            file_destination = file_destiny.replace('%04d', file_seq_number)
            self._check_if_path_exist(file_destination)
            shutil.copy2(file, file_destination)

    def _get_unversioned_file_version(self, name, settings, item):
        name = self.get_publish_name_from_path(name, settings, item)
        current_version = 0
        task = item.context.task
        published_files = sg.find('PublishedFile', [['task', 'is', task]], ['name', 'version_number'])
        published_files = filter(lambda x: x['name'] == name, published_files)
        for publish in published_files:
            version = publish['version_number']
            if version > current_version:
                current_version = version
        current_version = current_version + 1
        return current_version

    def _get_publish_template(self, settings, item):
        publish_template = None
        publish_extension = item.name
        publish_extension = publish_extension.split('.')[-1]
        publish_configurations = settings.get('Publish Template', [])
        publish_configurations = publish_configurations.value
        entity_type = item.context.entity.get('type') if item.context.entity else None
        item_type = item.type if item.context else None
        for template_config in publish_configurations:
            if item_type in template_config['item_type']:
                if entity_type == template_config['entity_type']:
                    if publish_extension in template_config['file_extension']:
                        publish_template = self.sgtk.templates[template_config['template']]
        return publish_template

    def _prompt_window_rename(self, fields, item):
        name = self._generate_file_name(item)
        rename_prompt = QtWidgets.QInputDialog()
        label = '''
            There are fields in name which dont fit 
            to selected task context: %s 
            Please provide file name only! 
            (without shot, step names and version!)
            Sugested file name is:     
        ''' % str(fields)

        rename_prompt.setLabelText(label)
        rename_prompt.setTextValue(name)
        show_prompt = rename_prompt.exec_()
        return rename_prompt.textValue()

    def get_fields(self, template, item):
        """
        Method used to get path fields. It's based on folder structure,
        if it's not exist it create needed path.

        :param template: current template
        :param item: current item
        :return: fields needed to resolve template path
        """

        task = item.context.task
        try:
            fields = item.context.as_template_fields(template)
        except sgtk.TankError:
            tk.create_filesystem_structure('Task', task['id'])
            fields = item.context.as_template_fields(template)
        return fields

    def _change_path_seq_format(self, path, settings, item):
        seq_format = self._get_seq_format(settings, item)
        path = path.replace(seq_format, '*')
        return path

    @staticmethod
    def _check_if_path_exist(file_destiny):
        path = os.path.split(file_destiny)[0]
        if not os.path.exists(path):
            os.makedirs(path)
