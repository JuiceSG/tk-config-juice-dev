from typing import Iterable
from typing import Text
from typing import Dict
class LimitGroup(LastWriteDocument):
	"""
	 A limit group.
	"""

	@property
	def LimitCurrentHolders(self) -> Iterable[Text]:
		"""
		
The list of current stub holders.         
		"""


	@property
	def LimitGroupExcludedSlaves(self) -> Iterable[Text]:
		"""
		
The Workers that do not need to aquire this limit group to render.         
		"""


	@property
	def LimitGroupInOverage(self) -> int:
		"""
		
The number of limit group stubs in use that are in overage.         
		"""


	@property
	def LimitGroupLimit(self) -> int:
		"""
		
The limit, or the number of stubs that can be obtained simultaneously.         
		"""
	@LimitGroupLimit.setter
	def LimitGroupLimit(self, value: int): ...


	@property
	def LimitGroupListedSlaves(self) -> Iterable[Text]:
		"""
		
The listed Workers for this limit group. If LimitGroupWhitelistFlag is True, this is an allow list, otherwise this is a deny list.         
		"""


	@property
	def LimitGroupName(self) -> Text:
		"""
		
The limit group name.         
		"""


	@property
	def LimitGroupOverage(self) -> int:
		"""
		
The soft cap.         
		"""
	@LimitGroupOverage.setter
	def LimitGroupOverage(self, value: int): ...


	@property
	def LimitGroupReleasePercentage(self) -> float:
		"""
		
The task progress at which this limit group will be released.         
		"""
	@LimitGroupReleasePercentage.setter
	def LimitGroupReleasePercentage(self, value: float): ...


	@property
	def LimitGroupThreePLEName(self) -> Text:
		"""
		
The name of the third-party licensing product assigned to this Limit.         
		"""


	@property
	def LimitGroupThreePLPerCore(self) -> bool:
		"""
		
This value is true if the product assigned for third-party licensing is licensed per core.         
		"""


	@property
	def LimitGroupUnlimitedLimit(self) -> bool:
		"""
		
Whether the limit is unlimited (infinite number of stubs can be checked out).         
		"""
	@LimitGroupUnlimitedLimit.setter
	def LimitGroupUnlimitedLimit(self, value: bool): ...


	@property
	def LimitGroupUseThirdPartyUBL(self) -> bool:
		"""
		
If using third-party licensing for this Limit is enabled or not. If enabled, the licensing environment for the Worker will be modified when the soft cap is exceeded.         
		"""
	@LimitGroupUseThirdPartyUBL.setter
	def LimitGroupUseThirdPartyUBL(self, value: bool): ...


	@property
	def LimitGroupWhitelistFlag(self) -> bool:
		"""
		
Whether or not the list of Workers is an allow list (as opposed to a deny list).         
		"""
	@LimitGroupWhitelistFlag.setter
	def LimitGroupWhitelistFlag(self, value: bool): ...


	@property
	def LimitInUse(self) -> int:
		"""
		
The number of limit group stubs currently in use.         
		"""


	@property
	def LimitStubLevel(self) -> StubLevel:
		"""
		
The type of stub holders this limit group has.         
		"""

	def SetLimitGroupExcludedSlaves(self, slaveNames: object):
		"""
		Sets the Workers that do not need to aquire this limit group to render. 

		:param object slaveNames: The Worker names. This should be a list of strings.
		:return: 
		"""

	def SetLimitGroupListedSlaves(self, slaveNames: object):
		"""
		Sets the listed Workers for this limit group. 

		:param object slaveNames: The Worker names. This should be a list of strings.
		:return: 
		"""

	def SetLimitGroupThreePLEName(self, newName: Text) -> bool:
		"""
		Sets which third-party licensing product should be assigned to this Limit. The product must not already be assigned to another Limit. 

		:param Text newName: The product name to be assigned to the Limit.
		:return: True if the product was successfully set to the Limit.
		"""

