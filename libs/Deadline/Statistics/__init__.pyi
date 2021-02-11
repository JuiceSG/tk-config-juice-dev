from typing import Iterable
from typing import Text
from typing import Dict
class JobEntry(BaseDocument):
	"""
	 Holds job statistics.
	"""

	@property
	def AuxiliaryFileNames(self) -> int:
		"""
		
The number of auxiliary files.         
		"""
	@AuxiliaryFileNames.setter
	def AuxiliaryFileNames(self, value: int): ...


	@property
	def AverageConcurrentTasks(self) -> int:
		"""
		
The average number of tasks rendering concurrently.         
		"""
	@AverageConcurrentTasks.setter
	def AverageConcurrentTasks(self, value: int): ...


	@property
	def AverageCpuUsage(self) -> long:
		"""
		
The job average cpu usage.         
		"""
	@AverageCpuUsage.setter
	def AverageCpuUsage(self, value: long): ...


	@property
	def AverageFrameRenderTime(self) -> TimeSpan:
		"""
		
The average frame render time.         
		"""
	@AverageFrameRenderTime.setter
	def AverageFrameRenderTime(self, value: TimeSpan): ...


	@property
	def AverageFrameRenderTimeAsString(self) -> Text:
		"""
		
The average frame render time.         
		"""
	@AverageFrameRenderTimeAsString.setter
	def AverageFrameRenderTimeAsString(self, value: Text): ...


	@property
	def AverageFrameStartupTime(self) -> TimeSpan:
		"""
		
The average frame startup time.         
		"""
	@AverageFrameStartupTime.setter
	def AverageFrameStartupTime(self, value: TimeSpan): ...


	@property
	def AverageFrameStartupTimeAsString(self) -> Text:
		"""
		
The average frame startup time.         
		"""
	@AverageFrameStartupTimeAsString.setter
	def AverageFrameStartupTimeAsString(self, value: Text): ...


	@property
	def AverageFrameTime(self) -> TimeSpan:
		"""
		
The average frame time.         
		"""
	@AverageFrameTime.setter
	def AverageFrameTime(self, value: TimeSpan): ...


	@property
	def AverageFrameTimeAsString(self) -> Text:
		"""
		
The average frame time.         
		"""
	@AverageFrameTimeAsString.setter
	def AverageFrameTimeAsString(self, value: Text): ...


	@property
	def AverageImageFileSize(self) -> long:
		"""
		
The average image file size.         
		"""
	@AverageImageFileSize.setter
	def AverageImageFileSize(self, value: long): ...


	@property
	def AverageNormalizedFrameRenderTime(self) -> TimeSpan:
		"""
		
The average frame render time.         
		"""
	@AverageNormalizedFrameRenderTime.setter
	def AverageNormalizedFrameRenderTime(self, value: TimeSpan): ...


	@property
	def AverageNormalizedFrameRenderTimeAsString(self) -> Text:
		"""
		
The average frame render time.         
		"""
	@AverageNormalizedFrameRenderTimeAsString.setter
	def AverageNormalizedFrameRenderTimeAsString(self, value: Text): ...


	@property
	def AverageNormalizedTaskRenderTime(self) -> TimeSpan:
		"""
		
The job average task render time.         
		"""
	@AverageNormalizedTaskRenderTime.setter
	def AverageNormalizedTaskRenderTime(self, value: TimeSpan): ...


	@property
	def AverageNormalizedTaskRenderTimeAsString(self) -> Text:
		"""
		
The job average task render time.         
		"""
	@AverageNormalizedTaskRenderTimeAsString.setter
	def AverageNormalizedTaskRenderTimeAsString(self, value: Text): ...


	@property
	def AverageRamUsage(self) -> long:
		"""
		
The job average ram usage.         
		"""
	@AverageRamUsage.setter
	def AverageRamUsage(self, value: long): ...


	@property
	def AverageSwapUsage(self) -> long:
		"""
		
The job average swap usage.         
		"""
	@AverageSwapUsage.setter
	def AverageSwapUsage(self, value: long): ...


	@property
	def AverageTaskRenderTime(self) -> TimeSpan:
		"""
		
The job average task render time.         
		"""
	@AverageTaskRenderTime.setter
	def AverageTaskRenderTime(self, value: TimeSpan): ...


	@property
	def AverageTaskRenderTimeAsString(self) -> Text:
		"""
		
The job average task render time.         
		"""
	@AverageTaskRenderTimeAsString.setter
	def AverageTaskRenderTimeAsString(self, value: Text): ...


	@property
	def AverageTaskStartupTime(self) -> TimeSpan:
		"""
		
The job average task render time.         
		"""
	@AverageTaskStartupTime.setter
	def AverageTaskStartupTime(self, value: TimeSpan): ...


	@property
	def AverageTaskStartupTimeAsString(self) -> Text:
		"""
		
The job average task render time.         
		"""
	@AverageTaskStartupTimeAsString.setter
	def AverageTaskStartupTimeAsString(self, value: Text): ...


	@property
	def AverageTaskTime(self) -> TimeSpan:
		"""
		
The job average task time.         
		"""
	@AverageTaskTime.setter
	def AverageTaskTime(self, value: TimeSpan): ...


	@property
	def AverageTaskTimeAsString(self) -> Text:
		"""
		
The job average task time.         
		"""
	@AverageTaskTimeAsString.setter
	def AverageTaskTimeAsString(self, value: Text): ...


	@property
	def Comment(self) -> Text:
		"""
		
The job comment.         
		"""
	@Comment.setter
	def Comment(self, value: Text): ...


	@property
	def CompletedDateTime(self) -> DateTime:
		"""
		
The job completed date/time.         
		"""
	@CompletedDateTime.setter
	def CompletedDateTime(self, value: DateTime): ...


	@property
	def CompletedTaskCount(self) -> int:
		"""
		
The job task count.         
		"""
	@CompletedTaskCount.setter
	def CompletedTaskCount(self, value: int): ...


	@property
	def Department(self) -> Text:
		"""
		
The job department.         
		"""
	@Department.setter
	def Department(self, value: Text): ...


	@property
	def EntryCreationTime(self) -> DateTime:
		"""
		
The job entry creation time.         
		"""
	@EntryCreationTime.setter
	def EntryCreationTime(self, value: DateTime): ...


	@property
	def ErrorReports(self) -> int:
		"""
		
The job error count.         
		"""
	@ErrorReports.setter
	def ErrorReports(self, value: int): ...


	@property
	def ExtraInfo0(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo0.setter
	def ExtraInfo0(self, value: Text): ...


	@property
	def ExtraInfo1(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo1.setter
	def ExtraInfo1(self, value: Text): ...


	@property
	def ExtraInfo2(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo2.setter
	def ExtraInfo2(self, value: Text): ...


	@property
	def ExtraInfo3(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo3.setter
	def ExtraInfo3(self, value: Text): ...


	@property
	def ExtraInfo4(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo4.setter
	def ExtraInfo4(self, value: Text): ...


	@property
	def ExtraInfo5(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo5.setter
	def ExtraInfo5(self, value: Text): ...


	@property
	def ExtraInfo6(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo6.setter
	def ExtraInfo6(self, value: Text): ...


	@property
	def ExtraInfo7(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo7.setter
	def ExtraInfo7(self, value: Text): ...


	@property
	def ExtraInfo8(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo8.setter
	def ExtraInfo8(self, value: Text): ...


	@property
	def ExtraInfo9(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@ExtraInfo9.setter
	def ExtraInfo9(self, value: Text): ...


	@property
	def FrameCount(self) -> int:
		"""
		
The number of frames for this job.         
		"""
	@FrameCount.setter
	def FrameCount(self, value: int): ...


	@property
	def FramesList(self) -> Text:
		"""
		
The job frame list.         
		"""
	@FramesList.setter
	def FramesList(self, value: Text): ...


	@property
	def Group(self) -> Text:
		"""
		
The job group.         
		"""
	@Group.setter
	def Group(self, value: Text): ...


	@property
	def JobID(self) -> Text:
		"""
		
The Job's ID.         
		"""
	@JobID.setter
	def JobID(self, value: Text): ...


	@property
	def MachineLimit(self) -> int:
		"""
		
The job machine limit.         
		"""
	@MachineLimit.setter
	def MachineLimit(self, value: int): ...


	@property
	def MedianCpuUsage(self) -> long:
		"""
		
The job median cpu usage.         
		"""
	@MedianCpuUsage.setter
	def MedianCpuUsage(self, value: long): ...


	@property
	def MedianFrameRenderTime(self) -> TimeSpan:
		"""
		
The medium frame render time.         
		"""
	@MedianFrameRenderTime.setter
	def MedianFrameRenderTime(self, value: TimeSpan): ...


	@property
	def MedianFrameRenderTimeAsString(self) -> Text:
		"""
		
The medium frame render time.         
		"""
	@MedianFrameRenderTimeAsString.setter
	def MedianFrameRenderTimeAsString(self, value: Text): ...


	@property
	def MedianFrameStartupTime(self) -> TimeSpan:
		"""
		
The median frame startup time.         
		"""
	@MedianFrameStartupTime.setter
	def MedianFrameStartupTime(self, value: TimeSpan): ...


	@property
	def MedianFrameStartupTimeAsString(self) -> Text:
		"""
		
The median frame startup time.         
		"""
	@MedianFrameStartupTimeAsString.setter
	def MedianFrameStartupTimeAsString(self, value: Text): ...


	@property
	def MedianFrameTime(self) -> TimeSpan:
		"""
		
The median frame time.         
		"""
	@MedianFrameTime.setter
	def MedianFrameTime(self, value: TimeSpan): ...


	@property
	def MedianFrameTimeAsString(self) -> Text:
		"""
		
The median frame time.         
		"""
	@MedianFrameTimeAsString.setter
	def MedianFrameTimeAsString(self, value: Text): ...


	@property
	def MedianImageFileSize(self) -> long:
		"""
		
The median image file size.         
		"""
	@MedianImageFileSize.setter
	def MedianImageFileSize(self, value: long): ...


	@property
	def MedianNormalizedFrameRenderTime(self) -> TimeSpan:
		"""
		
The average frame render time.         
		"""
	@MedianNormalizedFrameRenderTime.setter
	def MedianNormalizedFrameRenderTime(self, value: TimeSpan): ...


	@property
	def MedianNormalizedFrameRenderTimeAsString(self) -> Text:
		"""
		
The average frame render time.         
		"""
	@MedianNormalizedFrameRenderTimeAsString.setter
	def MedianNormalizedFrameRenderTimeAsString(self, value: Text): ...


	@property
	def MedianNormalizedTaskRenderTime(self) -> TimeSpan:
		"""
		
The job median task startup time.         
		"""
	@MedianNormalizedTaskRenderTime.setter
	def MedianNormalizedTaskRenderTime(self, value: TimeSpan): ...


	@property
	def MedianNormalizedTaskRenderTimeAsString(self) -> Text:
		"""
		
The job median task startup time.         
		"""
	@MedianNormalizedTaskRenderTimeAsString.setter
	def MedianNormalizedTaskRenderTimeAsString(self, value: Text): ...


	@property
	def MedianRamUsage(self) -> long:
		"""
		
The job median ram usage.         
		"""
	@MedianRamUsage.setter
	def MedianRamUsage(self, value: long): ...


	@property
	def MedianSwapUsage(self) -> long:
		"""
		
The job median swap usage.         
		"""
	@MedianSwapUsage.setter
	def MedianSwapUsage(self, value: long): ...


	@property
	def MedianTaskRenderTime(self) -> TimeSpan:
		"""
		
The job median task startup time.         
		"""
	@MedianTaskRenderTime.setter
	def MedianTaskRenderTime(self, value: TimeSpan): ...


	@property
	def MedianTaskRenderTimeAsString(self) -> Text:
		"""
		
The job median task startup time.         
		"""
	@MedianTaskRenderTimeAsString.setter
	def MedianTaskRenderTimeAsString(self, value: Text): ...


	@property
	def MedianTaskStartupTime(self) -> TimeSpan:
		"""
		
The job median task startup time.         
		"""
	@MedianTaskStartupTime.setter
	def MedianTaskStartupTime(self, value: TimeSpan): ...


	@property
	def MedianTaskStartupTimeAsString(self) -> Text:
		"""
		
The job median task startup time.         
		"""
	@MedianTaskStartupTimeAsString.setter
	def MedianTaskStartupTimeAsString(self, value: Text): ...


	@property
	def MedianTaskTime(self) -> TimeSpan:
		"""
		
The job median task time.         
		"""
	@MedianTaskTime.setter
	def MedianTaskTime(self, value: TimeSpan): ...


	@property
	def MedianTaskTimeAsString(self) -> Text:
		"""
		
The job median task time.         
		"""
	@MedianTaskTimeAsString.setter
	def MedianTaskTimeAsString(self, value: Text): ...


	@property
	def Name(self) -> Text:
		"""
		
The job name.         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def PeakCpuUsage(self) -> long:
		"""
		
The job peak cpu usage.         
		"""
	@PeakCpuUsage.setter
	def PeakCpuUsage(self, value: long): ...


	@property
	def PeakRamUsage(self) -> long:
		"""
		
The job peak ram usage.         
		"""
	@PeakRamUsage.setter
	def PeakRamUsage(self, value: long): ...


	@property
	def PeakSwapUsage(self) -> long:
		"""
		
The job peak swap usage.         
		"""
	@PeakSwapUsage.setter
	def PeakSwapUsage(self, value: long): ...


	@property
	def PluginDataFileName(self) -> Text:
		"""
		
The data file name (the first auxiliary file).         
		"""
	@PluginDataFileName.setter
	def PluginDataFileName(self, value: Text): ...


	@property
	def PluginDataFileSize(self) -> long:
		"""
		
The plugin data file size.         
		"""
	@PluginDataFileSize.setter
	def PluginDataFileSize(self, value: long): ...


	@property
	def PluginName(self) -> Text:
		"""
		
The job plugin name.         
		"""
	@PluginName.setter
	def PluginName(self, value: Text): ...


	@property
	def Pool(self) -> Text:
		"""
		
The job pool.         
		"""
	@Pool.setter
	def Pool(self, value: Text): ...


	@property
	def Priority(self) -> int:
		"""
		
The job priority.         
		"""
	@Priority.setter
	def Priority(self, value: int): ...


	@property
	def RenderTime(self) -> TimeSpan:
		"""
		
The job render time.         
		"""
	@RenderTime.setter
	def RenderTime(self, value: TimeSpan): ...


	@property
	def RenderTimeAsString(self) -> Text:
		"""
		
The job render time.         
		"""
	@RenderTimeAsString.setter
	def RenderTimeAsString(self, value: Text): ...


	@property
	def StartedDateTime(self) -> DateTime:
		"""
		
The job started date/time.         
		"""
	@StartedDateTime.setter
	def StartedDateTime(self, value: DateTime): ...


	@property
	def SubmitDateTime(self) -> DateTime:
		"""
		
The job submit date/time.         
		"""
	@SubmitDateTime.setter
	def SubmitDateTime(self, value: DateTime): ...


	@property
	def SubmitMachineName(self) -> Text:
		"""
		
The machine the job was submitted from.         
		"""
	@SubmitMachineName.setter
	def SubmitMachineName(self, value: Text): ...


	@property
	def TaskCount(self) -> int:
		"""
		
The job task count.         
		"""
	@TaskCount.setter
	def TaskCount(self, value: int): ...


	@property
	def TotalCpuClocks(self) -> long:
		"""
		
The total cpu clocks that could have been utilized.         
		"""
	@TotalCpuClocks.setter
	def TotalCpuClocks(self, value: long): ...


	@property
	def TotalImageFileSize(self) -> long:
		"""
		
The total image file size.         
		"""
	@TotalImageFileSize.setter
	def TotalImageFileSize(self, value: long): ...


	@property
	def TotalNormalizedTaskRenderTime(self) -> TimeSpan:
		"""
		
The job total task render time.         
		"""
	@TotalNormalizedTaskRenderTime.setter
	def TotalNormalizedTaskRenderTime(self, value: TimeSpan): ...


	@property
	def TotalNormalizedTaskRenderTimeAsString(self) -> Text:
		"""
		
The job total task render time.         
		"""
	@TotalNormalizedTaskRenderTimeAsString.setter
	def TotalNormalizedTaskRenderTimeAsString(self, value: Text): ...


	@property
	def TotalTaskRenderTime(self) -> TimeSpan:
		"""
		
The job total task render time.         
		"""
	@TotalTaskRenderTime.setter
	def TotalTaskRenderTime(self, value: TimeSpan): ...


	@property
	def TotalTaskRenderTimeAsString(self) -> Text:
		"""
		
The job total task render time.         
		"""
	@TotalTaskRenderTimeAsString.setter
	def TotalTaskRenderTimeAsString(self, value: Text): ...


	@property
	def TotalTaskStartupTime(self) -> TimeSpan:
		"""
		
The job total task render time.         
		"""
	@TotalTaskStartupTime.setter
	def TotalTaskStartupTime(self, value: TimeSpan): ...


	@property
	def TotalTaskStartupTimeAsString(self) -> Text:
		"""
		
The job total task render time.         
		"""
	@TotalTaskStartupTimeAsString.setter
	def TotalTaskStartupTimeAsString(self, value: Text): ...


	@property
	def TotalTaskTime(self) -> TimeSpan:
		"""
		
The job total task time.         
		"""
	@TotalTaskTime.setter
	def TotalTaskTime(self, value: TimeSpan): ...


	@property
	def TotalTaskTimeAsString(self) -> Text:
		"""
		
The job total task time.         
		"""
	@TotalTaskTimeAsString.setter
	def TotalTaskTimeAsString(self, value: Text): ...


	@property
	def UsedCpuClocks(self) -> long:
		"""
		
The cpu clocks used.         
		"""
	@UsedCpuClocks.setter
	def UsedCpuClocks(self, value: long): ...


	@property
	def UserName(self) -> Text:
		"""
		
The job user name.         
		"""
	@UserName.setter
	def UserName(self, value: Text): ...


	@property
	def WastedErrorTime(self) -> TimeSpan:
		"""
		
The wasted time due to errors.         
		"""
	@WastedErrorTime.setter
	def WastedErrorTime(self, value: TimeSpan): ...


	@property
	def WastedErrorTimeAsString(self) -> Text:
		"""
		
The wasted time due to errors.         
		"""
	@WastedErrorTimeAsString.setter
	def WastedErrorTimeAsString(self, value: Text): ...


	@property
	def WastedRequeueTime(self) -> TimeSpan:
		"""
		
The wasted time due to requeues.         
		"""
	@WastedRequeueTime.setter
	def WastedRequeueTime(self, value: TimeSpan): ...


	@property
	def WastedRequeueTimeAsString(self) -> Text:
		"""
		
The wasted time due to requeues.         
		"""
	@WastedRequeueTimeAsString.setter
	def WastedRequeueTimeAsString(self, value: Text): ...


	@property
	def m_auxiliaryFileNames(self) -> int:
		"""
		
        
		"""
	@m_auxiliaryFileNames.setter
	def m_auxiliaryFileNames(self, value: int): ...


	@property
	def m_averageConcurrentTasks(self) -> int:
		"""
		
        
		"""
	@m_averageConcurrentTasks.setter
	def m_averageConcurrentTasks(self, value: int): ...


	@property
	def m_averageCpuUsage(self) -> long:
		"""
		
        
		"""
	@m_averageCpuUsage.setter
	def m_averageCpuUsage(self, value: long): ...


	@property
	def m_averageFrameRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageFrameRenderTime.setter
	def m_averageFrameRenderTime(self, value: TimeSpan): ...


	@property
	def m_averageFrameStartupTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageFrameStartupTime.setter
	def m_averageFrameStartupTime(self, value: TimeSpan): ...


	@property
	def m_averageFrameTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageFrameTime.setter
	def m_averageFrameTime(self, value: TimeSpan): ...


	@property
	def m_averageImageFileSize(self) -> long:
		"""
		
        
		"""
	@m_averageImageFileSize.setter
	def m_averageImageFileSize(self, value: long): ...


	@property
	def m_averageNormalizedFrameRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageNormalizedFrameRenderTime.setter
	def m_averageNormalizedFrameRenderTime(self, value: TimeSpan): ...


	@property
	def m_averageNormalizedTaskRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageNormalizedTaskRenderTime.setter
	def m_averageNormalizedTaskRenderTime(self, value: TimeSpan): ...


	@property
	def m_averageRamUsage(self) -> long:
		"""
		
        
		"""
	@m_averageRamUsage.setter
	def m_averageRamUsage(self, value: long): ...


	@property
	def m_averageSwapUsage(self) -> long:
		"""
		
        
		"""
	@m_averageSwapUsage.setter
	def m_averageSwapUsage(self, value: long): ...


	@property
	def m_averageTaskRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageTaskRenderTime.setter
	def m_averageTaskRenderTime(self, value: TimeSpan): ...


	@property
	def m_averageTaskStartupTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageTaskStartupTime.setter
	def m_averageTaskStartupTime(self, value: TimeSpan): ...


	@property
	def m_averageTaskTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_averageTaskTime.setter
	def m_averageTaskTime(self, value: TimeSpan): ...


	@property
	def m_comment(self) -> Text:
		"""
		
        
		"""
	@m_comment.setter
	def m_comment(self, value: Text): ...


	@property
	def m_completedDateTime(self) -> DateTime:
		"""
		
        
		"""
	@m_completedDateTime.setter
	def m_completedDateTime(self, value: DateTime): ...


	@property
	def m_completedTaskCount(self) -> int:
		"""
		
        
		"""
	@m_completedTaskCount.setter
	def m_completedTaskCount(self, value: int): ...


	@property
	def m_department(self) -> Text:
		"""
		
        
		"""
	@m_department.setter
	def m_department(self, value: Text): ...


	@property
	def m_entryCreationTime(self) -> DateTime:
		"""
		
        
		"""
	@m_entryCreationTime.setter
	def m_entryCreationTime(self, value: DateTime): ...


	@property
	def m_errorReports(self) -> int:
		"""
		
        
		"""
	@m_errorReports.setter
	def m_errorReports(self, value: int): ...


	@property
	def m_extraInfo0(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo0.setter
	def m_extraInfo0(self, value: Text): ...


	@property
	def m_extraInfo1(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo1.setter
	def m_extraInfo1(self, value: Text): ...


	@property
	def m_extraInfo2(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo2.setter
	def m_extraInfo2(self, value: Text): ...


	@property
	def m_extraInfo3(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo3.setter
	def m_extraInfo3(self, value: Text): ...


	@property
	def m_extraInfo4(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo4.setter
	def m_extraInfo4(self, value: Text): ...


	@property
	def m_extraInfo5(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo5.setter
	def m_extraInfo5(self, value: Text): ...


	@property
	def m_extraInfo6(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo6.setter
	def m_extraInfo6(self, value: Text): ...


	@property
	def m_extraInfo7(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo7.setter
	def m_extraInfo7(self, value: Text): ...


	@property
	def m_extraInfo8(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo8.setter
	def m_extraInfo8(self, value: Text): ...


	@property
	def m_extraInfo9(self) -> Text:
		"""
		
        
		"""
	@m_extraInfo9.setter
	def m_extraInfo9(self, value: Text): ...


	@property
	def m_frameCount(self) -> int:
		"""
		
        
		"""
	@m_frameCount.setter
	def m_frameCount(self, value: int): ...


	@property
	def m_framesList(self) -> Text:
		"""
		
        
		"""
	@m_framesList.setter
	def m_framesList(self, value: Text): ...


	@property
	def m_group(self) -> Text:
		"""
		
        
		"""
	@m_group.setter
	def m_group(self, value: Text): ...


	@property
	def m_jobID(self) -> Text:
		"""
		
        
		"""
	@m_jobID.setter
	def m_jobID(self, value: Text): ...


	@property
	def m_machineLimit(self) -> int:
		"""
		
        
		"""
	@m_machineLimit.setter
	def m_machineLimit(self, value: int): ...


	@property
	def m_medianCpuUsage(self) -> long:
		"""
		
        
		"""
	@m_medianCpuUsage.setter
	def m_medianCpuUsage(self, value: long): ...


	@property
	def m_medianFrameRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianFrameRenderTime.setter
	def m_medianFrameRenderTime(self, value: TimeSpan): ...


	@property
	def m_medianFrameStartupTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianFrameStartupTime.setter
	def m_medianFrameStartupTime(self, value: TimeSpan): ...


	@property
	def m_medianFrameTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianFrameTime.setter
	def m_medianFrameTime(self, value: TimeSpan): ...


	@property
	def m_medianImageFileSize(self) -> long:
		"""
		
        
		"""
	@m_medianImageFileSize.setter
	def m_medianImageFileSize(self, value: long): ...


	@property
	def m_medianNormalizedFrameRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianNormalizedFrameRenderTime.setter
	def m_medianNormalizedFrameRenderTime(self, value: TimeSpan): ...


	@property
	def m_medianNormalizedTaskRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianNormalizedTaskRenderTime.setter
	def m_medianNormalizedTaskRenderTime(self, value: TimeSpan): ...


	@property
	def m_medianRamUsage(self) -> long:
		"""
		
        
		"""
	@m_medianRamUsage.setter
	def m_medianRamUsage(self, value: long): ...


	@property
	def m_medianSwapUsage(self) -> long:
		"""
		
        
		"""
	@m_medianSwapUsage.setter
	def m_medianSwapUsage(self, value: long): ...


	@property
	def m_medianTaskRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianTaskRenderTime.setter
	def m_medianTaskRenderTime(self, value: TimeSpan): ...


	@property
	def m_medianTaskStartupTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianTaskStartupTime.setter
	def m_medianTaskStartupTime(self, value: TimeSpan): ...


	@property
	def m_medianTaskTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_medianTaskTime.setter
	def m_medianTaskTime(self, value: TimeSpan): ...


	@property
	def m_name(self) -> Text:
		"""
		
        
		"""
	@m_name.setter
	def m_name(self, value: Text): ...


	@property
	def m_peakCpuUsage(self) -> long:
		"""
		
        
		"""
	@m_peakCpuUsage.setter
	def m_peakCpuUsage(self, value: long): ...


	@property
	def m_peakRamUsage(self) -> long:
		"""
		
        
		"""
	@m_peakRamUsage.setter
	def m_peakRamUsage(self, value: long): ...


	@property
	def m_peakSwapUsage(self) -> long:
		"""
		
        
		"""
	@m_peakSwapUsage.setter
	def m_peakSwapUsage(self, value: long): ...


	@property
	def m_pluginDataFileName(self) -> Text:
		"""
		
        
		"""
	@m_pluginDataFileName.setter
	def m_pluginDataFileName(self, value: Text): ...


	@property
	def m_pluginDataFileSize(self) -> long:
		"""
		
        
		"""
	@m_pluginDataFileSize.setter
	def m_pluginDataFileSize(self, value: long): ...


	@property
	def m_pluginName(self) -> Text:
		"""
		
        
		"""
	@m_pluginName.setter
	def m_pluginName(self, value: Text): ...


	@property
	def m_pool(self) -> Text:
		"""
		
        
		"""
	@m_pool.setter
	def m_pool(self, value: Text): ...


	@property
	def m_priority(self) -> int:
		"""
		
        
		"""
	@m_priority.setter
	def m_priority(self, value: int): ...


	@property
	def m_renderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_renderTime.setter
	def m_renderTime(self, value: TimeSpan): ...


	@property
	def m_startedDateTime(self) -> DateTime:
		"""
		
        
		"""
	@m_startedDateTime.setter
	def m_startedDateTime(self, value: DateTime): ...


	@property
	def m_submitDateTime(self) -> DateTime:
		"""
		
        
		"""
	@m_submitDateTime.setter
	def m_submitDateTime(self, value: DateTime): ...


	@property
	def m_submitMachineName(self) -> Text:
		"""
		
        
		"""
	@m_submitMachineName.setter
	def m_submitMachineName(self, value: Text): ...


	@property
	def m_taskCount(self) -> int:
		"""
		
        
		"""
	@m_taskCount.setter
	def m_taskCount(self, value: int): ...


	@property
	def m_totalCpuClocks(self) -> long:
		"""
		
        
		"""
	@m_totalCpuClocks.setter
	def m_totalCpuClocks(self, value: long): ...


	@property
	def m_totalImageFileSize(self) -> long:
		"""
		
        
		"""
	@m_totalImageFileSize.setter
	def m_totalImageFileSize(self, value: long): ...


	@property
	def m_totalNormalizedTaskRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_totalNormalizedTaskRenderTime.setter
	def m_totalNormalizedTaskRenderTime(self, value: TimeSpan): ...


	@property
	def m_totalTaskRenderTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_totalTaskRenderTime.setter
	def m_totalTaskRenderTime(self, value: TimeSpan): ...


	@property
	def m_totalTaskStartupTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_totalTaskStartupTime.setter
	def m_totalTaskStartupTime(self, value: TimeSpan): ...


	@property
	def m_totalTaskTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_totalTaskTime.setter
	def m_totalTaskTime(self, value: TimeSpan): ...


	@property
	def m_usedCpuClocks(self) -> long:
		"""
		
        
		"""
	@m_usedCpuClocks.setter
	def m_usedCpuClocks(self, value: long): ...


	@property
	def m_userName(self) -> Text:
		"""
		
        
		"""
	@m_userName.setter
	def m_userName(self, value: Text): ...


	@property
	def m_wastedErrorTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_wastedErrorTime.setter
	def m_wastedErrorTime(self, value: TimeSpan): ...


	@property
	def m_wastedRequeueTime(self) -> TimeSpan:
		"""
		
        
		"""
	@m_wastedRequeueTime.setter
	def m_wastedRequeueTime(self, value: TimeSpan): ...


	@property
	def ENTRY_TIME_FIELD(self) -> readonlystring:
		"""
		
The entry time field key.         
		"""
	@ENTRY_TIME_FIELD.setter
	def ENTRY_TIME_FIELD(self, value: readonlystring): ...

