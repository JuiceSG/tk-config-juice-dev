# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook that loads defines all the available actions, broken down by publish type.
"""
import os
import re
import glob
import sys
import sgtk
import nuke

HookBaseClass = sgtk.get_hook_baseclass()
current_engine = sgtk.platform.current_engine()
sg = current_engine.shotgun
tk = current_engine.sgtk

class NukeActions(HookBaseClass):

    def _create_read_node(self, path, sg_publish_data):
        """
        Create a read node representing the publish.

        :param path: Path to file.
        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        """

        # super(NukeActions, self)._create_read_node(path, sg_publish_data)

        (_, ext) = os.path.splitext(path)

        # If this is an Alembic cache, use a ReadGeo2 and we're done.
        if ext.lower() == ".abc":
            nuke.createNode("ReadGeo2", "file {%s}" % path)
            return

        valid_extensions = [
            ".png",
            ".jpg",
            ".jpeg",
            ".exr",
            ".cin",
            ".dpx",
            ".tiff",
            ".tif",
            ".mov",
            ".mp4",
            ".psd",
            ".tga",
            ".ari",
            ".gif",
            ".iff",
        ]

        if ext.lower() not in valid_extensions:
            raise Exception("Unsupported file extension for '%s'!" % path)

        # check if patch math loader template
        nuke_loader_template = tk.templates['shot_render_multilayer']
        if nuke_loader_template.validate(path):
            print('Layers exists')
            path_components = os.path.split(path)
            seq_directory = path_components[0]
            fields = nuke_loader_template.get_fields(path)
            layers, passes = self._get_passes_and_layers_lists(nuke_loader_template, seq_directory)
            sequences = self._get_sequences(nuke_loader_template, fields, layers, passes)
            self._create_layers_read_nodes(sequences)
        else:
            print('No Layers')
            self._create_node_reader(path)

    def _create_node_reader(self, path):
        read_node = nuke.createNode("Read")
        read_node["file"].fromUserText(path)

        # find the sequence range if it has one:
        seq_range = self._find_sequence_range(path)

        if seq_range:
            # override the detected frame range.
            read_node["first"].setValue(seq_range[0])
            read_node["last"].setValue(seq_range[1])
        return read_node

    def _create_layers_read_nodes(self, sequences):
        nodes_set_xpos = 0
        node_set_ypos = None
        for layer, layer_passes in sequences.items():
            for layer_pass, path_to_pass in layer_passes.items():
                node_name = '%s_%s' % (layer, layer_pass)
                read_node = self._create_node_reader(path_to_pass)
                node_xpos = read_node.xpos()
                node_ypos = read_node.ypos()
                if node_set_ypos is None:
                    node_set_ypos = node_ypos
                xpos = node_xpos + nodes_set_xpos
                read_node.setName(node_name)
                read_node.setXpos(xpos)
                read_node.setYpos(node_set_ypos)
                nodes_set_xpos += 50
            nodes_set_xpos += 50

    @staticmethod
    def _get_sequences(template, fields, layers, passes):
        sequences = {}
        for layer in layers:
            pass_sequences = {}
            fields['layer'] = layer
            for layer_pass in passes:
                fields['pass'] = layer_pass
                seq_path = template.apply_fields(fields)
                pass_sequences[layer_pass] = seq_path
            sequences[layer] = pass_sequences
        return sequences

    @staticmethod
    def _get_passes_and_layers_lists(template, publish_folder_path):
        layers_list = []
        pass_list = []
        folder_content = os.listdir(publish_folder_path)
        for render_file in folder_content:
            path = os.path.join(publish_folder_path, render_file)
            layer_field = template.get_fields(path)['layer']
            pass_field = template.get_fields(path)['pass']
            if layer_field not in layers_list:
                layers_list.append(layer_field)
            if pass_field not in pass_list:
                pass_list.append(pass_field)
        return layers_list, pass_list