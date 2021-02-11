class BalancerStatus:
	Unknown = 0 # The state is unknown.           
	Running = 1 # Balancer is running.           
	Offline = 2 # Balancer is not running.           
	Stalled = 4 # Balancer has hung or crashed.           
	Error = 5 # Balancer has errored too many times.           


from typing import Iterable
from typing import Text
from typing import Dict
class BalancerInfo(Deadline.MachineInfo):
	"""
	 Information about the current state of Balancer.
	"""

	@property
	def BalancerIsLicensePermanent(self) -> bool:
		"""
		
If the balancer's license is permanent.         
		"""


	@property
	def BalancerLastLicenseErrorMessage(self) -> Text:
		"""
		
The last licensing error message (if there was an error).         
		"""


	@property
	def BalancerLicenseDaysLeftToExpiry(self) -> int:
		"""
		
If the balancer's license isn't permanent, this is the number of days until the license expires.         
		"""


	@property
	def BalancerLicenseServer(self) -> Text:
		"""
		
The license server the balancer is connected to.         
		"""


	@property
	def BalancerName(self) -> Text:
		"""
		
Balancer's name (in the context of Deadline).         
		"""
	@BalancerName.setter
	def BalancerName(self, value: Text): ...


	@property
	def BalancerRegion(self) -> Text:
		"""
		
The Region the Balancer is in.         
		"""


	@property
	def BalancerRunningTime(self) -> int:
		"""
		
Balancer's current running time, in seconds.         
		"""


	@property
	def BalancerState(self) -> Text:
		"""
		
The current state of Balancer.         
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import BalancerSettings
from Deadline.Balancer import BalancerInfo
class BalancerInfoSettings(IComparable):
	"""
	 A wrapper around the balancer's info and settings objects.
	"""

	@property
	def BalancerName(self) -> Text:
		"""
		
The name of the balancer in question.         
		"""


	@property
	def Info(self) -> BalancerInfo:
		"""
		
The BalancerInfo for this Balancer.         
		"""


	@property
	def Settings(self) -> BalancerSettings:
		"""
		
The BalancerSettings for this Balancer.         
		"""

	def CompareTo(self, obj: object) -> int:
		"""
		Compare 2 

		:param object obj: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import BalancerStateStruct
