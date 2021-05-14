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
        houdini_session_settings = {
            "VDB Template": {
                "type": "template",
                "default": None,
                "description": "",
            },
            "BGEO Template": {
                "type": "template",
                "default": None,
                "description": "",
            },
        }

        # update the base settings with these settings
        collector_settings.update(houdini_session_settings)
        return collector_settings

    def process_current_session(self, settings, parent_item):
        """
        Analyzes the current Houdini session and parents a subtree of items
        under the parent_item passed in.

        :param dict settings: Configured settings for this collector
        :param parent_item: Root item instance
        """

        item = self.collect_current_houdini_session(settings, parent_item)
        self._alembic_nodes_collected = False
        self._mantra_nodes_collected = False
        self.collect_tk_alembicnodes(item)
        self.collect_tk_mantranodes(item)
        self.collect_node_outputs(item)
        self._collect_sgtk_geometry_out_nodes(settings, item)

    def _collect_sgtk_geometry_out_nodes(self, settings, parent_item):
        tk_node_type = 'sgtk_geometry_output'
        nodes = hou.nodeType(hou.ropNodeTypeCategory(), tk_node_type).instances()
        for node in nodes:
            self._create_sgtk_geometry_node_item(settings, node, parent_item)
        return

    def _create_sgtk_geometry_node_item(self, settings, node, parent_item):
        template_menu_index = node.parm('template_menu').eval()
        menu_labels = node.parm('template_menu').menuLabels()
        selected_format = menu_labels[template_menu_index]
        publisher = self.parent
        if selected_format.lower() == 'vdb':
            work_template_setting = settings.get("VDB Template")
        else:
            work_template_setting = settings.get("BGEO Template")
        if work_template_setting:
            work_template = publisher.engine.get_template_by_name(
                work_template_setting.value
            )
        node_child = node.children()[0]     # get HDA inner geometry node
        node_output_path = node_child.parm('sopoutput').eval()
        if self._node_output_exist(node_output_path) and self._is_correct_output_version(node_output_path):
            item = self._collect_file(
                parent_item, node_output_path, frame_sequence=True
            )
            node_name = node.name()
            item.name = node_name
            item.properties["publish_name"] = node_name
            item.properties["work_template"] = work_template

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