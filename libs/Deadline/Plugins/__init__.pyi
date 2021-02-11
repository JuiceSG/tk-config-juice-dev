class PluginType:
	Simple = None # A simple plugin that uses a managed process. This is often the choice when using an application's command line renderer to do the rendering.           
	Advanced = None # A more advanced plugin that provides more flexibility and control over the render job.           


from typing import Iterable
from typing import Text
from typing import Dict
from FranticX.Processes import ManagedProcess
from Deadline.Jobs import Job
from Deadline.Jobs import Task
class DeadlinePlugin(FranticX.Processes.ManagedProcess):
	"""
	 The abstract render plugin class, which is subclassed in the plugin python script file.
	"""

	@property
	def PluginType(self) -> PluginType:
		"""
		
Gets or sets the plugin type. Simple plugins just need to define the render execuable, arguments, etc, that are needed to run the process. The managing of the process is handled automatically. Advanced plugins provide a lot more control, but the managing of any rendering processes must be done manually.         
		"""
	@PluginType.setter
	def PluginType(self, value: PluginType): ...


	@property
	def SingleFramesOnly(self) -> bool:
		"""
		
Gets or sets if the plugin can only render one frame at a time.         
		"""
	@SingleFramesOnly.setter
	def SingleFramesOnly(self, value: bool): ...


	@property
	def UseProcessEnvironmentVariablesOnly(self) -> bool:
		"""
		
If True, only the extra environment variables defined for the plugin will be used. If False (the default behavior), the extra environment variables will be merged with the current environment.         
		"""
	@UseProcessEnvironmentVariablesOnly.setter
	def UseProcessEnvironmentVariablesOnly(self, value: bool): ...

	def CancelTask(self, ):
		"""
		Sets a flag to cancel the current task if possible. 

		
		:return: 
		"""

	def CheckForMonitoredManagedProcessPopups(self, name: Text) -> Text:
		"""
		Checks if the managed process has displayed any popups. If an unhandled popup is detected, an error message will be returned. Otherwise, this returns an empty string. 

		:param Text name: The unique name to identify the process.
		:return: An error message if an unhandled popup was detected. If no popup was detected, an empty string is returned.
		"""

	def ClearProcessEnvironmentVariables(self, ):
		"""
		Clears the extra environment variables for the plugin. 

		
		:return: 
		"""

	def CpuAffinity(self, ) -> Iterable[int]:
		"""
		Gets the Worker's CPU affinity if OverrideCpuAffinity is True. 

		
		:return: The list of CPU ids.
		"""

	def CreateCommandFile(self, filename: Text, command: Text):
		"""
		Creates a text file with the given command in it. This is useful when running programs that use file-based communication. 

		:param Text filename: The name of the file. If it exists, it will be overwritten.
		:param Text command: The command to write to the file.
		:return: 
		"""

	def CreateTempDirectory(self, prefix: Text) -> Text:
		"""
		Creates a temporary directory using the specified prefix. This directory is created in the local Worker's job folder. It will be cleaned up automatically when the Worker starts a new job. 

		:param Text prefix: The prefix for the temp directory.
		:return: 
		"""

	def DebugMessage(self, message: Text):
		"""
		Logs a DEBUG message. DEBUG messages are only visible if "DebugLogging=true" is set in the plugin's param file. 

		:param Text message: The message.
		:return: 
		"""

	def DetachMonitoredManagedProcess(self, name: Text):
		"""
		Detaches from a managed process. If the render finishes, the process will be left running. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def DetachMonitoredProgram(self, name: Text):
		"""
		Detaches from a monitored process. If the render finishes, the process will be left running. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def ExitWithSuccess(self, ):
		"""
		This will cause the render to finish immediately, and the task will be completed. 

		
		:return: 
		"""

	def FailRender(self, message: Text):
		"""
		Fails the render. This will requeue the task and create an error report. This is the same as calling 

		:param Text message: The message that will appear in the error report.
		:return: 
		"""

	def FlushMonitoredManagedProcessStdout(self, name: Text):
		"""
		Flushes the stdout for the managed process. This should be called occassionally so that the process' stdout is logged, and for stdout handling to work. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def FlushMonitoredManagedProcessStdoutNoHandling(self, name: Text):
		"""
		Flushes the stdout for the managed process. This works the same as FlushMonitoredManagedProcessStdout, except that no stdout handling is performed on the stdout that is flushed. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def GetAuxiliaryFilenames(self, ) -> Iterable[Text]:
		"""
		Gets the list of auxiliary files that were submitted with the job. 

		
		:return: The list of auxiliary files.
		"""

	def GetBooleanConfigEntry(self, key: Text) -> bool:
		"""
		Gets a value as a bool from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetBooleanConfigEntryWithDefault(self, key: Text, defaultValue: bool) -> bool:
		"""
		Gets a value as a bool from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param bool defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetBooleanPluginInfoEntry(self, key: Text) -> bool:
		"""
		Gets the job's plugin info value as a bool for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetBooleanPluginInfoEntryWithDefault(self, key: Text, defaultValue: bool) -> bool:
		"""
		Gets the job's plugin info value as a bool for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param bool defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetConfigEntry(self, key: Text) -> Text:
		"""
		Gets a value from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetConfigEntryWithDefault(self, key: Text, defaultValue: Text) -> Text:
		"""
		Gets a value from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param Text defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetCurrentTask(self, ) -> Task:
		"""
		Gets the current Task that is being rendered. 

		
		:return: 
		"""

	def GetCurrentTaskId(self, ) -> Text:
		"""
		Gets the ID of the task that is being rendered. 

		
		:return: The task ID, as a string.
		"""

	def GetDataFilename(self, ) -> Text:
		"""
		Gets the first auxiliary file that was submitted with the job. 

		
		:return: The name of the auxiliary file. If there are no auxiliary files, an empty string is returned.
		"""

	def GetEndFrame(self, ) -> int:
		"""
		Gets the last frame for the current task. If task only contains one frame, or if this plugin only supports single frames, this will be the same frame returned by 

		
		:return: The last frame, or -1 if there are no frames in the task or there is no current task.
		"""

	def GetFloatConfigEntry(self, key: Text) -> float:
		"""
		Gets a value as a float from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetFloatConfigEntryWithDefault(self, key: Text, defaultValue: float) -> float:
		"""
		Gets a value as a float from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param float defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetFloatPluginInfoEntry(self, key: Text) -> float:
		"""
		Gets the job's plugin info value as a float for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetFloatPluginInfoEntryWithDefault(self, key: Text, defaultValue: float) -> float:
		"""
		Gets the job's plugin info value as a float for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param float defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetIntegerConfigEntry(self, key: Text) -> int:
		"""
		Gets a value as an integer from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetIntegerConfigEntryWithDefault(self, key: Text, defaultValue: int) -> int:
		"""
		Gets a value as an integer from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param int defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetIntegerPluginInfoEntry(self, key: Text) -> int:
		"""
		Gets the job's plugin info value as an integer for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetIntegerPluginInfoEntryWithDefault(self, key: Text, defaultValue: int) -> int:
		"""
		Gets the job's plugin info value as an integer for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param int defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetJob(self, ) -> Job:
		"""
		Gets the job that is being rendered. 

		
		:return: The job object.
		"""

	def GetJobInfoEntry(self, propertyName: Text) -> Text:
		"""
		Gets the value of the Job Property with the given name. 

		:param Text propertyName: The name of the Job property to get.
		:return: The Job property's value.
		"""

	def GetJobInfoEntryElement(self, propertyName: Text, arrayPosition: int) -> Text:
		"""
		Returns the element at a specific position in a Job Property (the property specified must be an Array). 

		:param Text propertyName: The name of the Job property from which to obtain the element.
		:param int arrayPosition: The position of the element to query.
		:return: The element at the specified position within the Job's array property.
		"""

	def GetJobInfoEntryElementCount(self, propertyName: Text) -> int:
		"""
		Gets the number of elements in a Job Property (the property specified must be an Array). 

		:param Text propertyName: The name of the Job property to count.
		:return: The number of elements in the array property.
		"""

	def GetJobsDataDirectory(self, ) -> Text:
		"""
		Gets the Worker's local job directory where the job's auxiliary files are copied before rendering. 

		
		:return: The local job directory path.
		"""

	def GetLongConfigEntry(self, key: Text) -> long:
		"""
		Gets a value as a long from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetLongConfigEntryWithDefault(self, key: Text, defaultValue: long) -> long:
		"""
		Gets a value as a long from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param long defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetLongPluginInfoEntry(self, key: Text) -> long:
		"""
		Gets the job's plugin info value as a long for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetLongPluginInfoEntryWithDefault(self, key: Text, defaultValue: long) -> long:
		"""
		Gets the job's plugin info value as a long for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param long defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetManagedProcessIDs(self, ) -> Iterable[uint]:
		"""
		Gets the process ids for the managed processes for this plugin. 

		
		:return: 
		"""

	def GetMonitoredManagedProcessExitCode(self, name: Text) -> int:
		"""
		Gets the exit code of a managed process. 

		:param Text name: The unique name to identify the process.
		:return: The exit code.
		"""

	def GetMonitoredManagedProcessIDs(self, name: Text) -> Iterable[uint]:
		"""
		Gets the process IDs for the managed process and all of its child processes. 

		:param Text name: The unique name to identify the process.
		:return: The list of process IDs.
		"""

	def GetPluginDirectory(self, ) -> Text:
		"""
		Gets the Worker's local plugin directory where the job's plugin is copied before rendering. 

		
		:return: The local plugin directory path.
		"""

	def GetPluginInfoEntry(self, key: Text) -> Text:
		"""
		Gets the job's plugin info value for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetPluginInfoEntryWithDefault(self, key: Text, defaultValue: Text) -> Text:
		"""
		Gets the job's plugin info value for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param Text defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetProcessEnvironmentVariable(self, key: Text) -> Text:
		"""
		Gets the extra environment variable for the plugin with the given key. If the variable is not defined, an empty string is returned. 

		:param Text key: The name of the environment variable.
		:return: The value, or an empty string if the variable is not defined.
		"""

	def GetRenderExecutable(self, key: Text) -> Text:
		"""
		Gets a render executable from the plugin's configuration for a given key. If the key doesn't exist, or no render executables could be found a 

		:param Text key: The name of the plugin configuration entry.
		:return: The render executable.
		"""

	def GetRenderExecutable(self, key: Text, prettyName: Text) -> Text:
		"""
		Gets a render executable from the plugin's configuration for a given key. If the key doesn't exist, or no render executables could be found a 

		:param Text key: The name of the plugin configuration entry.
		:param Text prettyName: 
		:return: The render executable.
		"""

	def GetSlaveDirectory(self, ) -> Text:
		"""
		Gets the Worker's local directory where it stores the job's plugin and auxiliary files. 

		
		:return: The local Worker directory path.
		"""

	def GetSlaveName(self, ) -> Text:
		"""
		Gets the name of the Worker that is rendering this task. 

		
		:return: The Worker name.
		"""

	def GetStartFrame(self, ) -> int:
		"""
		Gets the first frame for the current task. 

		
		:return: The first frame, or -1 if there are no frames in the task or there is no current task.
		"""

	def GetThreadNumber(self, ) -> int:
		"""
		Gets the ID of the Worker's render thread that is rendering this task. 

		
		:return: The thread ID as an integer.
		"""

	def GpuAffinity(self, ) -> Iterable[int]:
		"""
		Gets the Worker's GPU affinity if OverrideGpuAffinity is True. 

		
		:return: The list of GPU ids.
		"""

	def IsCanceled(self, ) -> bool:
		"""
		Checks if the render has been cancelled. This should be used by advanced plugins to determine if the render has been canceled, and then perform any necessary cleanup. For simple plugins, cancelled renders are handled automatically. 

		
		:return: 
		"""

	def IsMaintenanceJob(self, ) -> bool:
		"""
		Gets if the current job is a maintenance job. 

		
		:return: True if the job is a maintence job.
		"""

	def IsRunningAsService(self, ) -> bool:
		"""
		Gets if the Worker is running as a service (Windows only). 

		
		:return: True if the Worker is running as a service. False is always returned on Linux and OSX.
		"""

	def IsTileJob(self, ) -> bool:
		"""
		Gets if the current job is a tile job. 

		
		:return: True if the job is a tile job.
		"""

	def LogInfo(self, message: Text):
		"""
		Logs an INFO message. 

		:param Text message: The message.
		:return: 
		"""

	def LogStdout(self, message: Text):
		"""
		Logs a STDOUT message. 

		:param Text message: The message.
		:return: 
		"""

	def LogWarning(self, message: Text):
		"""
		Logs a WARNING message. 

		:param Text message: The message.
		:return: 
		"""

	def MonitoredManagedProcessIsRunning(self, name: Text) -> bool:
		"""
		Checks if a managed process is still running. 

		:param Text name: The unique name to identify the process.
		:return: True if the process is running.
		"""

	def MonitoredProgramIsRunning(self, name: Text) -> bool:
		"""
		Checks if a monitored program is still running. 

		:param Text name: The unique name to identify the process.
		:return: True if the program is running.
		"""

	def OverrideCpuAffinity(self, ) -> bool:
		"""
		Gets if the Worker is overriding its CPU affinity. 

		
		:return: True if the Worker is overriding its CPU affinity.
		"""

	def OverrideGpuAffinity(self, ) -> bool:
		"""
		Gets if the Worker is overriding its GPU affinity. 

		
		:return: True if the Worker is overriding its GPU affinity.
		"""

	def ProcessEnvironmentVariableExists(self, key: Text) -> bool:
		"""
		Checks if the extra environment with the given key exists. 

		:param Text key: The name of the environment variable.
		:return: True if the variable exists, otherwise False.
		"""

	def RedirectStdOutToFileForMonitoredManagedProcess(self, name: Text, filename: Text):
		"""
		Redirect stdout for this managed process to the specified file. 

		:param Text name: The unique name to identify the process.
		:param Text filename: The name of the file. If the file already exists, it will be overwritten.
		:return: 
		"""

	def RunManagedProcess(self, managedProcess: ManagedProcess):
		"""
		Runs the given ManagedProcess object. The managing of this process will be handled automatically. This function blocks until the process has finished. 

		:param ManagedProcess managedProcess: The ManagedProcess object.
		:return: 
		"""

	def RunManagedProcessAsUser(self, managedProcess: ManagedProcess, userName: Text, domain: Text, password: Text, useSu: bool, preserveEnvironment: bool, setHomeVariable: bool):
		"""
		Runs the given ManagedProcess object as the given user. The managing of this process will be handled automatically. This function blocks until the process has finished. 

		:param ManagedProcess managedProcess: The ManagedProcess object.
		:param Text userName: The name of the user to run the process as. This is required for Windows, Linux, and Mac OS X.
		:param Text domain: The user's domain name, which is used to run the process as the given user. This is only required on Windows.
		:param Text password: The user's password, which is used to run the process as the given user. This is only required on Windows.
		:param bool useSu: If true, 'su' will be used to run the process as another user instead of 'sudo' (if runAsUser is enabled). This is ignored on Windows.
		:param bool preserveEnvironment: If true, the environment will be preserved when running the process as another user using 'su' or 'sudo' (if runAsUser is enabled). This is ignored on Windows.
		:param bool setHomeVariable: If true, the HOME environment variable will be set to the users home directory when running sudo. Not compatible with su. This is ignored on Windows.
		:return: 
		"""

	def RunProcess(self, executable: Text, arguments: Text, startupDirectory: Text, timeoutMilliseconds: int) -> int:
		"""
		Runs a process and waits for it to complete. 

		:param Text executable: The executable to run. If the executable isn't rooted, the current directory will be checked first, followed by all directories in the PATH environment variable.
		:param Text arguments: The arguments to pass to the executable.
		:param Text startupDirectory: The directory to start the exectuable in. Specify an empty string to use directory the executable is in.
		:param int timeoutMilliseconds: The number of milliseconds for the process to exit, otherwise an error is thrown. If this is less than 0, this will block until the process exits.
		:return: The exit code of the process.
		"""

	def RunProcessAsUser(self, executable: Text, arguments: Text, startupDirectory: Text, timeoutMilliseconds: int, userName: Text, domain: Text, password: Text) -> int:
		"""
		Runs a process as the given user and waits for it to complete. 

		:param Text executable: The executable to run. If the executable isn't rooted, the current directory will be checked first, followed by all directories in the PATH environment variable.
		:param Text arguments: The arguments to pass to the executable.
		:param Text startupDirectory: The directory to start the exectuable in. Specify an empty string to use directory the executable is in.
		:param int timeoutMilliseconds: The number of milliseconds for the process to exit, otherwise an error is thrown. If this is less than 0, this will block until the process exits.
		:param Text userName: The name of the user to run the process as. This is required for Windows, Linux, and Mac OS X.
		:param Text domain: The user's domain name, which is used to run the process as the given user. This is only required on Windows.
		:param Text password: The user's password, which is used to run the process as the given user. This is only required on Windows.
		:return: The exit code of the process.
		"""

	def RunProcessAsUser(self, executable: Text, arguments: Text, startupDirectory: Text, timeoutMilliseconds: int, userName: Text, domain: Text, password: Text, useSu: bool, preserveEnvironment: bool, setHomeVariable: bool) -> int:
		"""
		Runs a process as the given user and waits for it to complete. 

		:param Text executable: The executable to run. If the executable isn't rooted, the current directory will be checked first, followed by all directories in the PATH environment variable.
		:param Text arguments: The arguments to pass to the executable.
		:param Text startupDirectory: The directory to start the exectuable in. Specify an empty string to use directory the executable is in.
		:param int timeoutMilliseconds: The number of milliseconds for the process to exit, otherwise an error is thrown. If this is less than 0, this will block until the process exits.
		:param Text userName: The name of the user to run the process as. This is required for Windows, Linux, and Mac OS X.
		:param Text domain: The user's domain name, which is used to run the process as the given user. This is only required on Windows.
		:param Text password: The user's password, which is used to run the process as the given user. This is only required on Windows.
		:param bool useSu: If true, 'su' will be used to run the process as another user instead of 'sudo' (if runAsUser). This is ignored on Windows.
		:param bool preserveEnvironment: If true, the environment will be preserved when running the process as another user using 'su' or 'sudo' (if runAsUser). This is ignored on Windows.
		:param bool setHomeVariable: If true, a flag will be passed to 'sudo' when running running as another user to inherit the user's home directory. This is ignored on Windows.
		:return: The exit code of the process.
		"""

	def SetMonitoredManagedProcessExitCheckingFlag(self, name: Text, flag: bool):
		"""
		By default, if a managed process exits unexpectedly, an error whill be thrown. If this flag is set to False, no error will be thrown if the process exits. 

		:param Text name: The unique name to identify the process.
		:param bool flag: The flag value.
		:return: 
		"""

	def SetMonitoredProgramExitCheckingFlag(self, name: Text, flag: bool):
		"""
		By default, if a monitored program exits unexpectedly, an error whill be thrown. If this flag is set to False, no error will be thrown if the program exits. 

		:param Text name: The unique name to identify the process.
		:param bool flag: The flag value.
		:return: 
		"""

	def SetProcessEnvironmentVariable(self, key: Text, value: Text):
		"""
		Sets extra environment variables for any processes started by this plugin. The processes must be started using 

		:param Text key: The name of the environment variable.
		:param Text value: The value.
		:return: 
		"""

	def SetProgress(self, percent: float):
		"""
		Sets the Worker's current progress. 

		:param float percent: A value between 0.0 and 100.0 inclusive.
		:return: 
		"""

	def SetStatusMessage(self, status: Text):
		"""
		Sets the Worker's status message. 

		:param Text status: The status message.
		:return: 
		"""

	def ShutdownMonitoredManagedProcess(self, name: Text):
		"""
		Stops the managed process. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def ShutdownMonitoredProgram(self, name: Text):
		"""
		Stops the monitored process. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def StartMonitoredManagedProcess(self, name: Text, managedProcess: ManagedProcess):
		"""
		Runs the given ManagedProcess object. The managing of this process must be handled manually. This function will return as soon as the process has started. 

		:param Text name: The unique name to identify the process. This is necessary if the plugin is running more than one managaed process.
		:param ManagedProcess managedProcess: The ManagedProcess object.
		:return: 
		"""

	def StartMonitoredManagedProcessAsUser(self, name: Text, managedProcess: ManagedProcess, userName: Text, domain: Text, password: Text, useSu: bool, preserveEnvironment: bool, setHomeVariable: bool):
		"""
		Runs the given ManagedProcess object as the given user. The managing of this process must be handled manually. This function will return as soon as the process has started. 

		:param Text name: The unique name to identify the process. This is necessary if the plugin is running more than one managaed process.
		:param ManagedProcess managedProcess: The ManagedProcess object.
		:param Text userName: The name of the user to run the process as. This is required for Windows, Linux, and Mac OS X.
		:param Text domain: The user's domain name, which is used to run the process as the given user. This is only required on Windows.
		:param Text password: The user's password, which is used to run the process as the given user. This is only required on Windows.
		:param bool useSu: If true, 'su' will be used to run the process as another user instead of 'sudo' (if runAsUser). This is ignored on Windows.
		:param bool preserveEnvironment: If true, the environment will be preserved when running the process as another user using 'su' or 'sudo' (if runAsUser). This is ignored on Windows.
		:param bool setHomeVariable: If true, the HOME environment variable will be set to the users home directory when running sudo. Not compatible with su. This is ignored on Windows.
		:return: 
		"""

	def StartMonitoredProgram(self, name: Text, executable: Text, arguments: Text, startupDirectory: Text):
		"""
		Runs a monitored process. The process is monitored while it is running to determine if it exits unexpectedly, and it will be stopped automatically when the task is finished. 

		:param Text name: A unique name to identify the process. This is necessary if the plugin is running more than one monitored program.
		:param Text executable: The executable to run. If the executable isn't rooted, the current directory will be checked first, followed by all directories in the PATH environment variable.
		:param Text arguments: The arguments to pass to the executable.
		:param Text startupDirectory: The directory to start the exectuable in. Specify an empty string to use directory the executable is in.
		:return: 
		"""

	def StartMonitoredProgramAsUser(self, name: Text, executable: Text, arguments: Text, startupDirectory: Text, userName: Text, domain: Text, password: Text, useSu: bool, preserveEnvironment: bool, setHomeVariable: bool):
		"""
		Runs a monitored process as the given user. The process is monitored while it is running to determine if it exits unexpectedly, and it will be stopped automatically when the task is finished. 

		:param Text name: A unique name to identify the process. This is necessary if the plugin is running more than one monitored program.
		:param Text executable: The executable to run. If the executable isn't rooted, the current directory will be checked first, followed by all directories in the PATH environment variable.
		:param Text arguments: The arguments to pass to the executable.
		:param Text startupDirectory: The directory to start the exectuable in. Specify an empty string to use directory the executable is in.
		:param Text userName: The name of the user to run the process as. This is required for Windows, Linux, and Mac OS X.
		:param Text domain: The user's domain name, which is used to run the process as the given user. This is only required on Windows.
		:param Text password: The user's password, which is used to run the process as the given user. This is only required on Windows.
		:param bool useSu: If true, 'su' will be used to run the process as another user instead of 'sudo' (if runAsUser is set). This is ignored on Windows.
		:param bool preserveEnvironment: If true, the environment will be preserved when running the process as another user using 'su' or 'sudo' (if runAsUser is set). This is ignored on Windows.
		:param bool setHomeVariable: If true, the HOME environment variable will be set to the users home directory when running sudo. Not compatible with su. This is ignored on Windows.
		:return: 
		"""

	def VerifyAndMoveDirectory(self, source: Text, destination: Text, failIfEmpty: bool, fileSize: int):
		"""
		Moves the files from the source directory to the destination directory. It can verify that the source directory isn't empty and throw an error if it is. 

		:param Text source: The source directory.
		:param Text destination: The destination directory.
		:param bool failIfEmpty: If True, an error will be thrown if the source directory is empty, or if there are any files in it below the specified file size.
		:param int fileSize: The minimum file size. If less than 0, the file size isn't checked.
		:return: 
		"""

	def VerifyAndMoveFile(self, source: Text, destination: Text, fileSize: int):
		"""
		Moves the given file to the destination. It can verify that the file is above a certain size and throw an error if it is not. 

		:param Text source: The source file name.
		:param Text destination: The destination file name.
		:param int fileSize: The minimum file size. If less than 0, the file size isn't checked.
		:return: 
		"""

	def VerifyFile(self, filename: Text, fileSize: int):
		"""
		Checks that the file is larger than the given size, and throws an error if it is not. 

		:param Text filename: The file name.
		:param int fileSize: The minimum file size. If less than 0, the file size isn't checked, in which case this function does nothing.
		:return: 
		"""

	def VerifyMonitoredManagedProcess(self, name: Text):
		"""
		Automatically throws an error if the managed process is no longer running. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def VerifyMonitoredProgram(self, name: Text):
		"""
		Automatically throws an error if the monitored program is no longer running. 

		:param Text name: The unique name to identify the process.
		:return: 
		"""

	def WaitForCommandFile(self, filename: Text, delete: bool, timeoutMilliseconds: int) -> Text:
		"""
		Waits until a text file with the given name exists. The contents of the file are then returned. 

		:param Text filename: The name of the file.
		:param bool delete: If True, the file will be automatically deleted after the contents have been read in.
		:param int timeoutMilliseconds: The number of milliseconds to wait for the file to appear. If the timeout is reached, an empty string is returned. If this is less than 0, this will blcok until the file exists.
		:return: The contents of the text file, or an empty string if the timeout was reached.
		"""

	def WaitForMonitoredManagedProcessToExit(self, name: Text, timeoutMilliseconds: int) -> bool:
		"""
		Blocks until a managed process exits, or the timeout is reached. 

		:param Text name: The unique name to identify the process.
		:param int timeoutMilliseconds: The timeout, in milliseconds. If less than 0, this function will block until the process exits.
		:return: True if the process exited before the timeout.
		"""

	def WaitForMonitoredProgramToExit(self, name: Text, timeoutMilliseconds: int) -> bool:
		"""
		Blocks until a monitored program exits, or the timeout is reached. 

		:param Text name: The unique name to identify the process.
		:param int timeoutMilliseconds: The timeout, in milliseconds. If less than 0, this function will block until the program exits.
		:return: True if the program exited before the timeout.
		"""

	def WriteStdinToMonitoredManagedProcess(self, name: Text, stdin: Text):
		"""
		Writes input to the managed process' stding pipe. 

		:param Text name: The unique name to identify the process.
		:param Text stdin: The input to write.
		:return: 
		"""

	def GenericGetConfigEntry< T >(self, key: Text) -> T:
		"""
		

		:param Text key: 
		:return: 
		"""

	def GenericGetConfigEntryWithDefault< T >(self, key: Text, defaultValue: T) -> T:
		"""
		

		:param Text key: 
		:param T defaultValue: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class FailRenderException(ManagedProcessAbort):
	"""
	 An exception thrown to indicate that the Render has failed.
	"""
	def __init__(self, message: Text, level: ManagedProcess.AbortLevel):
		"""
		Basic constructor. 

		:param Text message: The error message pertaining to the failure.
		:param ManagedProcess.AbortLevel level: The level of severity of this failure.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class PluginConfig:
	"""
	 Contains the configuration settings for a render or event plugin.
	"""
	def ConfigEntryIsPassword(self, key: Text) -> bool:
		"""
		Determines whether or not a plugin entry is of type "password". 

		:param Text key: The name of the plugin info entry.
		:return: The Type value.
		"""

	def GetBooleanConfigEntry(self, key: Text) -> bool:
		"""
		Gets a value as a bool from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetBooleanConfigEntryWithDefault(self, key: Text, defaultValue: bool) -> bool:
		"""
		Gets a value as a bool from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param bool defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetConfigEntry(self, key: Text) -> Text:
		"""
		Gets a value from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetConfigEntryType(self, key: Text) -> Text:
		"""
		Get the Type value of a plugin info entry. 

		:param Text key: The name of the plugin info entry.
		:return: The Type value.
		"""

	def GetConfigEntryWithDefault(self, key: Text, defaultValue: Text) -> Text:
		"""
		Gets a value from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param Text defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetConfigKeys(self, ) -> Iterable[Text]:
		"""
		Gets the list of 

		
		:return: The list of keys.
		"""

	def GetDoubleConfigEntryWithDefault(self, key: Text, defaultValue: float) -> float:
		"""
		Gets a value as a double from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param float defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetFloatConfigEntry(self, key: Text) -> float:
		"""
		Gets a value as a float from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetFloatConfigEntryWithDefault(self, key: Text, defaultValue: float) -> float:
		"""
		Gets a value as a float from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param float defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetIntegerConfigEntry(self, key: Text) -> int:
		"""
		Gets a value as an integer from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetIntegerConfigEntryWithDefault(self, key: Text, defaultValue: int) -> int:
		"""
		Gets a value as an integer from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param int defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

	def GetLongConfigEntry(self, key: Text) -> long:
		"""
		Gets a value as a long from the plugin's configuration for the given key. 

		:param Text key: The name of the plugin info entry. An error is thrown if the key is not defined.
		:return: The value.
		"""

	def GetLongConfigEntryWithDefault(self, key: Text, defaultValue: long) -> long:
		"""
		Gets a value as a long from the plugin's configuration for the given key. If the key doesn't exist, the default value is returned. 

		:param Text key: The name of the plugin info entry.
		:param long defaultValue: The default value.
		:return: The value. If the given key does not exist, the default value is returned.
		"""

