﻿# Copyright (c) 2017 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import glob
import os
import maya.cmds as cmds
import maya.mel as mel
import sgtk

HookBaseClass = sgtk.get_hook_baseclass()


class MayaSessionCollector(HookBaseClass):
    """
    Collector that operates on the maya session. Should inherit from the basic
    collector hook.
    """


    @property
    def settings(self):
        """
        Dictionary defining the settings that this collector expects to receive
        through the settings parameter in the process_current_session and
        process_file methods.

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

        # grab any base class settings
        collector_settings = super(MayaSessionCollector, self).settings or {}

        # settings specific to this collector
        maya_session_settings = {
            "Work Template": {
                "type": "template",
                "default": None,
                "description": "Template path for artist work files. Should "
                               "correspond to a template defined in "
                               "templates.yml. If configured, is made available"
                               "to publish plugins via the collected item's "
                               "properties. ",
            },
            "Sets Prefix": {
                "type": "list",
                "default": ["geo"],
                "description": "Sets name prefix"
            }
        }

        # update the base settings with these settings
        collector_settings.update(maya_session_settings)

        return collector_settings


    def process_current_session(self, settings, parent_item):
        """
        Analyzes the current session open in Maya and parents a subtree of
        items under the parent_item passed in.

        :param dict settings: Configured settings for this collector
        :param parent_item: Root item instance

        """

        # dziedziczy z typu klasy objekt self
        super(MayaSessionCollector, self).process_current_session(settings, parent_item)
        # find the maya session item to attach to
        session_item = next((item for item in parent_item.descendants if item.type_spec == 'maya.session'), None)
        if session_item is None:
            return
        self._collect_cameras(session_item)
        self._collect_render_job(session_item)
        self._collect_meshes(session_item)
        self._collect_objects_sets(settings, session_item)


    def _collect_cameras(self, parent_item):
        """
        Creates items for each camera in the session.

        :param parent_item: The maya session parent item
        """

        # build a path for the icon to use for each item. the disk
        # location refers to the path of this hook file. this means that
        # the icon should live one level above the hook in an "icons"
        # folder.
        icon_path = os.path.join(
            self.disk_location,
            os.pardir,
            "icons",
            "publish_maya_camera.png"
        )

        # iterate over each camera and create an item for it
        for camera_shape in cmds.ls(cameras=True):

            # try to determine the camera display name
            try:
                camera_name = cmds.listRelatives(camera_shape, parent=True)[0]
            except Exception:
                # could not determine the name, just use the shape
                camera_name = camera_shape

            # create a new item parented to the supplied session item. We
            # define an item type (maya.session.camera) that will be
            # used by an associated camera publish plugin as it searches for
            # items to act upon. We also give the item a display type and
            # display name. In the future, other publish plugins might attach to
            # these camera items to perform other actions
            cam_item = parent_item.create_item(
                "maya.session.camera",
                "Camera",
                camera_name
            )

            # set the icon for the item
            cam_item.set_icon_from_path(icon_path)

            # store the camera name so that any attached plugin knows which
            # camera this item represents!
            cam_item.properties["camera_name"] = camera_name
            cam_item.properties["camera_shape"] = camera_shape

            self.logger.debug('Collected cameras: %s' % camera_name)


    def _collect_render_job(self, parent_item):
        """
        Creates items for Deadline render job
        :param parent_item:
        :return:
        """

        icon_path = os.path.join(
            self.disk_location,
            os.pardir,
            "icons",
            "publish_render_job.png"
        )
        render_job_name = self._get_scene_name()
        render_job_item = parent_item.create_item(
            "maya.session.render_job",
            "Render Job",
            render_job_name
        )
        # set the icon for the item
        render_job_item.set_icon_from_path(icon_path)
        render_job_item.properties["render_job_name"] = render_job_name


    def _collect_meshes(self, parent_item):
        """
        Collect mesh definitions and create publish items for them.

        :param parent_item: The maya session parent item
        """

        # build a path for the icon to use for each item. the disk
        # location refers to the path of this hook file. this means that
        # the icon should live one level above the hook in an "icons"
        # folder.
        icon_path = os.path.join(
            self.disk_location,
            os.pardir,
            "icons",
            "mesh.png"
        )

        # iterate over all top-level transforms and create mesh items
        # for any mesh.
        for object in cmds.ls(assemblies=True):

            if not cmds.ls(object, dag=True, type="mesh"):
                # ignore non-meshes
                continue

            # create a new item parented to the supplied session item. We
            # define an item type (maya.session.mesh) that will be
            # used by an associated shader publish plugin as it searches for
            # items to act upon. We also give the item a display type and
            # display name (the group name). In the future, other publish
            # plugins might attach to these mesh items to publish other things
            mesh_item = parent_item.create_item(
                "maya.session.mesh",
                "Mesh",
                object
            )

            # set the icon for the item
            mesh_item.set_icon_from_path(icon_path)

            # finally, add information to the mesh item that can be used
            # by the publish plugin to identify and export it properly
            mesh_item.properties["object"] = object


    def _collect_objects_sets(self, settings, parent_item):
        """
        collect sets which name starting with Sets Prefix pattern
        """


        for set_name in cmds.ls(sets=True):
            if self._set_name_match_pattern(settings, set_name):
                objects_in_set = self._get_meshes_from_set(set_name)
                self._create_item_for_set(parent_item, objects_in_set, set_name)
                self.logger.debug('Collected sets: %s' % set_name)


    def _get_meshes_from_set(self, set_name):
        objects_in_set = cmds.sets(set_name, q=True)
        shapes_in_set = []
        if objects_in_set:
            for object in objects_in_set:
                if cmds.listRelatives(object, shapes=True):
                    shapes_in_set.append(object)
        return shapes_in_set


    def _set_name_match_pattern(self, settings, set_name):
        lower_set_name = set_name.lower()
        set_prefix_list = settings["Sets Prefix"].value
        for prefix in set_prefix_list:
            lower_prefix = prefix.lower()
            if lower_set_name.startswith(lower_prefix):
                return True
        return False


    def _create_item_for_set(self, parent_item, objects_in_set, set_name):
        icon_path = os.path.join(
            self.disk_location,
            os.pardir,
            "icons",
            "mesh.png"
        )
        # for object in objects_in_set:
        object_sets_item = parent_item.create_item(
            "maya.session.object_set",
            set_name,
            object
        )
        object_sets_item.set_icon_from_path(icon_path)
        object_sets_item.properties["objects"] = objects_in_set
        object_sets_item.properties["set_name"] = set_name
        object_sets_item.expanded = False


    @staticmethod
    def _get_scene_name():
        scene_name = cmds.file(query=True, sceneName=True, shortName=True)
        if len(scene_name) == 0:
            return False
        scene_name = scene_name.split('.')[-2]
        return scene_name