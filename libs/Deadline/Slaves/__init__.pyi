class SlaveSchedulingMode:
	AllJobs = 0 # The Worker will dequeue any job.           
	MachineJobs = 1 # The Worker will only dequeue jobs submitted by the machine it's running on.           
	UserJobs = 2 # The Worker will only dequeue jobs submitted by specific users.           


class SlaveStatus:
	Unknown = 0 # The Worker's state is unknown.           
	Rendering = 1 # The Worker is rendering.           
	Idle = 2 # The Worker is idle.           
	Offline = 3 # The Worker is offline.           
	Stalled = 4 # The Worker is stalled.           
	StartingJob = 8 # The Worker is starting its job.           
	HouseCleaning = 9 # The Worker is performing house cleaning, repository repair or pending job scan.           


from typing import Iterable
from typing import Text
from typing import Dict
class SlaveInfo(Deadline.MachineInfo):
	"""
	 Information about the current state of a Worker.
	"""

	@property
	def SlaveCompletedTasks(self) -> int:
		"""
		
The number of tasks the Worker has completed for this session.         
		"""


	@property
	def SlaveConfigName(self) -> Text:
		"""
		
The Worker's config name. This is used to differentiate multiple instances of the Worker on the same machine, and is unrelated to the host name of the machine.         
		"""


	@property
	def SlaveCurrentJobGroup(self) -> Text:
		"""
		
If the Worker is rendering, this is the current job's group.         
		"""


	@property
	def SlaveCurrentJobId(self) -> Text:
		"""
		
If the Worker is rendering, this is the current job's ID.         
		"""


	@property
	def SlaveCurrentJobName(self) -> Text:
		"""
		
If the Worker is rendering, this is the current job's name.         
		"""


	@property
	def SlaveCurrentJobPool(self) -> Text:
		"""
		
If the Worker is rendering, this is the current job's pool.         
		"""


	@property
	def SlaveCurrentJobPriority(self) -> int:
		"""
		
If the Worker is rendering, this is the current job's priority.         
		"""


	@property
	def SlaveCurrentJobUserName(self) -> Text:
		"""
		
If the Worker is rendering, this is the current job's user.         
		"""


	@property
	def SlaveCurrentPlugin(self) -> Text:
		"""
		
If the Worker is rendering, this is the plugin it's currently using.         
		"""


	@property
	def SlaveCurrentTaskIds(self) -> Iterable[Text]:
		"""
		
If the Worker is rendering, these are the IDs of the current tasks.         
		"""


	@property
	def SlaveCurrentTaskNames(self) -> Iterable[Text]:
		"""
		
If the Worker is rendering, these are the names of the current tasks.         
		"""


	@property
	def SlaveCurrentTaskProgresses(self) -> Iterable[Text]:
		"""
		
If the Worker is rendering, these are the progress strings of the current tasks.         
		"""


	@property
	def SlaveCurrentTaskRenderTimes(self) -> Iterable[Text]:
		"""
		
If the Worker is rendering, these are the render time strings of the current tasks.         
		"""


	@property
	def SlaveCurrentTaskStatus(self) -> Iterable[Text]:
		"""
		
If the Worker is rendering, these are the status strings of the current tasks.         
		"""


	@property
	def SlaveFailedTasks(self) -> int:
		"""
		
The number of tasks the Worker has reported an error for this session.         
		"""


	@property
	def SlaveFreeMode(self) -> bool:
		"""
		
If the Worker is running in Free Mode.         
		"""


	@property
	def SlaveIsActive(self) -> bool:
		"""
		
If the Worker is in a state we consider active.         
		"""


	@property
	def SlaveIsLicensedByUsage(self) -> bool:
		"""
		
Whether or not the Worker is using UBL.         
		"""


	@property
	def SlaveIsLicensePermanent(self) -> bool:
		"""
		
If the Worker's license is permanent.         
		"""


	@property
	def SlaveLastLicenseErrorMessage(self) -> Text:
		"""
		
The last licensing error message (if there was an error).         
		"""


	@property
	def SlaveLastMessage(self) -> Text:
		"""
		
A message from the Worker that indicates how the Worker was started or shut down.         
		"""


	@property
	def SlaveLicenseDaysLeftToExpiry(self) -> int:
		"""
		
If the Worker's license isn't permanent, this is the number of days until the license expires.         
		"""


	@property
	def SlaveLicenseServer(self) -> Text:
		"""
		
The license server the Worker is connected to.         
		"""


	@property
	def SlaveLimitGroupStubs(self) -> Iterable[Text]:
		"""
		
If the Worker is rendering, this is the list of limit group stubs it currently has.         
		"""


	@property
	def SlaveName(self) -> Text:
		"""
		
The Worker's name in the context of Deadline.         
		"""
	@SlaveName.setter
	def SlaveName(self, value: Text): ...


	@property
	def SlaveOnLastTaskComplete(self) -> Text:
		"""
		
What the Worker will do when it finishes its current task.         
		"""


	@property
	def SlaveRegion(self) -> Text:
		"""
		
The region that the Worker belongs to.         
		"""


	@property
	def SlaveRenderingTime(self) -> int:
		"""
		
If the Worker is rendering, this is how long the Worker has been rendering for, in seconds.         
		"""


	@property
	def SlaveRunningTime(self) -> int:
		"""
		
The Worker's current running time, in seconds.         
		"""


	@property
	def SlaveState(self) -> Text:
		"""
		
The Worker's current state.         
		"""


	@property
	def INACTIVE_SLAVE_STATES(self) -> List[SlaveStatus]:
		"""
		
        
		"""
	@INACTIVE_SLAVE_STATES.setter
	def INACTIVE_SLAVE_STATES(self, value: List[SlaveStatus]): ...


	@property
	def WorkerLastRenderFinishedTime(self) -> DateTime:
		"""
		
The last UTC time Worker exited the Rendering state. If the Worker has not been in the Rendering state yet this value will be null. It should be noted that this field gets update even if the previous render failed, was suspended, etc. It contains no guarantees about whether or not the previous render succeeded.         
		"""
	@WorkerLastRenderFinishedTime.setter
	def WorkerLastRenderFinishedTime(self, value: DateTime): ...

	@staticmethod
	def LegacySetter(existingMode: refLicenseStatus, newMode: LicenseStatus, newModeIsSet: bool):
		"""
		This is a helper function that is used in implementing the setter properties of the old "one per bool" licensing modes. This helps maintain some of the old logic that previously existed. Specifically, if we're clearing a currently set value, then change the enum to be the "Expirable" state, as that was that state that was implied when all the bools where false. 

		:param refLicenseStatus existingMode: 
		:param LicenseStatus newMode: 
		:param bool newModeIsSet: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Slaves import SlaveSettings
from Deadline.Slaves import SlaveInfo
class SlaveInfoSettings:
	"""
	 Holds the SlaveInfo and SlaveSettings for a particular Worker.
	"""

	@property
	def Info(self) -> SlaveInfo:
		"""
		
