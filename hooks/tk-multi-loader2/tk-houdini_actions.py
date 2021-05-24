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
import re
import sgtk
import hou

HookBaseClass = sgtk.get_hook_baseclass()


class HoudiniActions(HookBaseClass):

    ##############################################################################################################
    # public interface - to be overridden by deriving classes

    def generate_actions(self, sg_publish_data, actions, ui_area):
        """
        Returns a list of action instances for a particular publish.
        This method is called each time a user clicks a publish somewhere in the UI.
        The data returned from this hook will be used to populate the actions menu for a publish.

        The mapping between Publish types and actions are kept in a different place
        (in the configuration) so at the point when this hook is called, the loader app
        has already established *which* actions are appropriate for this object.

        The hook should return at least one action for each item passed in via the
        actions parameter.

        This method needs to return detailed data for those actions, in the form of a list
        of dictionaries, each with name, params, caption and description keys.

        Because you are operating on a particular publish, you may tailor the output
        (caption, tooltip etc) to contain custom information suitable for this publish.

        The ui_area parameter is a string and indicates where the publish is to be shown.
        - If it will be shown in the main browsing area, "main" is passed.
        - If it will be shown in the details area, "details" is passed.
        - If it will be shown in the history area, "history" is passed.

        Please note that it is perfectly possible to create more than one action "instance" for
        an action! You can for example do scene introspection - if the action passed in
        is "character_attachment" you may for example scan the scene, figure out all the nodes
        where this object can be attached and return a list of action instances:
        "attach to left hand", "attach to right hand" etc. In this case, when more than
        one object is returned for an action, use the params key to pass additional
        data into the run_action hook.

        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        :param actions: List of action strings which have been defined in the app configuration.
        :param ui_area: String denoting the UI Area (see above).
        :returns List of dictionaries, each with keys name, params, caption and description
        """
        action_instances = super(HoudiniActions, self).generate_actions(sg_publish_data, actions, ui_area)

        if 'file_load' in actions:
            action_instances.append(
                {
                    'name': 'geo_load',
                    'params': None,
                    'caption': 'Geo load',
                    'description': 'This will load files to scene using file node.',
                }
            )
        if 'arnold_load' in actions:
            action_instances.append(
                {
                    'name': 'arnold_load',
                    'params': None,
                    'caption': 'Arnold load',
                    'description': 'Load Arnold .ass files'
                }
            )

        return action_instances

    def execute_action(self, name, params, sg_publish_data):
        """
        Execute a given action. The data sent to this be method will
        represent one of the actions enumerated by the generate_actions method.

        :param name: Action name string representing one of the items returned by generate_actions.
        :param params: Params data, as specified by generate_actions.
        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        :returns: No return value expected.
        """

        super(HoudiniActions, self).execute_action(name, params, sg_publish_data)
        path = self.get_publish_path(sg_publish_data)
        if name == 'geo_load':
            self._geo_load(path, sg_publish_data)
        if name == 'arnold_load':
            self._arnold_load(path, sg_publish_data)

    def _geo_load(self, path, sg_publish_data):
        """
        method which use geometry node to load bgeo and VDB files into Houdini scene
        path: path to the file to load
        sg_publish_data: publish data from Shotgun
        """

        app = self.parent
        name = self.__generate_node_name(sg_publish_data)
        #path = self.__get_houdini_formated_publish_path(sg_publish_data)
        obj_context = _get_current_context('/obj')
        geo_node = self.__create_geo_node(app, obj_context, name)
        file_sop = self.__create_file_sop(app, geo_node, name, path)
        _show_node(file_sop)

    def _arnold_load(self, path, sg_publish_data):
        """
        method which load Arnold ASS files into houdini scene using Arnold procedural Node
        path: path to the file to load
        sg_publish_data: publish data from Shotgun
        """

        app = self.parent
        name =  self.__generate_node_name(sg_publish_data)
        obj_context = _get_current_context('/obj')
        arnold_procedural_node = self.__create_arnold_node(app, obj_context, name)
        self.__load_geometry_to_arnold_node(app, arnold_procedural_node, name, path)

    def __generate_node_name(self, sg_publish_data):
        """
        method generating name for loader node which contain current version number
        sg_publish_data: publish data from Shotgun
        """

        name = self.__get_name_from_publish_data(sg_publish_data)
        version = self.__get_version_from_publish_data(sg_publish_data)
        return '%s_%s' % (name, version)

    def __get_houdini_formated_publish_path(self, sg_publish_data):
        """
        method changing frame sequence convention to work with Houdini, and normalize path separators
        sg_publish_data: publish data from Shotgun
        """

        path = self.get_publish_path(sg_publish_data)
        path = path.replace('\\', '/')
        path = path.replace('%04d', '$F4')
        return path

    @staticmethod
    def __get_name_from_publish_data(sg_publish_data):
        """
        method which obtain name from published data
        sg_publish_data: publish data from Shotgun
        """

        name = sg_publish_data.get('name', 'published_file')
        pattern = re.compile("[\W_]+")
        name = pattern.sub("_", name)
        return name

    @staticmethod
    def __get_version_from_publish_data(sg_publish_data):
        """
        method which obtain version from published data
        sg_publish_data: publish data from Shotgun
        """

        version = sg_publish_data.get('version_number','published_file')
        version = 'v%03d' % version
        return version

    @staticmethod
    def __create_geo_node(app, obj_context, name):
        """
        method for creating geometry node with provided name, which will load bgeo or VDB files
        app: current app
        obj_context: current context
        name: name which will be used for creating node
        """

        try:
            geo_node = obj_context.createNode('geo', name)
        except:
            obj_context = hou.node('/obj')
            geo_node = obj_context.createNode('geo', name)
        app.log_debug("Created geo node: %s" % (geo_node.path(),))
        for child in geo_node.children():
            child.destroy()
        return geo_node

    @staticmethod
    def __create_arnold_node(app, obj_context, name):
        """
        method which create Arnold procedural node
        app: current app
        obj_context: current context
        name: name which will be used for creating node
        """

        try:
            arnold_node = obj_context.createNode('arnold_procedural', name)
        except:
            obj_context = hou.node('/obj')
            arnold_node = obj_context.createNode('arnold_procedural', name)
        app.log_debug("Created geo node: %s" % (arnold_node.path(),))
        return arnold_node

    @staticmethod
    def __create_file_sop(app,geo_node, name, path):
        """
        crate sop node which will load bgeo or VDB file into scene
        app: current app
        geo_node: geo node which will contain this node
        name: name which will be used for creating node
        path: path to file on disk
        """

        file_sop = geo_node.createNode('file', name)
        file_sop.parm('file').set(path)
        app.log_debug(
            'Creating file sop: %s\n  path: "%s" ' % (file_sop.path(), path)
        )
        file_sop.parm('reload').pressButton()
        return file_sop

    @staticmethod
    def __load_geometry_to_arnold_node(app, node, name, path):
        node.parm('ar_filename').set(path)


