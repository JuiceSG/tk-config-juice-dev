from typing import Iterable
from typing import Text
from typing import Dict
class MachineInfo(LastWriteDocument):
	"""
	 Contains information about the machine that a Worker or pulse is running on.
	"""

	@property
	def MachineArchitecture(self) -> Text:
		"""
		
The machine's architecture.         
		"""


	@property
	def MachineCPUs(self) -> int:
		"""
		
The number of CPUs the machine has.         
		"""


	@property
	def MachineCPUUsage(self) -> int:
		"""
		
The machine's CPU usage.         
		"""


	@property
	def MachineDiskSpace(self) -> long:
		"""
		
The free disk space on the machine, in bytes.         
		"""


	@property
	def MachineFreeMemory(self) -> long:
		"""
		
The machine's available RAM.         
		"""


	@property
	def MachineIPAddress(self) -> Text:
		"""
		
The machine's IP address.         
		"""


	@property
	def MachineMACAddress(self) -> Text:
		"""
		
The machine's MAC address.         
		"""


	@property
	def MachineMemory(self) -> long:
		"""
		
The machine's total RAM.         
		"""


	@property
	def MachineOperatingSystem(self) -> Text:
		"""
		
The machine's operating system.         
		"""


	@property
	def MachineProcessorSpeed(self) -> long:
		"""
		
The machine's processor speed, in Hz.         
		"""


	@property
	def MachineRealName(self) -> Text:
		"""
		
The machine's host name.         
		"""


	@property
	def MachineUserName(self) -> Text:
		"""
		
The machine's user name.         
		"""


	@property
	def MachineVideoCard(self) -> Text:
		"""
		
The name of the machine's video card.         
		"""