from Deadline.Plugins import PluginConfig
from Deadline.Balancer import BalancerTargetStruct
class BalancerPluginWrapper:
	"""
	 The BalancerPluginWrapper class uses a builder pattern to construct objects. In order for BalancerPluginWrapper
	objects to function properly, you must set the PluginConfig, DataController, and BalancerPluginName, then
	initialize the secret retriever.
	"""

	@property
	def c_secretRetrievalFailureMessage(self) -> conststring:
		"""
		
        
		"""
	@c_secretRetrievalFailureMessage.setter
	def c_secretRetrievalFailureMessage(self, value: conststring): ...


	@property
	def m_balancerPluginConfig(self) -> PluginConfig:
		"""
		
        
		"""
	@m_balancerPluginConfig.setter
	def m_balancerPluginConfig(self, value: PluginConfig): ...


	@property
	def m_balancerPluginName(self) -> Text:
		"""
		
        
		"""
	@m_balancerPluginName.setter
	def m_balancerPluginName(self, value: Text): ...


	@property
	def m_dataController(self) -> DataController:
		"""
		
        
		"""
	@m_dataController.setter
	def m_dataController(self, value: DataController): ...


	@property
	def m_secretRetriever(self) -> PluginSecretRetriever:
		"""
		
        
		"""
	@m_secretRetriever.setter
	def m_secretRetriever(self, value: PluginSecretRetriever): ...


	@property
	def m_secretsManagementEnabled(self) -> bool:
		"""
		
        
		"""
	@m_secretsManagementEnabled.setter
	def m_secretsManagementEnabled(self, value: bool): ...

	def BalancerAlgorithm(self, stateStruct: BalancerStateStruct) -> BalancerTargetStruct:
		"""
		Gets the balancer algorithm. 

		:param BalancerStateStruct stateStruct: 
		:return: 
		"""

	def GetBooleanConfigEntry(self, key: Text) -> bool:
		"""
		Retrieves a config entry as a bool 

		:param Text key: The key of the config entry
		:return: The config entry's value
		"""

	def GetBooleanConfigEntryWithDefault(self, key: Text, defaultValue: bool) -> bool:
		"""
		Retrieves a config entry as a bool 

		:param Text key: The key of the config entry
		:param bool defaultValue: The default value
		:return: The config entry's value, or the provided default if it doesn't exist.
		"""

	def GetConfigEntry(self, key: Text) -> Text:
		"""
		Retrieves the config entry with the given key 

		:param Text key: The key of the Config Entry
		:return: The Config Entry's value
		"""

	def GetConfigEntryWithDefault(self, key: Text, defaultValue: Text) -> Text:
		"""
		Retrieves a config entry 

		:param Text key: The key of the config entry
		:param Text defaultValue: The default value
		:return: The config entry's value, or the provided default if it doesn't exist.
		"""

	def GetDoubleConfigEntryWithDefault(self, key: Text, defaultValue: float) -> float:
		"""
		Retrieves a config entry as a double 

		:param Text key: The key of the config entry
		:param float defaultValue: The default value
		:return: The config entry's value, or the provided default if it doesn't exist.
		"""

	def GetFloatConfigEntry(self, key: Text) -> float:
		"""
		Retrieves a config entry as a float 

		:param Text key: The key of the config entry
		:return: The config entry's value
		"""

	def GetFloatConfigEntryWithDefault(self, key: Text, defaultValue: float) -> float:
		"""
		Retrieves a config entry as a float 

		:param Text key: The key of the config entry
		:param float defaultValue: The default value
		:return: The config entry's value, or the provided default if it doesn't exist.
		"""

	def GetIntegerConfigEntry(self, key: Text) -> int:
		"""
		Retrieves a config entry as an integer 

		:param Text key: The key of the config entry
		:return: The config entry's value
		"""

	def GetIntegerConfigEntryWithDefault(self, key: Text, defaultValue: int) -> int:
		"""
		Retrieves a config entry as an integer 

		:param Text key: The key of the config entry
		:param int defaultValue: The default value
		:return: The config entry's value, or the provided default if it doesn't exist.
		"""

	def GetLongConfigEntry(self, key: Text) -> long:
		"""
		Retrieves a config entry as a long 

		:param Text key: The key of the config entry
		:return: The config entry's value
		"""

	def GetLongConfigEntryWithDefault(self, key: Text, defaultValue: long) -> long:
		"""
		Retrieves a config entry as a long 

		:param Text key: The key of the config entry
		:param long defaultValue: The default value
		:return: The config entry's value, or the provided default if it doesn't exist.
		"""

	def InitializeSecretRetriever(self, ):
		"""
		Initializes the PluginSecretRetriever. The PluginSecretRetriever MUST be initialized for the 

		
		:return: 
		"""

	def ResetBalancerPlugin(self, ):
		"""
		Resets the cloud plugin, cleaning up any resources it might be holding onto 

		
		:return: 
		"""

	def SetBalancerPluginConfig(self, config: PluginConfig):
		"""
		Sets the plugin config 

		:param PluginConfig config: 
		:return: 
		"""

	def SetBalancerPluginName(self, name: Text):
		"""
		Sets the 

		:param Text name: 
		:return: 
		"""

	def SetDataController(self, dataController: DataController):
		"""
		Sets the Data Controller 

		:param DataController dataController: 
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
class BalancerSettings(LastWriteDocument):
	"""
	 Contains settings for the balancer.
	"""

	@property
	def BalancerHostMachineIPAddressOverride(self) -> Text:
		"""
		
