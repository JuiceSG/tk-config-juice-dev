from typing import Iterable
from typing import Text
from typing import Dict
class UserInfo(BaseDocument):
	"""
	 A user.
	"""

	@property
	def RunAsUserPassword(self) -> Text:
		"""
		
When rendering the job as the job's user, this is the user's password (Windows only).         
		"""
	@RunAsUserPassword.setter
	def RunAsUserPassword(self, value: Text): ...


	@property
	def UserEmailAddress(self) -> Text:
		"""
		
The user's email address.         
		"""
	@UserEmailAddress.setter
	def UserEmailAddress(self, value: Text): ...


	@property
	def UserEmailNotification(self) -> bool:
		"""
		
If the user will receive email notifications for their job.         
		"""
	@UserEmailNotification.setter
	def UserEmailNotification(self, value: bool): ...


	@property
	def UserJobCompleted(self) -> bool:
		"""
		
Whether or not to receive Job Completed notifications.         
		"""
	@UserJobCompleted.setter
	def UserJobCompleted(self, value: bool): ...


	@property
	def UserJobFailed(self) -> bool:
		"""
		
Whether or not to receive Job Failed notifications.         
		"""
	@UserJobFailed.setter
	def UserJobFailed(self, value: bool): ...


	@property
	def UserJobTaskTimeout(self) -> bool:
		"""
		
Whether or not to receive Job Task Timeout notifications.         
		"""
	@UserJobTaskTimeout.setter
	def UserJobTaskTimeout(self, value: bool): ...


	@property
	def UserJobWarning(self) -> bool:
		"""
		
Whether or not to receive Job Warning notifications.         
		"""
	@UserJobWarning.setter
	def UserJobWarning(self, value: bool): ...


	@property
	def UserMachineName(self) -> Text:
		"""
		
The user's machine. This is used when sending popup messages.         
		"""
	@UserMachineName.setter
	def UserMachineName(self, value: Text): ...


	@property
	def UserPopupNotification(self) -> bool:
		"""
		
If the user will receive popup notifications for their job.         
		"""
	@UserPopupNotification.setter
	def UserPopupNotification(self, value: bool): ...

