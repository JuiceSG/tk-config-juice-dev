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
import hou
import sgtk

HookBaseClass = sgtk.get_hook_baseclass()


class HoudiniSessionCollector(HookBaseClass):
    """
    Collector that operates on the current houdini session. Should inherit from
    the basic collector hook.
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
        collector_settings = super(HoudiniSessionCollector, self).settings or {}
        return collector_settings

    def process_current_session(self, settings, parent_item):
        """
        Analyzes the current Houdini session and parents a subtree of items
        under the parent_item passed in.

        :param dict settings: Configured settings for this collector
        :param parent_item: Root item instance
        """
        # create an item representing the current houdini session

        item = self.collect_current_houdini_session(settings, parent_item)
        self._collect_sgtk_geometry_out_nodes(item)

    def collect_current_houdini_session(self, settings, parent_item):
        session_item = super(HoudiniSessionCollector, self).collect_current_houdini_session(settings, parent_item)
        return session_item

    def _collect_sgtk_geometry_out_nodes(self, parent_item):
        tk_node_type = 'sgtk_geometry_output'
        nodes = hou.nodeType(hou.ropNodeTypeCategory(), tk_node_type).instances()
        for node in nodes:
            self._create_sgtk_geometry_node_item(node, parent_item)
        return

    def _create_sgtk_geometry_node_item(self, node, parent_item):
        '''
        template_menu_index = node.parm('template_menu').eval()
        menu_labels = node.parm('template_menu').menuLabels()
        selected_format = menu_labels[template_menu_index]
        '''
        node_child = node.children()[0]     # get HDA inner geometry node
        node_output_path = node_child.parm('sopoutput').eval()
        if self._node_output_exist(node_output_path) and self._is_correct_output_version(node_output_path):
            item = super(HoudiniSessionCollector, self)._collect_file(
                parent_item, node_output_path, frame_sequence=True
            )
        node_name = node.name()
        item.name = node_name
        item.properties["publish_name"] = node_name

    @staticmethod
    def _node_output_exist(node_output_path):
        path_head, path_tail = os.path.split(node_output_path)
        path_tail_pattern = path_tail.replace('$F4', '\d*')
        folder_content = os.listdir(path_head)
        for file in folder_content:
            if re.match(path_tail_pattern, file):
                return True
        return False

    @staticmethod
    def _is_correct_output_version(node_output_path):
        hip_file_path = hou.hipFile.name()
        hip_file_path_tail = os.path.split(hip_file_path)[1]
        hip_file_name = hip_file_path_tail.split('.')[0]
        hip_version = hip_file_name.split('_')[-1]
        output_path_tail = os.path.split(node_output_path)[1]
        output_file_name = output_path_tail.split('.')[0]
        output_version = output_file_name.split('_')[-1]
        if hip_version == output_version:
            return True
        return False