If non-empty, this host name or IP address will be used for remote communication with the balancer.         
		"""
	@BalancerHostMachineIPAddressOverride.setter
	def BalancerHostMachineIPAddressOverride(self, value: Text): ...


	@property
	def BalancerIsPrimary(self) -> bool:
		"""
		
Is this balancer the primary balancer?         
		"""
	@BalancerIsPrimary.setter
	def BalancerIsPrimary(self, value: bool): ...


	@property
	def BalancerListeningPort(self) -> int:
		"""
		
The port to use listen on if BalancerOverridePort is enabled.         
		"""
	@BalancerListeningPort.setter
	def BalancerListeningPort(self, value: int): ...


	@property
	def BalancerMacAddressOverride(self) -> Text:
		"""
		
If non-empty, this is used to override the MAC address for the balancer.         
		"""
	@BalancerMacAddressOverride.setter
	def BalancerMacAddressOverride(self, value: Text): ...


	@property
	def BalancerName(self) -> Text:
		"""
		
The Balancer name.         
		"""
	@BalancerName.setter
	def BalancerName(self, value: Text): ...


	@property
	def BalancerOverrideListeningPort(self) -> bool:
		"""
		
If balancer should listen on a specific port.         
		"""
	@BalancerOverrideListeningPort.setter
	def BalancerOverrideListeningPort(self, value: bool): ...


	@property
	def BalancerRegion(self) -> Text:
		"""
		
The Region the Balancer is in.         
		"""
	@BalancerRegion.setter
	def BalancerRegion(self, value: Text): ...


	@property
	def m_balancerName(self) -> Text:
		"""
		
        
		"""
	@m_balancerName.setter
	def m_balancerName(self, value: Text): ...


	@property
	def m_hostMachineIPAddressOverride(self) -> Text:
		"""
		
        
		"""
	@m_hostMachineIPAddressOverride.setter
	def m_hostMachineIPAddressOverride(self, value: Text): ...


	@property
	def m_listeningPort(self) -> int:
		"""
		
        
		"""
	@m_listeningPort.setter
	def m_listeningPort(self, value: int): ...


	@property
	def m_macAddressOverride(self) -> Text:
		"""
		
        
		"""
	@m_macAddressOverride.setter
	def m_macAddressOverride(self, value: Text): ...


	@property
	def m_overrideListeningPort(self) -> bool:
		"""
		
        
		"""
	@m_overrideListeningPort.setter
	def m_overrideListeningPort(self, value: bool): ...


	@property
	def m_primaryBalancer(self) -> bool:
		"""
		
        
		"""
	@m_primaryBalancer.setter
	def m_primaryBalancer(self, value: bool): ...


	@property
	def m_region(self) -> Text:
		"""
		
        
		"""
	@m_region.setter
	def m_region(self, value: Text): ...

	def CompareTo(self, obj: object) -> int:
		"""
		Compare 2 balancer settings by comparing their id's 

		:param object obj: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import CloudRegionTargetStruct
class BalancerTargetStruct:
	"""
	 The BalancerTargetStruct indicates the ideal number of VM instances that should be running in each enabled Group of
	each CloudRegion. The BalancerTargetStruct is populated by a Balancer Logic Plug-in.
	"""

	@property
	def CloudRegionTargets(self) -> Iterable[CloudRegionTargetStruct]:
		"""
		
An array of cloud region targets.         
		"""
	@CloudRegionTargets.setter
	def CloudRegionTargets(self, value: Iterable[CloudRegionTargetStruct]): ...


	@property
	def ErrorEncountered(self) -> bool:
		"""
		
Logic plug-in can set this to true to indicate that an error occurred.         
		"""
	@ErrorEncountered.setter
	def ErrorEncountered(self, value: bool): ...


	@property
	def ErrorMessage(self) -> Text:
		"""
		
Logic plugin can convey an error message here (ErrorEncountered should be set to true).         
		"""
	@ErrorMessage.setter
	def ErrorMessage(self, value: Text): ...


	@property
	def Message(self) -> Text:
		"""
		
Logic plugin can convey a non-error message here.         
		"""
	@Message.setter
	def Message(self, value: Text): ...


	@property
	def Time(self) -> DateTime:
		"""
		
The time the structure was filled.         
		"""
	@Time.setter
	def Time(self, value: DateTime): ...

	def __init__(self, ):
		"""
		Constructor 

		
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import GroupTargetStruct
class CloudRegionTargetStruct:
	"""
	 Cloud region target struct
	"""

	@property
	def GroupTargets(self) -> Iterable[GroupTargetStruct]:
		"""
		
