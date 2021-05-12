import os
import sys
import tank

packages_path = r'\\192.168.1.204\Dane\Shotgun\python_packages\py3'
if packages_path not in sys.path:
    sys.path.append(packages_path)

from dotenv import dotenv_values

class BeforeAppLaunch(tank.Hook):

    def execute(self, app_path, app_args, version, engine_name, **kwargs):
        tk = self.parent.sgtk
        project_path = tk.project_path
        context = tk.context_from_path(project_path)
        if engine_name == 'tk-maya':
            maya_env = self.MayaEnv()
            maya_env.load_env()
        if engine_name == 'tk-houdini':
            houdini_env = self.HoudiniEnv(tk, context, self.__append_env_vars)
            houdini_env.load_env()
            self.parent.log_info('Houdini environment loaded successfully')


    def __append_env_vars(self, env_vars):
        self.parent.log_info(env_vars)
        if env_vars is None:
            return
        for key, value in env_vars.items():
            existing_value = os.environ.get(key)
            if existing_value is None:
                os.environ[key] = value
            else:
                old_env_values_list  = existing_value.split(';')
                new_env_values_list = old_env_values_list + value.split(';')
                env_values_list = list(element for element in new_env_values_list if element != '&')
                env_values_list.append('&')
                path_separator = os.pathsep
                env_values = path_separator.join(env_values_list)
                os.environ[key] = env_values


    class MayaEnv:
        @staticmethod
        def load_env():
            python_path = 'S:/Maya_plugs_prod_v2/scripts;%REDSHIFT_SCRIPT_PATH%'
            sg_python_path = os.getenv('PYTHONPATH')
            python_path = '%s;%s' % (sg_python_path, python_path)
            os.environ['PYTHONPATH'] = python_path


    class HoudiniEnv:
        def __init__(self, tk, context, append_env_vars_method):
            self.__tk = tk
            self.__context = context
            self.__append_env_vars = append_env_vars_method

        def load_env(self):
            self.__load_project_context_env()
            self.__load_global_env()
            # self.__load_default()

        def __load_project_context_env(self):
            houdini_cfg_template = self.__tk.templates['houdini_project_cfg']
            fields = self.__context.as_template_fields(houdini_cfg_template)
            path = houdini_cfg_template.apply_fields(fields)
            env_vars = self.__get_houdini_env_vars(path)
            self.__append_env_vars(env_vars)

        def __get_houdini_env_vars(self, path):
            cfg_path = os.path.join(path, 'houdini.env')
            if os.path.isfile(cfg_path):
                env_vars = dotenv_values(cfg_path)
                ocio_template = self.__tk.templates['ocio']
                ocio_fields = self.__context.as_template_fields(ocio_template)
                ocio_path = ocio_template.apply_fields(ocio_fields)
                env_vars['HOUDINI_OTLSCAN_PATH'] = os.path.join(path, 'otls')
                env_vars['OCIO'] = os.path.join(ocio_path)
                return dict(env_vars)

        def __load_global_env(self):
            path = 'S:/_houdini/houdini.env'
            env_vars = dotenv_values(path)
            env_vars = dict(env_vars)
            if os.path.isfile(path):
                self.__append_env_vars(env_vars)

        def __load_default(self):
            default_vars = {'HOUDINI_OTLSCAN_PATH': '$HFS/houdini/otls'}
            self.__append_env_vars(default_vars)