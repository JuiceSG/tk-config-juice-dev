class InstanceStatus:
	Unknown = 0 # Unknown status           
	Pending = 1 # Pending status           
	Running = 2 # Running status           
	Rebooting = 3 # Rebboting status           
	Stopping = 4 # Stopping status           
	Stopped = 5 # Stopped status           
	Terminated = 6 # Terminated status           


from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Cloud import CloudInstance
class CloudInstance(IEquatable< CloudInstance >):
	"""
	 A simple class used to describe a Cloud Instance
	"""

	@property
	def GroupName(self) -> Text:
		"""
		
The Name of the Group to which this instance belongs         
		"""
	@GroupName.setter
	def GroupName(self, value: Text): ...


	@property
	def HardwareID(self) -> Text:
		"""
		
The HardwareType on which this VM was created         
		"""
	@HardwareID.setter
	def HardwareID(self, value: Text): ...


	@property
	def Hostname(self) -> Text:
		"""
		
This VM's hostname         
		"""
	@Hostname.setter
	def Hostname(self, value: Text): ...


	@property
	def ID(self) -> Text:
		"""
		
This VM's unique ID         
		"""
	@ID.setter
	def ID(self, value: Text): ...


	@property
	def ImageID(self) -> Text:
		"""
		
The OSImage that was used to create this VM         
		"""
	@ImageID.setter
	def ImageID(self, value: Text): ...


	@property
	def Name(self) -> Text:
		"""
		
The human-readable name of this VM instance         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def PrivateIP(self) -> Text:
		"""
		
This VM's private IP         
		"""
	@PrivateIP.setter
	def PrivateIP(self, value: Text): ...


	@property
	def Provider(self) -> Text:
		"""
		
The Name of the Provider that is hosting this instance         
		"""
	@Provider.setter
	def Provider(self, value: Text): ...


	@property
	def PublicIP(self) -> Text:
		"""
		
This VM's public IP         
		"""
	@PublicIP.setter
	def PublicIP(self, value: Text): ...


	@property
	def RegionName(self) -> Text:
		"""
		
The Name of the Region to which this instance belongs         
		"""
	@RegionName.setter
	def RegionName(self, value: Text): ...


	@property
	def Status(self) -> InstanceStatus:
		"""
		
This VM's status         
		"""
	@Status.setter
	def Status(self, value: InstanceStatus): ...


	@property
	def Zone(self) -> Text:
		"""
		
The Physical region the instances resides in. (From the provider)         
		"""
	@Zone.setter
	def Zone(self, value: Text): ...

	def CompareTo(self, obj: object) -> int:
		"""
		Compares two 

		:param object obj: 
		:return: 
		"""

	def Equals(self, obj: object) -> overridebool:
		"""
		Override of the base object 'Equals' function; calls generic version if applicable. 

		:param object obj: 
		:return: 
		"""

	def Equals(self, other: CloudInstance) -> bool:
		"""
		Equality comparer 

		:param CloudInstance other: The other instance to compare this one to
		:return: True if their properties match up, false otherwise
		"""

	def GetHashCode(self, ) -> overrideint:
		"""
		Override of the base object hash code; returns the hash of the Instance ID 

		
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Cloud import OSImage
from Deadline.Cloud import CloudInstance
from Deadline.Cloud import ImageSource
from Deadline.Cloud import HardwareType
class CloudPluginWrapper:
	"""
	 The managed wrapper for the python Cloud Plugins. The CloudPluginWrapper class uses a builder pattern to construct
	objects. In order for CloudPluginWrapper objects to function properly, they must set the PluginConfig,
	DataController, and CloudPluginName, then initialze the plugin secret retriever.
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

from typing import Iterable
from typing import Text
from typing import Dict
class GroupMapping:
	"""
	 Used to represent the mapping between a Deadline Group and a Cloud OSImage and HardwareType
	"""

	@property
	def Cost(self) -> float:
		"""
		
The cost that this particular mapping incurs. The precise meaning of this value is provider-specific, but should represent the same units as 'CostLimit' of the CloudRegion         
		"""
	@Cost.setter
	def Cost(self, value: float): ...


	@property
	def Enabled(self) -> bool:
		"""
		
Whether or not this particular mapping is currently enabled         
		"""
	@Enabled.setter
	def Enabled(self, value: bool): ...


	@property
	def Group(self) -> Text:
		"""
		