An array of Group targets         
		"""
	@GroupTargets.setter
	def GroupTargets(self, value: Iterable[GroupTargetStruct]): ...


	@property
	def RegionName(self) -> Text:
		"""
		
The name of the region.         
		"""
	@RegionName.setter
	def RegionName(self, value: Text): ...

	def __init__(self, ):
		"""
		Constructor 

		
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class GroupTargetStruct:
	"""
	 Group Target Struct
	"""

	@property
	def Count(self) -> int:
		"""
		
The target number of VM instances for the group.         
		"""
	@Count.setter
	def Count(self, value: int): ...


	@property
	def Name(self) -> Text:
		"""
		
The name of the group.         
		"""
	@Name.setter
	def Name(self, value: Text): ...

	def __init__(self, ):
		"""
		Default constructor 

		
		:return: 
		"""

	def __init__(self, Name: Text, Count: int):
		"""
		Constructor 

		:param Text Name: 
		:param int Count: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import LimitStruct
from Deadline.Balancer import SlaveStruct
from Deadline.Balancer import JobStruct
from Deadline.Balancer import GroupStruct
from Deadline.Balancer import CloudRegionStruct
class BalancerStateStruct:
	"""
	 A BalancerStateStruct holds a deep copy of all state information for consumption by a BalancerLogicPlugin. The
	BalancerStateStruct is strictly a value set, with no backward ties. The BalancerLogicPlugin is free to manipulate
	the struct for its own purposes if desired.
	"""

	@property
	def CloudRegions(self) -> Iterable[CloudRegionStruct]:
		"""
		
Array of CloudRegions pre-sorted by region preference. Only enabled cloud regions are included.         
		"""
	@CloudRegions.setter
	def CloudRegions(self, value: Iterable[CloudRegionStruct]): ...


	@property
	def Groups(self) -> Iterable[GroupStruct]:
		"""
		
Array of cloud-enabled Groups.         
		"""
	@Groups.setter
	def Groups(self, value: Iterable[GroupStruct]): ...


	@property
	def Jobs(self) -> Iterable[JobStruct]:
		"""
		
Array of cloud-eligible Jobs.         
		"""
	@Jobs.setter
	def Jobs(self, value: Iterable[JobStruct]): ...


	@property
	def Limits(self) -> Iterable[LimitStruct]:
		"""
		
Array of (Worker) Limits.         
		"""
	@Limits.setter
	def Limits(self, value: Iterable[LimitStruct]): ...


	@property
	def Slaves(self) -> Iterable[SlaveStruct]:
		"""
		
Array of Workers.         
		"""
	@Slaves.setter
	def Slaves(self, value: Iterable[SlaveStruct]): ...


	@property
	def Time(self) -> DateTime:
		"""
		
The time that this state struct was filled.         
		"""
	@Time.setter
	def Time(self, value: DateTime): ...


	@property
	def Version(self) -> readonlystring:
		"""
		
Version number.         
		"""
	@Version.setter
	def Version(self, value: readonlystring): ...

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import GroupRegionInfoStruct
class CloudRegionStruct:
	"""
	 Cloud region struct.
	"""

	@property
	def Budget(self) -> float:
		"""
		