##############################################################################################################
def _get_current_context(context_type):
    """Attempts to return the current node context.

    :param str context_type: Return a full context under this context type.
        Example: "/obj"

    Looks for a current network pane tab displaying the supplied context type.
    Returns the full context being displayed in that network editor.

    """

    # default to the top level context type
    context = hou.node(context_type)
    network_tab = _get_current_network_panetab(context_type)
    if network_tab:
        context = network_tab.pwd()

    return context


##############################################################################################################
def _get_current_network_panetab(context_type):
    """Attempt to retrieve the current network pane tab.

    :param str context_type: Search for a network pane showing this context
        type. Example: "/obj"

    """

    network_tab = None

    # there doesn't seem to be a way to know the current context "type" since
    # there could be multiple network panels open with different contexts
    # displayed. so for now, loop over pane tabs and find a network editor in
    # the specified context type that is the current tab in its pane. hopefully
    # that's the one the user is looking at.
    for panetab in hou.ui.paneTabs():
        if (
            isinstance(panetab, hou.NetworkEditor)
            and panetab.pwd().path().startswith(context_type)
            and panetab.isCurrentTab()
        ):

            network_tab = panetab
            break

    return network_tab


##############################################################################################################
def _show_node(node):
    """Frame the supplied node in the current network pane.

    :param hou.Node node: The node to frame in the current network pane.

    """

    context_type = "/" + node.path().split("/")[0]
    network_tab = _get_current_network_panetab(context_type)

    if not network_tab:
        return

    # select the node and frame it
    node.setSelected(True, clear_all_selected=True)
    network_tab.cd(node.parent().path())
    network_tab.frameSelection()
