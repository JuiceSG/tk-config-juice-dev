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
import re
import pprint
import sgtk
import glob
import nuke
from tank_vendor import six

HookBaseClass = sgtk.get_hook_baseclass()


class UploadVersionPlugin(HookBaseClass):
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
        return "Upload for review"

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
        Upload the file to Shotgun for review.<br><br>

        A <b>Version</b> entry will be created in Shotgun and a transcoded
        copy of the file will be attached to it. The file can then be reviewed
        via the project's <a href='%s'>Media</a> page, <a href='%s'>RV</a>, or
        the <a href='%s'>Shotgun Review</a> mobile app.
        """ % (
            media_page_url,
            review_url,
            review_url,
        )

        # TODO: when settings editable, describe upload vs. link

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
        plugin_settings = super(UploadVersionPlugin, self).settings or {}
        upload_version_settings = {
            'EXR Output Template': {
                'type': 'template',
                'default': None,
            },
            'PNG Output Template': {
                'type': 'template',
                'default': None,
            },
            'JPG Output Template': {
                'type': 'template',
                'default': None,
            },
            'DPX Mono Output Template': {
                'type': 'template',
                'default': None,
            },
            'Stereo Output Template': {
                'type': 'template',
                'default': None,
            },
            'Movie Output Template': {
                'type': 'template',
                'default': None,
            },
        }
        plugin_settings.update(upload_version_settings)
        return plugin_settings

    @property
    def item_filters(self):
        """
        List of item types that this plugin is interested in.

        Only items matching entries in this list will be presented to the
        accept() method. Strings can contain glob patters such as *, for example
        ["maya.*", "file.maya"]
        """

        # we use "video" since that's the mimetype category.
        return ["file.image", "file.video"]

    def accept(self, settings, item):
        return super(UploadVersionPlugin, self).accept(settings, item)

    def validate(self, settings, item):
        output_templates, output_fields = self.__get_output_templates(settings, item)
        output_paths = (template.apply_fields(output_fields) for template in output_templates)
        path_to_frames = self.__path_to_frames(output_paths)
        item.properties['__path_to_frame'] = path_to_frames
        if path_to_frames:
            for template in output_templates:
                if template.validate(path_to_frames):
                    self.logger.debug('Output frames path match template: %s' % template)
                    return True
        self.logger.error('Path to frames isnt valid with any template or no frames found')
        return False

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

        # allow the publish name to be supplied via the item properties. this is
        # useful for collectors that have access to templates and can determine
        # publish information about the item that doesn't require further, fuzzy
        # logic to be used here (the zero config way)
        publish_name = item.properties.get("publish_name")
        if not publish_name:

            self.logger.debug("Using path info hook to determine publish name.")

            # use the path's filename as the publish name
            path_components = publisher.util.get_file_path_components(path)
            publish_name = path_components["filename"]

        self.logger.debug("Publish name: %s" % (publish_name,))

        self.logger.info("Creating Version...")
        version_data = {
            "project": item.context.project,
            "code": publish_name,
            "sg_path_to_frames": item.properties['__path_to_frame'],
            "description": item.description,
            "entity": self._get_version_entity(item),
            "sg_task": item.context.task,
        }

        if "sg_publish_data" in item.properties:
            publish_data = item.properties["sg_publish_data"]
            version_data["published_files"] = [publish_data]

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
                upload_path = six.ensure_text(path)
            else:
                upload_path = path

            self.parent.shotgun.upload(
                "Version", version["id"], upload_path, "sg_uploaded_movie"
            )
        elif thumb:
            # only upload thumb if we are not uploading the content. with
            # uploaded content, the thumb is automatically extracted.
            self.logger.info("Uploading thumbnail...")
            self.parent.shotgun.upload_thumbnail("Version", version["id"], thumb)

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

    def _get_version_entity(self, item):
        """
        Returns the best entity to link the version to.
        """

        if item.context.entity:
            return item.context.entity
        elif item.context.project:
            return item.context.project
        else:
            return None

    def __get_output_templates(self, settings, item):
        publisher = self.parent
        path = item.properties["path"]
        self.logger.debug('Item path: %s' % path)
        movie_output_template = settings['Movie Output Template'].value
        movie_output_template = publisher.engine.get_template_by_name(movie_output_template)

        output_fields = movie_output_template.get_fields(path)
        if not 'eye' in output_fields.keys():
            output_fields['eye'] = 'left'
        output_templates = (
            settings['EXR Output Template'].value,
            settings['PNG Output Template'].value,
            settings['JPG Output Template'].value,
            settings['DPX Mono Output Template'].value,
            settings['Stereo Output Template'].value,
        )
        output_templates = list(publisher.engine.get_template_by_name(template) for template in output_templates)
        return output_templates, output_fields

    def __path_to_frames(self, output_paths):
        pattern = '%\d\dd'
        for output in output_paths:
            frame_counter = re.findall(pattern, output)[-1]
            if glob.glob(output.replace(frame_counter, '*')):
                return output
        return ''