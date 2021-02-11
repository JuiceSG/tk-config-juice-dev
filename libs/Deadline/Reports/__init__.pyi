from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Reports import Report
class JobReportCollection(BaseDocument):
	"""
	 A collection of job reports.
	"""
	def GetAllReports(self, ) -> Iterable[Report]:
		"""
		Returns all of the job's reports. 

		
		:return: 
		"""

	def GetAllTaskReports(self, taskID: int) -> Iterable[Report]:
		"""
		Gets the reports for the given task. 

		:param int taskID: 
		:return: 
		"""

	def GetErrorReports(self, ) -> Iterable[Report]:
		"""
		Returns all of the job's error reports. 

		
		:return: 
		"""

	def GetHistoryEntries(self, ) -> Iterable[HistoryEntry]:
		"""
		Returns an array of history entries. 

		
		:return: 
		"""

	def GetLogReports(self, ) -> Iterable[Report]:
		"""
		Returns all of the job's log reports. 

		
		:return: 
		"""

	def GetRequeueReports(self, ) -> Iterable[Report]:
		"""
		Returns all of the job's requeue reports. 

		
		:return: 
		"""

	def GetTaskErrorReports(self, taskID: int) -> Iterable[Report]:
		"""
		Gets the error reports for the given task. 

		:param int taskID: 
		:return: 
		"""

	def GetTaskLogReports(self, taskID: int) -> Iterable[Report]:
		"""
		Gets the log reports for the given task. 

		:param int taskID: 
		:return: 
		"""

	def GetTaskRequeueReports(self, taskID: int) -> Iterable[Report]:
		"""
		Gets the requeue reports for the given task. 

		:param int taskID: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class Report(LastWriteDocument):
	"""
	 A report.
	"""

	@property
	def ReportAverageCpu(self) -> int:
		"""
		
The average CPU usage for the task.         
		"""


	@property
	def ReportAverageRam(self) -> long:
		"""
		
The average RAM usage for the task.         
		"""


	@property
	def ReportDateTimeOf(self) -> DateTime:
		"""
		
The date/time the report was created.         
		"""


	@property
	def ReportError(self) -> Text:
		"""
		
If an error occurred while saving the log for this report, it is stored here.         
		"""


	@property
	def ReportFrameString(self) -> Text:
		"""
		
The frame string of the task that the report was created for.         
		"""


	@property
	def ReportID(self) -> Text:
		"""
		
The report ID.         
		"""


	@property
	def ReportJobName(self) -> Text:
		"""
		
The name of the job the report was created for.         
		"""


	@property
	def ReportJobUserName(self) -> Text:
		"""
		
The job's user.         
		"""


	@property
	def ReportMessage(self) -> Text:
		"""
		
The report message.         
		"""


	@property
	def ReportPeakCpu(self) -> int:
		"""
		
The peak CPU usage for the task.         
		"""


	@property
	def ReportPeakRam(self) -> long:
		"""
		
The peak RAM usage for the task.         
		"""


	@property
	def ReportPluginName(self) -> Text:
		"""
		
The plugin the job is using.         
		"""


	@property
	def ReportSlaveName(self) -> Text:
		"""
		
The Worker that created the report.         
		"""


	@property
	def ReportTaskID(self) -> int:
		"""
		
The ID of the task the report was created for.         
		"""


	@property
	def ReportTaskSecondsElapsed(self) -> int:
		"""
		
The rendering time in seconds before the report was created.         
		"""


	@property
	def ReportTaskTimeElapsed(self) -> TimeSpan:
		"""
		
The rendering time before the report was created.         
		"""


	@property
	def ReportTypeOf(self) -> Text:
		"""
		
The type of report this is.         
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Reports import Report
class SlaveReportCollection(BaseDocument):
	"""
	 A collection of Worker reports.
	"""
	def GetErrorReports(self, ) -> Iterable[Report]:
		"""
		Returns all of the Worker's error reports. 

		
		:return: 
		"""

	def GetLogReports(self, ) -> Iterable[Report]:
		"""
		Gets the log reports. 

		
		:return: 
		"""

	def GetSlaveReports(self, ) -> Iterable[Report]:
		"""
		Gets all the Worker reports. 

		
		:return: 
		"""

