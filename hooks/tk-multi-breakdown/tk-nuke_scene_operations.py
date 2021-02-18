# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import nuke
import sgtk

HookBaseClass = sgtk.get_hook_baseclass()


class BreakdownSceneOperations(HookBaseClass):
    """
    Breakdown operations for Nuke.

    This implementation handles detection of Nuke read nodes,
    geometry nodes and camera nodes.
    """

    def scan_scene(self):
        """
        The scan scene method is executed once at startup and its purpose is
        to analyze the current scene and return a list of references that are
        to be potentially operated on.

        The return data structure is a list of dictionaries. Each scene reference
        that is returned should be represented by a dictionary with three keys:

        - "node": The name of the 'node' that is to be operated on. Most DCCs have
          a concept of a node, path or some other way to address a particular
          object in the scene.
        - "type": The object type that this is. This is later passed to the
          update method so that it knows how to handle the object.
        - "path": Path on disk to the referenced object.

        Toolkit will scan the list of items, see if any of the objects matches
        any templates and try to determine if there is a more recent version
        available. Any such versions are then displayed in the UI as out of date.

        """

        reads = []
        reads_layered = []

        # If we're in Nuke Studio or Hiero, we need to see if there are any
        # clips we need to be aware of that we might want to point to newer
        # publishes.
        if self.parent.engine.studio_enabled or self.parent.engine.hiero_enabled:
            import hiero

            for project in hiero.core.projects():
                for clip in project.clipsBin().clips():
                    files = clip.activeItem().mediaSource().fileinfos()
                    for file in files:
                        path = file.filename().replace("/", os.path.sep)
                        reads.append(
                            dict(node=clip.activeItem(), type="Clip", path=path,)
                        )

        # Hiero doesn't have nodes to check, so just return the clips.
        if self.parent.engine.hiero_enabled:
            return reads

        # first let's look at the read nodes
        for node in nuke.allNodes("Read"):

            node_name = node.name()
            # note! We are getting the "abstract path", so contains
            # %04d and %V rather than actual values.
            path = node.knob("file").value().replace("/", os.path.sep)

            tk_engine = self.parent.engine.sgtk
            nuke_loader_template = tk_engine.templates['nuke_shot_render_multilayer']
            '''    
            if nuke_loader_template.validate(path):
                reads_layered.append(node)
            else:
            '''
        reads.append({"node": node_name, "type": "Read", "path": path})

        # then the read geometry nodes
        for node in nuke.allNodes("ReadGeo2"):
            node_name = node.name()
            path = node.knob("file").value().replace("/", os.path.sep)
            reads.append({"node": node_name, "type": "ReadGeo2", "path": path})

        # then the read camera nodes
        for node in nuke.allNodes("Camera2"):
            node_name = node.name()

            path = node.knob("file").value().replace("/", os.path.sep)
            reads.append({"node": node_name, "type": "Camera2", "path": path})

        if reads_layered:
            layers_dict = self.get_layers_dict(nuke_loader_template,reads_layered)
            for layer in layers_dict:
                layers_passes = layers_dict[layer]
                contain_beauty_pass = False
                beauty_pass = '%s_beauty' % (layer.lower())
                for layer_pass in layers_passes:
                    node_name = layer_pass.name()
                    path = layer_pass.knob("file").value().replace("/", os.path.sep)
                    if node_name.lower() == beauty_pass:
                        contain_beauty_pass = True
                        reads.append({"node": node_name, "type": "ReadLayers", "path": path})
                if not contain_beauty_pass:
                    node = layers_passes[0]
                    node_name = node.name()
                    path = node.knob("file").value().replace("/", os.path.sep)
                    reads.append({"node": node_name, "type": "ReadLayers", "path": path})
        return reads

    @staticmethod
    def get_layers_dict(nuke_loader_template,reads_layered):
        layers_dict = {}
        for element in reads_layered:
            path = element.knob("file").value().replace("/", os.path.sep)
            fields = nuke_loader_template.get_fields(path)
            if fields['layer'] not in layers_dict.keys():
                layers_dict[fields['layer']] = []
            layers_dict[fields['layer']].append(element)
        return layers_dict

    def update(self, items):
        """
        Perform replacements given a number of scene items passed from the app.

        Once a selection has been performed in the main UI and the user clicks
        the update button, this method is called.

        The items parameter is a list of dictionaries on the same form as was
        generated by the scan_scene hook above. The path key now holds
        the that each node should be updated *to* rather than the current path.
        """
        engine = self.parent.engine

        node_type_list = ["Read", "ReadGeo2", "Camera2"]

        print('+++++++++++++++++++++++++++++++++++')
        print(items)
        print('+++++++++++++++++++++++++++++++++++')

        for i in items:
            node_name = i["node"]
            node_type = i["type"]
            new_path = i["path"].replace(os.path.sep, "/")

            if node_type in node_type_list:
                engine.log_debug(
                    "Node %s: Updating to version %s" % (node_name, new_path)
                )
                node = nuke.toNode(node_name)
                node.knob("file").setValue(new_path)

            if node_type == "Clip":
                engine.log_debug(
                    "Clip %s: Updating to version %s" % (node_name, new_path)
                )
                clip = node_name
                clip.reconnectMedia(new_path)

            if node_type == 'ReadLayers':
                engine.log_debug(
                    "Node %s: Updating to version %s" % (node_name, new_path)
                )
                print('==================================')
                print(i)
                print('==================================')
                layer_passes = i['passes']
                self.update_layer_passes(layer_passes)

    @staticmethod
    def update_layer_passes(layer_passes):
        for layer_pass in layer_passes:
            node_name = layer_pass['node']
            new_path = layer_pass['path'].replace(os.path.sep, '/')
            node = nuke.toNode(node_name)
            node.knob('file').setValue(new_path)