The maximum aggregate cost capacity of instances running in this cloud region.         
		"""
	@Budget.setter
	def Budget(self, value: float): ...


	@property
	def EnabledGroups(self) -> Iterable[GroupRegionInfoStruct]:
		"""
		
Array of infos about the groups enabled in this cloud region.         
		"""
	@EnabledGroups.setter
	def EnabledGroups(self, value: Iterable[GroupRegionInfoStruct]): ...


	@property
	def ID(self) -> Text:
		"""
		
The unique ID (within scope of provider) of this cloud region.         
		"""
	@ID.setter
	def ID(self, value: Text): ...


	@property
	def Name(self) -> Text:
		"""
		
The human-readable name of this cloud region (not necessarily unique).         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def Preference(self) -> int:
		"""
		
The unique global preference order of this cloud region. Lower numbers are preferred over higher numbers.         
		"""
	@Preference.setter
	def Preference(self, value: int): ...

from typing import Iterable
from typing import Text
from typing import Dict
class GroupRegionInfoStruct:
	"""
	 Group region info struct.
	"""

	@property
	def Cost(self) -> float:
		"""
		
The cost of this Group for this cloud region.         
		"""
	@Cost.setter
	def Cost(self, value: float): ...


	@property
	def Name(self) -> Text:
		"""
		
The unique name of the Deadline Group.         
		"""
	@Name.setter
	def Name(self, value: Text): ...

from typing import Iterable
from typing import Text
from typing import Dict
class GroupStruct:
	"""
	 Group struct.
	"""

	@property
	def EnabledRegions(self) -> Iterable[Text]:
		"""
		
The IDs of the Regions on which this group is enabled (listed in Region-preference order).         
		"""
	@EnabledRegions.setter
	def EnabledRegions(self, value: Iterable[Text]): ...


	@property
	def JobsIDs(self) -> Iterable[Text]:
		"""
		
Array of IDs for jobs in this group.         
		"""
	@JobsIDs.setter
	def JobsIDs(self, value: Iterable[Text]): ...


	@property
	def Name(self) -> Text:
		"""
		
The unique name of this group.         
		"""
	@Name.setter
	def Name(self, value: Text): ...

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import TaskStruct
class JobStruct:
	"""
	 Job struct.
	"""

	@property
	def AssetReadyRegions(self) -> Iterable[Text]:
		"""
		
The regions for which assets are ready for this job, or that have asset checking disabled.         
		"""
	@AssetReadyRegions.setter
	def AssetReadyRegions(self, value: Iterable[Text]): ...


	@property
	def ConcurrentTasks(self) -> int:
		"""
		
Number of concurrent tasks that can be performed by a Worker for this job.         
		"""
	@ConcurrentTasks.setter
	def ConcurrentTasks(self, value: int): ...


	@property
	def Group(self) -> Text:
		"""
		
The group assigned to this job, or blank if none.         
		"""
	@Group.setter
	def Group(self, value: Text): ...


	@property
	def ID(self) -> Text:
		"""
		
The unique ID of this job.         
		"""
	@ID.setter
	def ID(self, value: Text): ...


	@property
	def Limits(self) -> Iterable[Text]:
		"""
		
The names of the Limits used by this job.         
		"""
	@Limits.setter
	def Limits(self, value: Iterable[Text]): ...


	@property
	def Name(self) -> Text:
		"""
		
The human-readable name of this job (not necessarily unique).         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def Priority(self) -> int:
		"""
		
The priority of this job.         
		"""
	@Priority.setter
	def Priority(self, value: int): ...


	@property
	def Tasks(self) -> Iterable[TaskStruct]:
		"""
		
An array of TaskStructs that contain info about each task.         
		"""
	@Tasks.setter
	def Tasks(self, value: Iterable[TaskStruct]): ...

from typing import Iterable
from typing import Text
from typing import Dict
class LimitStruct:
	"""
	 Limit struct.
	"""

	@property
	def CloudStubHolders(self) -> Iterable[Text]:
		"""
		
