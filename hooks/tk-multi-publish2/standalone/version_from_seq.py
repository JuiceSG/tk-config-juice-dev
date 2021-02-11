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
import sys
import pprint
import sgtk
import glob
from tank_vendor import six
from sgtk.util.filesystem import copy_file, ensure_folder_exists
from sgtk.platform.qt5 import QtCore, QtGui, QtWidgets

packages_path = r'\\192.168.1.204\Dane\Shotgun\python_packages\py2'
if packages_path not in sys.path:
    sys.path.append(packages_path)

import numpy as np
import cv2

HookBaseClass = sgtk.get_hook_baseclass()
current_engine = sgtk.platform.current_engine()
tk = current_engine.sgtk

class PublishSeqAsMov(HookBaseClass):
    """
    Plugin for sending quicktimes and images to shotgun for review.
    """

    @property
    def icon(self):
        """
        Path to an png icon on disk
        """

        # look for icon one level up from this hook's folder in "icons" folder
        return os.path.join(self.disk_location, "icons", "review.png")

    @property
    def name(self):
        """
        One line display name describing the plugin
        """
        return "Upload sequence as .mov"

    @property
    def description(self):
        """
        Verbose, multi-line description of what the plugin does. This can
        contain simple html for formatting.
        """

        publisher = self.parent

        shotgun_url = publisher.sgtk.shotgun_url

        media_page_url = "%s/page/media_center" % (shotgun_url,)
        review_url = "https://www.shotgunsoftware.com/features/#review"

        return """
        Convert image sequence to .mov file, and upload it to Shotgun for review.<br><br>

        A <b>Version</b> entry will be created in Shotgun and a transcoded
        copy of the file will be attached to it. The file can then be reviewed
        via the project's <a href='%s'>Media</a> page, <a href='%s'>RV</a>, or
        the <a href='%s'>Shotgun Review</a> mobile app.<br><br>
        
        This plugin use OpenCV 4.2.0.34 and Numpy 1.16.4 libaries.
        """ % (
            media_page_url,
            review_url,
            review_url,
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

        The type string should be one of the data types that toolkit accepts as
        part of its environment configuration.
        """
        settings = super(PublishSeqAsMov, self).settings or {}
        
        settings["File Extensions"] = {
            "type": "str",
            "default": "jpeg, jpg, png, exr",
            "description": "File Extensions of files to include.",
        }
        
        settings["Upload"] = {
            "type": "bool",
            "default": True,
            "description": "Upload content to Shotgun?",
        }
        
        settings["Link Local File"] = {
            "type": "bool",
            "default": False,
            "description": "Should the local file be referenced by Shotgun",
        }

        settings['Publish Template'] = {
            "type": "template",
            "default": None,
            "description": "Template path for published sequence as mov."
                           "Should correspond to a template defined in "
                           "templates.yml.",
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

        return ["file.image.sequence"]

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
        publisher = self.parent
        template_name = settings["Publish Template"].value
        if template_name is None:
            self.logger.debug("There is a problem with tk_multi_publish2.yml")
            accepted = False

        file_path = item.properties["path"]
        file_info = publisher.util.get_file_path_components(file_path)
        extension = file_info["extension"].lower()
        valid_extensions = []
        for ext in settings["File Extensions"].value.split(","):
            ext = ext.strip().lstrip(".")
            valid_extensions.append(ext)

        self.logger.debug("Valid extensions: %s" % valid_extensions)

        if extension in valid_extensions:
            self.logger.info(
                "Upload sequence as mov plugin accepted: %s" % (file_path,),
                extra={"action_show_folder": {"path": file_path}},
            )
            accepted= True
        else:
            self.logger.debug(
                "%s is not in the valid extensions list for Upload sequence as mov"
                % (extension,)
            )
            accepted = False

        return {
            "accepted": accepted,
            "checked": True
        }

    def validate(self, settings, item):
        """
        Validates the given item to check that it is ok to publish.

        Returns a boolean to indicate validity.

        :param settings: Dictionary of Settings. The keys are strings, matching
            the keys returned in the settings property. The values are `Setting`
            instances.
        :param item: Item to process

        :returns: True if item is valid, False otherwise.
        """
        publish_name = self._get_publish_name(item)
        self.logger.info('Publish name: {}'.format(publish_name))

        validation = True
        fps = self._get_project_fps(item)
        error_msg = 'No FPS value in SG project settings, please set value on project site'
        if fps is None:
            validation = False
            self.logger.error(error_msg)
            raise Exception(error_msg)

        task = item.context.task
        error_msg = 'No task selected, if you need to upload .mov file to Shotgun please select right task'
        if task is None:
            validation = False
            self.logger.error(error_msg)
            raise Exception(error_msg)

        publish_path = self._get_publish_directory(settings, item)
        error_msg = 'Problem with publish path'
        if publish_path is None:
            validation = False
            self.logger.error(error_msg)
            raise Exception(error_msg)

        return validation

    def publish(self, settings, item):
        """
        Executes the publish logic for the given item and settings.

        :param settings: Dictionary of Settings. The keys are strings, matching
            the keys returned in the settings property. The values are `Setting`
            instances.
        :param item: Item to process
        """

        publisher = self.parent
        path = item.properties["path"]
        publish_data = item.properties["sg_publish_data"]
        # allow the publish name to be supplied via the item properties. this is
        # useful for collectors that have access to templates and can determine
        # publish information about the item that doesn't require further, fuzzy
        # logic to be used here (the zero config way)
        publish_name = self._get_publish_name(item)
        self.logger.debug("Publish name: %s" % (publish_name,))
        self.logger.info("Creating Version...")
        version_data = {
            "project": item.context.project,
            "code": publish_name,
            "description": item.description,
            "entity": self._get_version_entity(item),
            "sg_task": item.context.task,
            "sg_first_frame": 1001,
        }

        if "sg_publish_data" in item.properties:
            version_data["published_files"] = [publish_data]
            publish_name = version_data["published_files"]
            publish_version = publish_name[0]["version_number"]
            publish_version = "{:03d}".format(publish_version)
            publish_name = publish_name[0]["code"]
            publish_name = publish_name.split(".")
            version_data["code"] = "%s_mov" % publish_name[0]
        if settings["Link Local File"].value:
            version_data["sg_path_to_movie"] = path

        # log the version data for debugging
        self.logger.debug(
            "Populated Version data...",
            extra={
                "action_show_more_info": {
                    "label": "Version Data",
                    "tooltip": "Show the complete Version data dictionary",
                    "text": "<pre>%s</pre>" % (pprint.pformat(version_data),),
                }
            },
        )

        output_file = self._get_output_file(settings, item)
        self._seq_to_mov(path, output_file, item)
        self.logger.debug("PATH: %s, OUTPUT: %s" % (path, output_file))

        # Create the version
        version = publisher.shotgun.create("Version", version_data)
        self.logger.info("Version created!")

        # stash the version info in the item just in case
        item.properties["sg_version_data"] = version
        thumb = item.get_thumbnail_as_path()

        if settings["Upload"].value:
            self.logger.info("Uploading content...")
            # on windows, ensure the path is utf-8 encoded to avoid issues with
            # the shotgun api
            if sgtk.util.is_windows():
                upload_path = six.ensure_text(output_file)
            else:
                upload_path = output_file
            self.parent.shotgun.upload(
                "Version", version["id"], upload_path, "sg_uploaded_movie"
            )
        elif thumb:
            # only upload thumb if we are not uploading the content. withs
            # uploaded content, the thumb is automatically extracted.
            self.logger.info("Uploading thumbnail...")
            self.parent.shotgun.upload_thumbnail("Version", version["id"], thumb)

        try:
            os.remove(output_file)
            self.logger.info("Temporary file deleted")
        except:
            self.logger.warning("There was problem with deleting temporary file")

        self.logger.debug("Version: %s" % version["id"])
        self.logger.info("Upload complete!")

    def finalize(self, settings, item):
        """
        Execute the finalization pass. This pass executes once all the publish
        tasks have completed, and can for example be used to version up files.

        :param settings: Dictionary of Settings. The keys are strings, matching
            the keys returned in the settings property. The values are `Setting`
            instances.
        :param item: Item to process
        """

        path = item.properties["path"]
        version = item.properties["sg_version_data"]

        self.logger.info(
            "Version uploaded for file: %s" % (path,),
            extra={
                "action_show_in_shotgun": {
                    "label": "Show Version",
                    "tooltip": "Reveal the version in Shotgun.",
                    "entity": version,
                }
            },
        )

    def _get_publish_name(self, item):
        path = item.properties["path"]
        publisher = self.parent
        publish_name = item.properties.get("publish_name")
        if not publish_name:
            self.logger.debug("Using path info hook to determine publish name.")
            # use the path's filename as the publish name
            path_components = publisher.util.get_file_path_components(path)
            publish_name = path_components["filename"]
        return publish_name

    def _get_output_file(self, settings, item):
        publish_directory = self._get_publish_directory(settings, item)
        mov_name = item.name.split(".")[0]
        output_file_name = '%s.mov' % mov_name
        output_file = '%s/%s' % (publish_directory, output_file_name)
        return output_file

    def _get_project_fps(self, item):
        sg = self.parent.shotgun
        project = item.context.project
        project_id = project['id']
        fps = sg.find_one('Project', [['id', 'is', project_id]], ['sg_fps'])
        fps = fps['sg_fps']
        if fps is None:
            self._prompt_window_fps()
        fps = float(fps)
        return fps

    def _get_publish_directory(self, settings, item):
        template = self._get_publish_template(settings, item)
        fields = self.get_fields(template, item)
        publish_path = template.apply_fields(fields)
        self.logger.info('Publish_path: %s' % publish_path)
        return  publish_path

    def _get_publish_template(self, settings, item):
        publish_template = None
        publish_configurations = settings.get("Publish Template", [])
        publish_configurations = publish_configurations.value
        entity_type = item.context.entity.get('type') if item.context.entity else None
        item_type = item.type if item.context else None
        for template_config in publish_configurations:
            if item_type in template_config['item_type'] and entity_type == template_config['entity_type']:
                publish_template = self.sgtk.templates[template_config['template']]
        return publish_template

    def _seq_to_mov(self, path_to_sequence, output_file, item):
        """
        convert images sequence to .MOV tested with exr png jpg
        """

        path_to_sequence = self._format_path_to_seq(path_to_sequence)
        fps = self._get_project_fps(item)

        gamma = 1/2.2
        img_sequence = []
        size = ()

        for file in glob.glob(path_to_sequence):
            file = file.encode('unicode_escape')
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            img = self._format_dtype_as_uint8(img, gamma)
            img_sequence.append(img)
            height, width, layers = img.shape
            size = (width, height)

        out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'x264'), fps, size)
        for frame in img_sequence:
            out.write(frame)
        out.release()
        self.logger.debug("MOV created")
        return True

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

    @staticmethod
    def get_fields(template, item):
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

    @staticmethod
    def _get_version_entity(item):
        """
        Returns the best entity to link the version to.
        """

        if item.context.entity:
            return item.context.entity
        elif item.context.project:
            return item.context.project
        else:
            return None

    @staticmethod
    def _format_path_to_seq(path):
        seq_path = ('%04d', '%06d', '%08d', '####', '######', '########')
        seq_path = filter(lambda x: x in path, seq_path)
        seq_path = list(seq_path)
        seq_path = seq_path[-1]
        seq_path = path.replace(seq_path, '*')
        return seq_path

    @staticmethod
    def _prompt_window_fps():
        fps_prompt = QtWidgets.QMessageBox()
        fps_prompt.setWindowTitle('Set FPS')
        fps_prompt.setText('no FPS value in SG project settings.')
        fps_prompt.setIcon(QtWidgets.QMessageBox.Critical)
        show_prompt = fps_prompt.exec_()



















