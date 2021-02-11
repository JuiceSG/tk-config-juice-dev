from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Reports import Report
from Deadline.Jobs import Task
from Deadline.PowerMgmt import MachineStartupOptions
from Deadline.PowerMgmt import MachineRestartOptions
from Deadline.Slaves import SlaveInfo
from Deadline.Jobs import Job
from Deadline.PowerMgmt import ThermalShutdownOptions
from Deadline.PowerMgmt import IdleShutdownOptions
class DeadlineEventListener:
	"""
	 The abstract event plugin class, which is subclassed in the event plugin python script file.
	"""

	@property
	def UseProcessEnvironmentVariablesOnly(self) -> bool:
		"""
		
If True, only the extra environment variables defined for the event plugin will be used. If False (the default behavior), the extra environment variables will be merged with the current environment.         
		"""
	@UseProcessEnvironmentVariablesOnly.setter
	def UseProcessEnvironmentVariablesOnly(self, value: bool): ...


	@property
	def m_eventPlugin(self) -> DeadlineEventPlugin:
		"""
		
        
		"""
	@m_eventPlugin.setter
	def m_eventPlugin(self, value: DeadlineEventPlugin): ...


	@property
	def m_jobRunning(self) -> bool:
		"""
		
        
		"""
	@m_jobRunning.setter
	def m_jobRunning(self, value: bool): ...

	def AddMetaDataEntry(self, key: Text, value: Text):
		"""
		Adds a dictionary entry to the event's metadata. This entry will persist between event triggers. This has no effect if the key already exists. 

		:param Text key: The key.
		:param Text value: The value.
		:return: 
		"""

	def CancelJobSubmission(self, ):
		"""
		

		
		:return: 
		"""

	def ClearProcessEnvironmentVariables(self, ):
		"""
		Clears the extra environment variables for the event plugin. 

		
		:return: 
		"""

	def DeleteMetaDataEntry(self, key: Text):
		"""
		Deletes an existing dictionary entry from the event's metadata. This has no effect if the key does not exist. 

		:param Text key: The key.
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

	def GetDataFilename(self, ) -> Text:
		"""
		Gets the first auxiliary file that was submitted with the job. 

		
		:return: The name of the auxiliary file. If there are no auxiliary files, an empty string is returned.
		"""

	def GetEventDirectory(self, ) -> Text:
		"""
		Gets the event's plugin directory in the Repository. 

		
		:return: The local plugin directory path.
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

	def GetMetaData(self, ) -> Dict[Text,Text]:
		"""
		Gets the full metadata dictionary for the event. 

		
		:return: The metadata dictionary.
		"""

	def GetMetaDataEntry(self, key: Text) -> Text:
		"""
		Gets the value of an existing dictionary entry from the event's metadata. 

		:param Text key: The key.
		:return: The value. Returns null if the key does not exist.
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
		Gets the extra environment variable for the event plugin with the given key. If the variable is not defined, an empty string is returned. 

		:param Text key: The name of the environment variable.
		:return: The value, or an empty string if the variable is not defined.
		"""

	def LogInfo(self, message: Text):
		"""
		Logs an INFO message. 

		:param Text message: The message.
		:return: 
		"""

	def LogMessage(self, message: Text):
		"""
		Logs a message. 

		:param Text message: 
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

	def OnHouseCleaning(self, ):
		"""
		Calls the on house cleaning callback. 

		
		:return: 
		"""

	def OnIdleShutdown(self, groupName: Text, slaveNames: Iterable[Text], idleShutdownOptions: IdleShutdownOptions):
		"""
		Calls the on idle shutdown callback. 

		:param Text groupName: The name of the power management group.
		:param Iterable[Text] slaveNames: The Workers that are being shut down.
		:param IdleShutdownOptions idleShutdownOptions: The idle shutdown options for the power management group that is triggering the shutdown.
		:return: 
		"""

	def OnJobDeleted(self, job: Job):
		"""
		Calls the on job deleted callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobError(self, job: Job, task: Task, errorReport: Report):
		"""
		Calls the on job error callback. 

		:param Job job: 
		:param Task task: 
		:param Report errorReport: 
		:return: 
		"""

	def OnJobFailed(self, job: Job):
		"""
		Calls the on job failed callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobFinished(self, job: Job):
		"""
		Calls the on job finished callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobImported(self, job: Job) -> bool:
		"""
		Calls the on job imported callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobPended(self, job: Job):
		"""
		Calls the on job pending callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobPurged(self, job: Job):
		"""
		Calls the on job purged callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobReleased(self, job: Job):
		"""
		Calls the on job released callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobRequeued(self, job: Job):
		"""
		Calls the on job requeued callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobResumed(self, job: Job):
		"""
		Calls the on job resumed. 

		:param Job job: 
		:return: 
		"""

	def OnJobStarted(self, job: Job):
		"""
		Calls the on job started callback. 

		:param Job job: 
		:return: 
		"""

	def OnJobSubmitted(self, job: Job) -> bool:
		"""
		Calls the on job submitted callback. 

		:param Job job: 
		:return: Should the job be submitted or not.
		"""

	def OnJobSuspended(self, job: Job):
		"""
		Calls the on job suspended callback. 

		:param Job job: 
		:return: 
		"""

	def OnMachineRestart(self, groupName: Text, slaveNames: Iterable[Text], machineRestartOptions: MachineRestartOptions):
		"""
		Calls the on machine restart callback. 

		:param Text groupName: The name of the power management group.
		:param Iterable[Text] slaveNames: The Workers that are being restarted.
		:param MachineRestartOptions machineRestartOptions: The machine restart options for the power management group that is triggering the restart.
		:return: 
		"""

	def OnMachineStartup(self, groupName: Text, slaveNames: Iterable[Text], machineStartupOptions: MachineStartupOptions):
		"""
		Calls the on machine startup callback. 

		:param Text groupName: The name of the power management group.
		:param Iterable[Text] slaveNames: The Workers that are being started up.
		:param MachineStartupOptions machineStartupOptions: The machine startup options for the power management group that is triggering the startup.
		:return: 
		"""

	def OnRepositoryRepair(self, ):
		"""
		Calls the on repository repair callback. 

		
		:return: 
		"""

	def OnSlaveIdle(self, slaveName: Text):
		"""
		Calls the on Worker idle callback. 

		:param Text slaveName: 
		:return: 
		"""

	def OnSlaveInfoUpdate(self, slaveName: Text, slaveInfo: SlaveInfo):
		"""
		Calls the on Worker info updated callback. 

		:param Text slaveName: 
		:param SlaveInfo slaveInfo: 
		:return: 
		"""

	def OnSlaveRendering(self, slaveName: Text, job: Job):
		"""
		calls the on Worker rendering callback. 

		:param Text slaveName: 
		:param Job job: 
		:return: 
		"""

	def OnSlaveStalled(self, slaveName: Text):
		"""
		Calls the on Worker stalled callback. 

		:param Text slaveName: 
		:return: 
		"""

	def OnSlaveStarted(self, slaveName: Text):
		"""
		Calls the on Worker started callback. 

		:param Text slaveName: 
		:return: 
		"""

	def OnSlaveStartingJob(self, slaveName: Text, job: Job):
		"""
		Calls the on Worker starting job callback. 

		:param Text slaveName: 
		:param Job job: 
		:return: 
		"""

	def OnSlaveStopped(self, slaveName: Text):
		"""
		Calls the on Worker stopped callback. 

		:param Text slaveName: 
		:return: 
		"""

	def OnThermalShutdown(self, groupName: Text, slaveNames: Iterable[Text], thermalShutdownOptions: ThermalShutdownOptions):
		"""
		Calls the on thermal shutdown callback. 

		:param Text groupName: The name of the power management group.
		:param Iterable[Text] slaveNames: The Workers that are being shut down.
		:param ThermalShutdownOptions thermalShutdownOptions: The thermal shutdown options for the power management group that is triggering the shutdown.
		:return: 
		"""

	def ProcessEnvironmentVariableExists(self, key: Text) -> bool:
		"""
		Checks if the extra environment with the given key exists. 

		:param Text key: The name of the environment variable.
		:return: True if the variable exists, otherwise False.
		"""

	def ResetEventPlugin(self, ):
		"""
		Resets the event plugin. 

		
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
		Runs a process and waits for it to complete. 

		:param Text executable: The executable to run. If the executable isn't rooted, the current directory will be checked first, followed by all directories in the PATH environment variable.
		:param Text arguments: The arguments to pass to the executable.
		:param Text startupDirectory: The directory to start the exectuable in. Specify an empty string to use directory the executable is in.
		:param int timeoutMilliseconds: The number of milliseconds for the process to exit, otherwise an error is thrown. If this is less than 0, this will block until the process exits.
		:param Text userName: The name of the user to run the process as. This is required for Windows, Linux, and Mac OS X.
		:param Text domain: The user's domain name, which is used to run the process as the given user. This is only required on Windows.
		:param Text password: The user's password, which is used to run the process as the given user. This is only required on Windows.
		:return: The exit code of the process.
		"""

	def SetEventPlugin(self, eventPlugin: DeadlineEventPlugin):
		"""
		Sets the event plugin. 

		:param DeadlineEventPlugin eventPlugin: 
		:return: 
		"""

	def SetProcessEnvironmentVariable(self, key: Text, value: Text):
		"""
		Sets extra environment variables for any processes started by this event plugin. The processes must be started using 

		:param Text key: The name of the environment variable.
		:param Text value: The value.
		:return: 
		"""

	def UpdateMetaDataEntry(self, key: Text, value: Text):
		"""
		Updates an existing dictionary entry to the event's metadata. This entry will persist between event triggers. This has no effect if the key does not exist. 

		:param Text key: The key.
		:param Text value: The value.
		:return: 
		"""