The SlaveInfo for this Worker.         
		"""
	@Info.setter
	def Info(self, value: SlaveInfo): ...


	@property
	def Settings(self) -> SlaveSettings:
		"""
		
The SlaveSettings for this Worker.         
		"""
	@Settings.setter
	def Settings(self, value: SlaveSettings): ...


	@property
	def SlaveName(self) -> Text:
		"""
		
The name of the Worker in question.         
		"""


	@property
	def m_slaveInfo(self) -> SlaveInfo:
		"""
		
        
		"""
	@m_slaveInfo.setter
	def m_slaveInfo(self, value: SlaveInfo): ...


	@property
	def m_slaveSettings(self) -> SlaveSettings:
		"""
		
        
		"""
	@m_slaveSettings.setter
	def m_slaveSettings(self, value: SlaveSettings): ...

	def __init__(self, slaveInfo: SlaveInfo, slaveSettings: SlaveSettings):
		"""
		Basic Constructor. 

		:param SlaveInfo slaveInfo: 
		:param SlaveSettings slaveSettings: 
		:return: 
		"""

	def __init__(self, ):
		"""
		The constructor. 

		
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class SlaveSettings(LastWriteDocument):
	"""
	 Contains settings for the Worker.
	"""

	@property
	def SlaveComment(self) -> Text:
		"""
		
Brief comment regarding the Worker.         
		"""
	@SlaveComment.setter
	def SlaveComment(self, value: Text): ...


	@property
	def SlaveConcurrentTasksLimit(self) -> int:
		"""
		
Limit the number of concurrent tasks the Worker can dequeue. The value must be between 0 and 16 inclusive. Set to 0 to use the Worker's processor count.         
		"""
	@SlaveConcurrentTasksLimit.setter
	def SlaveConcurrentTasksLimit(self, value: int): ...


	@property
	def SlaveCpuAffinity(self) -> Iterable[int]:
		"""
		
The list of specific CPUs to use if SlaveOverrideCpuAffinity is True.         
		"""
	@SlaveCpuAffinity.setter
	def SlaveCpuAffinity(self, value: Iterable[int]): ...


	@property
	def SlaveDescription(self) -> Text:
		"""
		
A description of the Worker.         
		"""
	@SlaveDescription.setter
	def SlaveDescription(self, value: Text): ...


	@property
	def SlaveEnabled(self) -> bool:
		"""
		
If the Worker is enabled.         
		"""
	@SlaveEnabled.setter
	def SlaveEnabled(self, value: bool): ...


	@property
	def SlaveEnableIdleCpuThreshold(self) -> bool:
		"""
		
If enabled, the Worker will not start when the machine is idle unless the current CPU usage of the machine is lower than the value in SlaveIdleCpuThreshold.         
		"""
	@SlaveEnableIdleCpuThreshold.setter
	def SlaveEnableIdleCpuThreshold(self, value: bool): ...


	@property
	def SlaveEnableIdleProcessCheck(self) -> bool:
		"""
		
If enabled, the Worker will not start when the machine is idle if any processes in SlaveIdleProcessNames are currently running on the machine.         
		"""
	@SlaveEnableIdleProcessCheck.setter
	def SlaveEnableIdleProcessCheck(self, value: bool): ...


	@property
	def SlaveEnableIdleRamMBThreshold(self) -> bool:
		"""
		
If enabled, the Worker will not start when the machine is idle unless the current RAM usage of the machine is lower than the value (in Megabytes) in SlaveEnableIdleRamMBThreshold.         
		"""
	@SlaveEnableIdleRamMBThreshold.setter
	def SlaveEnableIdleRamMBThreshold(self, value: bool): ...


	@property
	def SlaveEnableIdleRamPercentThreshold(self) -> bool:
		"""
		
If enabled, the Worker will not start when the machine is idle unless the current RAM usage of the machine is lower than the value (as a percentage) in SlaveEnableRamPercentThreshold.         
		"""
	@SlaveEnableIdleRamPercentThreshold.setter
	def SlaveEnableIdleRamPercentThreshold(self, value: bool): ...


	@property
	def SlaveEnableIdleUserCheck(self) -> bool:
		"""
		
If enabled, the Worker will not start when the machine is idle if the launcher is running as one of the users in SlaveIdleUserNames.         
		"""
	@SlaveEnableIdleUserCheck.setter
	def SlaveEnableIdleUserCheck(self, value: bool): ...


	@property
	def SlaveExtraInfo0(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo0.setter
	def SlaveExtraInfo0(self, value: Text): ...


	@property
	def SlaveExtraInfo1(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo1.setter
	def SlaveExtraInfo1(self, value: Text): ...


	@property
	def SlaveExtraInfo2(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo2.setter
	def SlaveExtraInfo2(self, value: Text): ...


	@property
	def SlaveExtraInfo3(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo3.setter
	def SlaveExtraInfo3(self, value: Text): ...


	@property
	def SlaveExtraInfo4(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo4.setter
	def SlaveExtraInfo4(self, value: Text): ...


	@property
	def SlaveExtraInfo5(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo5.setter
	def SlaveExtraInfo5(self, value: Text): ...


	@property
	def SlaveExtraInfo6(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo6.setter
	def SlaveExtraInfo6(self, value: Text): ...


	@property
	def SlaveExtraInfo7(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo7.setter
	def SlaveExtraInfo7(self, value: Text): ...


	@property
	def SlaveExtraInfo8(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo8.setter
	def SlaveExtraInfo8(self, value: Text): ...


	@property
	def SlaveExtraInfo9(self) -> Text:
		"""
		
One of the Worker's ten Extra Info fields.         
		"""
	@SlaveExtraInfo9.setter
	def SlaveExtraInfo9(self, value: Text): ...


	@property
	def SlaveExtraInfoDictionary(self) -> Dict[Text,Text]:
		"""
		
A dictionary of Extra Info KVPs.         
		"""
	@SlaveExtraInfoDictionary.setter
	def SlaveExtraInfoDictionary(self, value: Dict[Text,Text]): ...


	@property
	def SlaveFinishTaskWhenStoppingIfNotIdle(self) -> bool:
		"""
		
If a Worker should finish its current task before shutting down when the machine is no longer idle.         
		"""
	@SlaveFinishTaskWhenStoppingIfNotIdle.setter
	def SlaveFinishTaskWhenStoppingIfNotIdle(self, value: bool): ...


	@property
	def SlaveGpuAffinity(self) -> Iterable[int]:
		"""
		
The list of specific GPUs to use if SlaveOverrideGpuAffinity is True.         
		"""
	@SlaveGpuAffinity.setter
	def SlaveGpuAffinity(self, value: Iterable[int]): ...


	@property
	def SlaveGroups(self) -> Iterable[Text]:
		"""
		
The groups that the Worker has been assigned to.         
		"""


	@property
	def SlaveHostMachineIPAddressOverride(self) -> Text:
		"""
		
If non-empty, this host name or IP address will be used for remote communication with the Worker.         
		"""
	@SlaveHostMachineIPAddressOverride.setter
	def SlaveHostMachineIPAddressOverride(self, value: Text): ...


	@property
	def SlaveIdleCpuThreshold(self) -> int:
		"""
		
If CPU threshold checking is enabled, the Worker will not start when the machine is idle unless the current CPU usage of the machine is lower than this value.         
		"""
	@SlaveIdleCpuThreshold.setter
	def SlaveIdleCpuThreshold(self, value: int): ...


	@property
	def SlaveIdleMinutes(self) -> int:
		"""
		
The number of minutes a Worker must be idle for.         
		"""
	@SlaveIdleMinutes.setter
	def SlaveIdleMinutes(self, value: int): ...


	@property
	def SlaveIdleProcessNames(self) -> Iterable[Text]:
		"""
		
The Worker will not start when the machine is idle if any processes in this list are currently running on the machine.         
		"""


	@property
	def SlaveIdleRamMBThreshold(self) -> long:
		"""
		
If RAM MB threshold checking is enabled, the Worker will not start when the machine is idle unless the current RAM usage of the machine is lower than this value (in Megabytes).         
		"""
	@SlaveIdleRamMBThreshold.setter
	def SlaveIdleRamMBThreshold(self, value: long): ...


	@property
	def SlaveIdleRamPercentThreshold(self) -> int:
		"""
		
If RAM Percent threshold checking is enabled, the Worker will not start when the machine is idle unless the current RAM usage of the machine is lower than this value (as a percentage).         
		"""
	@SlaveIdleRamPercentThreshold.setter
	def SlaveIdleRamPercentThreshold(self, value: int): ...


	@property
	def SlaveIdleUserNames(self) -> Iterable[Text]:
		"""
		
If user checking is enabled, the Worker will not start when the machine is idle if the launcher is running as this user.         
		"""


	@property
	def SlaveListeningPort(self) -> int:
		"""
		
The port to use listen on if SlaveOverridePort is enabled.         
		"""
	@SlaveListeningPort.setter
	def SlaveListeningPort(self, value: int): ...


	@property
	def SlaveMacAddressOverride(self) -> Text:
		"""
		
If non-empty, this is used to override the MAC address for the Worker.         
		"""
	@SlaveMacAddressOverride.setter
	def SlaveMacAddressOverride(self, value: Text): ...


	@property
	def SlaveName(self) -> Text:
		"""
		
The Worker name.         
		"""
	@SlaveName.setter
	def SlaveName(self, value: Text): ...


	@property
	def SlaveNormalizedRenderTimeMultiplier(self) -> float:
		"""
		
Used to calculate the normalized render time of the Worker. The value must be between 0.01 and 100.0 inclusive.         
		"""
	@SlaveNormalizedRenderTimeMultiplier.setter
	def SlaveNormalizedRenderTimeMultiplier(self, value: float): ...


	@property
	def SlaveNormalizedTimeoutMultiplier(self) -> float:
		"""
		
Used to calculate the normalized timeout for the Worker. The value must be between 0.01 and 100.0 inclusive.         
		"""
	@SlaveNormalizedTimeoutMultiplier.setter
	def SlaveNormalizedTimeoutMultiplier(self, value: float): ...


	@property
	def SlaveOnlyStopSlaveIfStartedByIdleDetection(self) -> bool:
		"""
		
Only stops the slWorkerave if it was started by idle detection.         
		"""
	@SlaveOnlyStopSlaveIfStartedByIdleDetection.setter
	def SlaveOnlyStopSlaveIfStartedByIdleDetection(self, value: bool): ...


	@property
	def SlaveOverrideCpuAffinity(self) -> bool:
		"""
		
Enable to override the Worker's CPU affinity (Windows and Linux only).         
		"""
	@SlaveOverrideCpuAffinity.setter
	def SlaveOverrideCpuAffinity(self, value: bool): ...


	@property
	def SlaveOverrideGpuAffinity(self) -> bool:
		"""
		
Enable to override the Worker's GPU affinity.         
		"""
	@SlaveOverrideGpuAffinity.setter
	def SlaveOverrideGpuAffinity(self, value: bool): ...


	@property
	def SlaveOverrideListeningPort(self) -> bool:
		"""
		
If Worker should listen on a specific port.         
		"""
	@SlaveOverrideListeningPort.setter
	def SlaveOverrideListeningPort(self, value: bool): ...


	@property
	def SlaveOverrideSlaveScheduling(self) -> bool:
		"""
		
If the Worker settings should override the global Worker Scheduling settings.         
		"""
	@SlaveOverrideSlaveScheduling.setter
	def SlaveOverrideSlaveScheduling(self, value: bool): ...


	@property
	def SlavePools(self) -> Iterable[Text]:
		"""
		
The pools that the Worker has been assigned to.         
		"""


	@property
	def SlaveSchedulingMode(self) -> SlaveSchedulingMode:
		"""
		
Scheduling modes for a Worker, which affects how it dequeues jobs. If set to SlaveSchedulingMode.UserJobs, it will only render jobs for users in the SlaveUserJobsModeNames list.         
		"""
	@SlaveSchedulingMode.setter
	def SlaveSchedulingMode(self, value: SlaveSchedulingMode): ...


	@property
	def SlaveStartSlaveIfIdle(self) -> bool:
		"""
		
Starts the Worker if the machine has been idle for the number of minutes specified in SlaveIdleMinutes.         
		"""
	@SlaveStartSlaveIfIdle.setter
	def SlaveStartSlaveIfIdle(self, value: bool): ...


	@property
	def SlaveStopSlaveIfNotIdle(self) -> bool:
		"""
		
Stops the Worker if the machine is no longer idle.         
		"""
	@SlaveStopSlaveIfNotIdle.setter
	def SlaveStopSlaveIfNotIdle(self, value: bool): ...


	@property
	def SlaveUserJobsModeNames(self) -> Iterable[Text]:
		"""
		
If SlaveSchedulingMode is set to SlaveSchedulingMode.UserJobs, it will only render jobs for users in this list.         
		"""

	def GetSlaveExtraInfoKeys(self, ) -> Iterable[Text]:
		"""
		Gets the keys for the Worker's extra info entries. 

		
		:return: The keys, as a list of strings.
		"""

	def GetSlaveExtraInfoKeyValue(self, key: Text) -> Text:
		"""
		Gets the extra info value for the given key. 

		:param Text key: The key.
		:return: The value as a string. If the key isn't found, an empty string is returned.
		"""

	def GetSlaveExtraInfoKeyValueWithDefault(self, key: Text, defaultValue: Text) -> Text:
		"""
		Gets the extra info value for the given key. 

		:param Text key: The key.
		:param Text defaultValue: The default value
		:return: The value, as a string. If the key isn't found, an empty string is returned.
		"""

	def SetSlaveGroups(self, groups: object):
		"""
		Sets the groups that the Worker has been assigned to. 

		:param object groups: The groups. This should be a list of strings.
		:return: 
		"""

	def SetSlaveIdleProcessNames(self, processNames: object):
		"""
		The Worker will not start when the machine is idle if any processes in this list are currently running on the machine. 

		:param object processNames: The process names. This should be a list of strings.
		:return: 
		"""

	def SetSlaveIdleUserNames(self, userNames: object):
		"""
		If user checking is enabled, the Worker will not start when the machine is idle if the launcher is running as this user. 

		:param object userNames: The user names. This should be a list of strings.
		:return: 
		"""

	def SetSlavePools(self, pools: object):
		"""
		Sets the pools that the Worker has been assigned to. 

		:param object pools: The pools. This should be a list of strings.
		:return: 
		"""

	def SetSlaveUserJobsModeNames(self, userNames: object):
		"""
		If SlaveSchedulingMode is set to 

		:param object userNames: The user names. This should be a list of strings.
		:return: 
		"""

