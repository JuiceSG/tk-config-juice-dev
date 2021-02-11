class PulseStatus:
	Unknown = 0 # The state is unknown.           
	Running = 1 # Pulse is running.           
	Offline = 2 # Pulse is not running.           
	Stalled = 4 # Pulse has hung or crashed.           


from typing import Iterable
from typing import Text
from typing import Dict
class PulseInfo(Deadline.MachineInfo):
	"""
	 Information about the current state of pulse.
	"""

	@property
	def PulseName(self) -> Text:
		"""
		
Pulse's name (in the context of Deadline).         
		"""
	@PulseName.setter
	def PulseName(self, value: Text): ...


	@property
	def PulsePort(self) -> int:
		"""
		
The port that Pulse is listening on.         
		"""


	@property
	def PulseRegion(self) -> Text:
		"""
		
The Region the Pulse is in.         
		"""
	@PulseRegion.setter
	def PulseRegion(self, value: Text): ...


	@property
	def PulseRunningTime(self) -> int:
		"""
		
Pulse's current running time, in seconds.         
		"""


	@property
	def PulseState(self) -> Text:
		"""
		
The current state of Pulse.         
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Pulses import PulseSettings
from Deadline.Pulses import PulseInfo
class PulseInfoSettings(IComparable):
	"""
	 A wrapper around pulse's info and settings objects.
	"""

	@property
	def Info(self) -> PulseInfo:
		"""
		
The PulseInfo for this Pulse.         
		"""


	@property
	def PulseName(self) -> Text:
		"""
		
The name of the pulse in question.         
		"""


	@property
	def Settings(self) -> PulseSettings:
		"""
		
The PulseSettings for this Pulse.         
		"""

	def CompareTo(self, obj: object) -> int:
		"""
		Compare 2 pulse info settings by comparing their info then Settings 

		:param object obj: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class PulseSettings(LastWriteDocument):
	"""
	 Pulse settings.
	"""

	@property
	def PulseHostMachineIPAddressOverride(self) -> Text:
		"""
		
If non-empty, this host name or IP address will be used for remote communication with pulse.         
		"""
	@PulseHostMachineIPAddressOverride.setter
	def PulseHostMachineIPAddressOverride(self, value: Text): ...


	@property
	def PulseIsPrimary(self) -> bool:
		"""
		
Is this Pulse the Primary Pulse?         
		"""
	@PulseIsPrimary.setter
	def PulseIsPrimary(self, value: bool): ...


	@property
	def PulseListeningPort(self) -> int:
		"""
		
The port to use listen on if PulseOverridePort is enabled.         
		"""
	@PulseListeningPort.setter
	def PulseListeningPort(self, value: int): ...


	@property
	def PulseMacAddressOverride(self) -> Text:
		"""
		
If non-empty, this is used to override the MAC address for pulse.         
		"""
	@PulseMacAddressOverride.setter
	def PulseMacAddressOverride(self, value: Text): ...


	@property
	def PulseName(self) -> Text:
		"""
		
The Pulse name.         
		"""
	@PulseName.setter
	def PulseName(self, value: Text): ...


	@property
	def PulseOverrideListeningPort(self) -> bool:
		"""
		
If pulse should listen on a specific port.         
		"""
	@PulseOverrideListeningPort.setter
	def PulseOverrideListeningPort(self, value: bool): ...


	@property
	def PulseOverridePort(self) -> bool:
		"""
		
If pulse should use a specific port.         
		"""
	@PulseOverridePort.setter
	def PulseOverridePort(self, value: bool): ...


	@property
	def PulsePort(self) -> int:
		"""
		
The port to use if PulseOverridePort is enabled.         
		"""
	@PulsePort.setter
	def PulsePort(self, value: int): ...

	def CompareTo(self, obj: object) -> int:
		"""
		Compare 2 pulse settings by Name 

		:param object obj: 
		:return: 
		"""

