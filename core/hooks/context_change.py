# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
This hook gets executed before and after the context changes in Toolkit.
"""

import os
import sgtk
from tank import get_hook_baseclass


class ContextChange(get_hook_baseclass()):
    """
    - If an engine **starts up**, the ``current_context`` passed to the hook
      methods will be ``None`` and the ``next_context`` parameter will be set
      to the context that the engine is starting in.

    - If an engine is being **reloaded**, in the context of an engine restart
      for example, the ``current_context`` and ``next_context`` will usually be
      the same.

    - If a **context switch** is requested, for example when a user switches
      from project to shot mode in Nuke Studio, ``current_context`` and ``next_context``
      will contain two different context.

    .. note::

       These hooks are called whenever the context is being set in Toolkit. It is
       possible that the new context will be the same as the old context. If
       you want to trigger some behavior only when the new one is different
       from the old one, you'll need to compare the two arguments using the
       ``!=`` operator.
    """

    def pre_context_change(self, current_context, next_context):
        """
        Executed before the context has changed.

        The default implementation does nothing.

        :param current_context: The context of the engine.
        :type current_context: :class:`~sgtk.Context`
        :param next_context: The context the engine is switching to.
        :type next_context: :class:`~sgtk.Context`
        """
        pass

    def post_context_change(self, previous_context, current_context):
        """
        Executed after the context has changed.

        The default implementation does nothing.

        :param previous_context: The previous context of the engine.
        :type previous_context: :class:`~sgtk.Context`
        :param current_context: The current context of the engine.
        :type current_context: :class:`~sgtk.Context`
        """

        engine = sgtk.platform.current_engine()

        if engine and engine.name == 'tk-houdini':
            import hou
            if current_context.entity:
                if current_context.entity['type'] == 'Shot':
                    houdini = Houdini(hou, current_context)
                    houdini.load_env()
                else:
                    houdini = Houdini(hou, current_context)
                    houdini.unset_env()
        pass


class Houdini():
    def __init__(self, hou, current_context):
        current_engine = sgtk.platform.current_engine()
        self.tk = current_engine.sgtk
        self.hou = hou
        self.current_context = current_context

    def load_env(self):
        template = self.tk.templates['shot_output_area']
        fields = self.current_context.as_template_fields(template)
        output_path = template.apply_fields(fields)
        self.hou.putenv('JOB', output_path)
        self.hou.allowEnvironmentToOverwriteVariable('JOB', True)

        template = self.tk.templates['shot_work_area']
        work_path = template.apply_fields(fields)
        old_otlscan_paths = self.hou.getenv('HOUDINI_OTLSCAN_PATH_JBASE')
        if old_otlscan_paths is None:
            old_otlscan_paths = ''
        new_otlscan_path = os.path.join(work_path, 'hda')
        otlscan_paths = old_otlscan_paths + os.pathsep + new_otlscan_path
        self.hou.putenv('HOUDINI_OTLSCAN_PATH', otlscan_paths)

    def unset_env(self):
        self.hou.unsetenv('JOB')
        self.hou.unsetenv('HOUDINI_OTLSCAN_PATH')