Cloud-managed Workers holding stubs.         
		"""
	@CloudStubHolders.setter
	def CloudStubHolders(self, value: Iterable[Text]): ...


	@property
	def Limit(self) -> int:
		"""
		
The number of stubs permitted in this limit group.         
		"""
	@Limit.setter
	def Limit(self, value: int): ...


	@property
	def Name(self) -> Text:
		"""
		
The unique name of the limit group.         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def NonCloudStubHolders(self) -> Iterable[Text]:
		"""
		
Non-cloud-managed Workers holding stubs.         
		"""
	@NonCloudStubHolders.setter
	def NonCloudStubHolders(self, value: Iterable[Text]): ...


	@property
	def UnlimitedLimit(self) -> bool:
		"""
		
If the number of stubs permitted by this limit group is unlimited. This value trumps the physical limit. 
        
		"""
	@UnlimitedLimit.setter
	def UnlimitedLimit(self, value: bool): ...

from typing import Iterable
from typing import Text
from typing import Dict
class SlaveStruct:
	"""
	 Worker struct.
	"""

	@property
	def CloudRegion(self) -> Text:
		"""
		
If a cloud Worker, this is the CloudRegion to which it belongs.         
		"""
	@CloudRegion.setter
	def CloudRegion(self, value: Text): ...


	@property
	def CloudSlave(self) -> bool:
		"""
		
True if the Worker is a cloud-managed Worker.         
		"""
	@CloudSlave.setter
	def CloudSlave(self, value: bool): ...


	@property
	def CurrentJobId(self) -> Text:
		"""
		
The ID of the currently loaded job, if any.         
		"""
	@CurrentJobId.setter
	def CurrentJobId(self, value: Text): ...


	@property
	def CurrentJobName(self) -> Text:
		"""
		
The name of the currently loaded job, if any.         
		"""
	@CurrentJobName.setter
	def CurrentJobName(self, value: Text): ...


	@property
	def GroupName(self) -> Text:
		"""
		
If a cloud Worker, this is the Group to which it belongs.         
		"""
	@GroupName.setter
	def GroupName(self, value: Text): ...


	@property
	def Name(self) -> Text:
		"""
		
The unique name of the Worker.         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def SlaveLimitGroupStubs(self) -> Iterable[Text]:
		"""
		
If the Worker is rendering, this is the list of limit group stubs it current has.         
		"""
	@SlaveLimitGroupStubs.setter
	def SlaveLimitGroupStubs(self, value: Iterable[Text]): ...

from typing import Iterable
from typing import Text
from typing import Dict
class TaskStruct:
	"""
	 Task struct.
	"""

	@property
	def CloudSlave(self) -> bool:
		"""
		
True if the Worker is a cloud-managed Worker (Technically this info belongs with the Worker data, but it's intentionally duplicated here for convenience to the BalancerLogicPlugin).         
		"""
	@CloudSlave.setter
	def CloudSlave(self, value: bool): ...


	@property
	def ID(self) -> Text:
		"""
		
The Task id.         
		"""
	@ID.setter
	def ID(self, value: Text): ...


	@property
	def IsPostJobTask(self) -> bool:
		"""
		
True if this is a post job task.         
		"""
	@IsPostJobTask.setter
	def IsPostJobTask(self, value: bool): ...


	@property
	def IsPreJobTask(self) -> bool:
		"""
		
True if this is a pre job task.         
		"""
	@IsPreJobTask.setter
	def IsPreJobTask(self, value: bool): ...


	@property
	def SlaveName(self) -> Text:
		"""
		
The Worker that rendered or is rendering this task.         
		"""
	@SlaveName.setter
	def SlaveName(self, value: Text): ...


	@property
	def Status(self) -> int:
		"""
		
Unknown = 1, Queued = 2, Suspended = 3, Rendering = 4, Completed = 5, Failed = 6, Pending = 8         
		"""
	@Status.setter
	def Status(self, value: int): ...