The name of the Deadline Group that is part of this mapping         
		"""
	@Group.setter
	def Group(self, value: Text): ...


	@property
	def HardwareTypeID(self) -> Text:
		"""
		
The ID of the HardwareType that is part of this mapping         
		"""
	@HardwareTypeID.setter
	def HardwareTypeID(self, value: Text): ...


	@property
	def HardwareTypeName(self) -> Text:
		"""
		
The human-readable name for the Hardware         
		"""
	@HardwareTypeName.setter
	def HardwareTypeName(self, value: Text): ...


	@property
	def OSImageID(self) -> Text:
		"""
		
The ID of the OSImage that is part of this mapping         
		"""
	@OSImageID.setter
	def OSImageID(self, value: Text): ...


	@property
	def OSImageName(self) -> Text:
		"""
		
The human-readable name for the OS Image         
		"""
	@OSImageName.setter
	def OSImageName(self, value: Text): ...


	@property
	def Pools(self) -> Iterable[Text]:
		"""
		
Pools to start the instances in.         
		"""
	@Pools.setter
	def Pools(self, value: Iterable[Text]): ...


	@property
	def Region(self) -> Text:
		"""
		
Known active instance IDs for this mapping         
		"""
	@Region.setter
	def Region(self, value: Text): ...


	@property
	def m_hardwareName(self) -> Text:
		"""
		
        
		"""
	@m_hardwareName.setter
	def m_hardwareName(self, value: Text): ...


	@property
	def m_imageName(self) -> Text:
		"""
		
        
		"""
	@m_imageName.setter
	def m_imageName(self, value: Text): ...


	@property
	def m_pools(self) -> Iterable[Text]:
		"""
		
        
		"""
	@m_pools.setter
	def m_pools(self, value: Iterable[Text]): ...


	@property
	def m_regionName(self) -> Text:
		"""
		
        
		"""
	@m_regionName.setter
	def m_regionName(self, value: Text): ...

	def __init__(self, ):
		"""
		Default constructor, required for DB Serialization 

		
		:return: 
		"""

	def __init__(self, region: Text, group: Text, hardwareID: Text, imageID: Text):
		"""
		Constructor 

		:param Text region: The region the mapping belongs to
		:param Text group: The 
		:param Text hardwareID: The ID of the 
		:param Text imageID: The ID of the 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class HardwareType:
	"""
	 A class used by Cloud code to describe hardware
	"""

	@property
	def DiskMB(self) -> int:
		"""
		
The Size of the Disk attached to this hardware type (in MB)         
		"""
	@DiskMB.setter
	def DiskMB(self, value: int): ...


	@property
	def ID(self) -> Text:
		"""
		
An ID used by Cloud plugins to identify this specific hardware type         
		"""
	@ID.setter
	def ID(self, value: Text): ...


	@property
	def Name(self) -> Text:
		"""
		
Human-readable name of the Hardware type         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def RamMB(self) -> int:
		"""
		
The amount of RAM available, in MB         
		"""
	@RamMB.setter
	def RamMB(self, value: int): ...


	@property
	def VCPUs(self) -> int:
		"""
		
The number of virtual CPU cores         
		"""
	@VCPUs.setter
	def VCPUs(self, value: int): ...

from typing import Iterable
from typing import Text
from typing import Dict
class ImageSource:
	"""
	 Object that holds information about the sources of images. Used for creating images.
	"""

	@property
	def ID(self) -> Text:
		"""
		
The id of the source object.         
		"""
	@ID.setter
	def ID(self, value: Text): ...


	@property
	def Name(self) -> Text:
		"""
		
the human readable name of the source object.         
		"""
	@Name.setter
	def Name(self, value: Text): ...

from typing import Iterable
from typing import Text
from typing import Dict
class OSImage:
	"""
	 A class used to describe an OS Image, in a provider-agnostic way
	"""

	@property
	def Bitness(self) -> int:
		"""
		
The bitness of this image         
		"""
	@Bitness.setter
	def Bitness(self, value: int): ...


	@property
	def Description(self) -> Text:
		"""
		
Human-readable description of this OS Image         
		"""
	@Description.setter
	def Description(self, value: Text): ...


	@property
	def ID(self) -> Text:
		"""
		
The ID used to uniquely identify this OS Image         
		"""
	@ID.setter
	def ID(self, value: Text): ...


	@property
	def Platform(self) -> Environment2.OS:
		"""
		
The type of OS contained in this Image (ie, Windows, Linux)         
		"""
	@Platform.setter
	def Platform(self, value: Environment2.OS): ...

