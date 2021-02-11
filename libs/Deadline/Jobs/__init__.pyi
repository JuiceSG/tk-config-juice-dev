class AutoJobCleanupType:
	DeleteJobs = None # Delete all unarchived completed jobs.           
	ArchiveJobs = None # Archive all unarchived completed jobs.           


class JobCompleteAction:
	Archive = None # The job should be archived when it completes.           
	Delete = None # The job should be deleted when it completes.           
	Nothing = None # Nothing should be done when the job is complete.           


class JobScheduledType:
	None = 0 # The job is not scheduled.           
	NotScheduled = None # The Job is not scheduled. Synonym for the 'None' type for Python compatibility purposes.           
	Once = 1 # The job is scheduled to run once.           
	Daily = 2 # The job is scheduled to run on daily intervals.           
	Custom = 3 # The job follows a custom schedule.           


class JobStatus:
	Unknown = 0 # The job state is unknown.           
	Active = 1 # The job is active (queued or rendering).           
	Suspended = 2 # The job is suspended.           
	Completed = 3 # The job is completed.           
	Failed = 4 # The job has failed.           
	Pending = 6 # The job is pending.           


class TaskOnTimeout:
	ErrorAndNotify = None # Report an error and notify the user.           
	Error = None # Report an error only.           
	Notify = None # Notify the user only.           
	Complete = None # Mark the task as complete.           
	RequeueAndNotify = None # Requeue the task and notify the user.           
	Requeue = None # Fail the task and report an error.           
	FailAndNotify = None # Fail the task, report an error, and notify the user.           
	Fail = None # Fail the task and report an error.           


class TaskStatus:
	Unknown = 1 # The task's state is unknown.           
	Queued = 2 # The task is queued.           
	Suspended = 3 # The task is suspended.           
	Rendering = 4 # The task is rendering.           
	Completed = 5 # The task has completed.           
	Failed = 6 # The task has failed.           
	Pending = 8 # The task is pending.           


from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Jobs import AssetDependency
class AssetDependency(Deadline.Jobs.OffsetDependency):
	"""
	 The AssetDependency Class
	"""

	@property
	def FileName(self) -> Text:
		"""
		
The asset dependency filename.         
		"""
	@FileName.setter
	def FileName(self, value: Text): ...


	@property
	def FrameString(self) -> Text:
		"""
		
The frame string that requires this dependency.         
		"""
	@FrameString.setter
	def FrameString(self, value: Text): ...


	@property
	def IsFrameAware(self) -> bool:
		"""
		
Whether the dependency is frame aware or not.         
		"""
	@IsFrameAware.setter
	def IsFrameAware(self, value: bool): ...


	@property
	def m_fileName(self) -> Text:
		"""
		
        
		"""
	@m_fileName.setter
	def m_fileName(self, value: Text): ...


	@property
	def m_frameAware(self) -> bool:
		"""
		
        
		"""
	@m_frameAware.setter
	def m_frameAware(self, value: bool): ...


	@property
	def m_frameString(self) -> Text:
		"""
		
        
		"""
	@m_frameString.setter
	def m_frameString(self, value: Text): ...

	def __init__(self, ):
		"""
		Default constructor. 

		
		:return: 
		"""

	def __init__(self, fileName: Text):
		"""
		The overloaded constructor that allows a filename to be specified. 

		:param Text fileName: 
		:return: 
		"""

	def Clone(self, ) -> newobject:
		"""
		Clones this 

		
		:return: A clone of this AssetDependency.
		"""

	def Copy(self, ) -> AssetDependency:
		"""
		Copies this 

		
		:return: A copy of this AssetDependency.
		"""

	def Equals(self, obj: object) -> overridebool:
		"""
		Override for Equals 

		:param object obj: 
		:return: 
		"""

	def ToString(self, ) -> overridestring:
		"""
		Returns the file name. 

		
		:return: The file name as a string.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class BaseDependency(ICloneable):
	"""
	 BaseDependency class.
	"""

	@property
	def IgnoreFrameOffsets(self) -> bool:
		"""
		
Whether or not to ignore frame offsets.         
		"""
	@IgnoreFrameOffsets.setter
	def IgnoreFrameOffsets(self, value: bool): ...


	@property
	def Notes(self) -> Text:
		"""
		
Notes for the dependency.         
		"""
	@Notes.setter
	def Notes(self, value: Text): ...


	@property
	def m_ignoreFrameOffsets(self) -> bool:
		"""
		
        
		"""
	@m_ignoreFrameOffsets.setter
	def m_ignoreFrameOffsets(self, value: bool): ...


	@property
	def m_notes(self) -> Text:
		"""
		
        
		"""
	@m_notes.setter
	def m_notes(self, value: Text): ...

	def __init__(self, ):
		"""
		Default constructor. 

		
		:return: 
		"""

	def __init__(self, notes: Text, ignoreFrameOffsets: bool):
		"""
		Overloaded constructor that allows the notes and ignoreFrameOffsets to be specified. 

		:param Text notes: 
		:param bool ignoreFrameOffsets: 
		:return: 
		"""

	def Clone(self, ) -> object:
		"""
		Clones this instance of the 

		
		:return: A clone of this BaseDependency.
		"""

	def Equals(self, obj: object) -> overridebool:
		"""
		Override for equals 

		:param object obj: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Jobs import AssetDependency
from Deadline.Jobs import ScriptDependency
class Job(LastWriteDocument):
	"""
	 A job.
	"""

	@property
	def JobAuxiliarySubmissionFileNames(self) -> Iterable[Text]:
		"""
		
The auxiliary files submitted with the job.         
		"""


	@property
	def JobBatchName(self) -> Text:
		"""
		
The name of the Batch that this job belongs to.         
		"""
	@JobBatchName.setter
	def JobBatchName(self, value: Text): ...


	@property
	def JobComment(self) -> Text:
		"""
		
A brief comment about the job.         
		"""
	@JobComment.setter
	def JobComment(self, value: Text): ...


	@property
	def JobCompletedDateTime(self) -> DateTime:
		"""
		
The date/time at which the job finished rendering.         
		"""


	@property
	def JobCompletedTasks(self) -> int:
		"""
		
The number of tasks in the completed state.         
		"""


	@property
	def JobConcurrentTasks(self) -> int:
		"""
		
The maximum number of concurrent tasks a Worker can dequeue for this job at a time. The value must be between 1 and 16 inclusive.         
		"""
	@JobConcurrentTasks.setter
	def JobConcurrentTasks(self, value: int): ...


	@property
	def JobCustomEventPluginDirectory(self) -> Text:
		"""
		
A custom location to load the job's event plugin from.         
		"""
	@JobCustomEventPluginDirectory.setter
	def JobCustomEventPluginDirectory(self, value: Text): ...


	@property
	def JobCustomPluginDirectory(self) -> Text:
		"""
		
A custom location to load the job's plugin from.         
		"""
	@JobCustomPluginDirectory.setter
	def JobCustomPluginDirectory(self, value: Text): ...


	@property
	def JobDepartment(self) -> Text:
		"""
		
The department to which the job's user belongs to.         
		"""
	@JobDepartment.setter
	def JobDepartment(self, value: Text): ...


	@property
	def JobDependencyIDs(self) -> Iterable[Text]:
		"""
		
The ids of the jobs that this job is dependent on.         
		"""


	@property
	def JobDependencyPercentageValue(self) -> float:
		"""
		
This job will resume when its dependencies have completed this percentage of their tasks.         
		"""
	@JobDependencyPercentageValue.setter
	def JobDependencyPercentageValue(self, value: float): ...


	@property
	def JobEmailNotification(self) -> bool:
		"""
		
If overriding the user's notification method, whether to use email notification.         
		"""
	@JobEmailNotification.setter
	def JobEmailNotification(self, value: bool): ...


	@property
	def JobEnableAutoTimeout(self) -> bool:
		"""
		
The Auto Task Timeout feature is based on the Auto Job Timeout Settings in the Repository Options. The timeout is based on the render times of the tasks that have already finished for this job, so this option should only be used if the frames for the job have consistent render times.         
		"""
	@JobEnableAutoTimeout.setter
	def JobEnableAutoTimeout(self, value: bool): ...


	@property
	def JobEnableFrameTimeouts(self) -> bool:
		"""
		
If the timeouts are Frame based instead of Task based.         
		"""
	@JobEnableFrameTimeouts.setter
	def JobEnableFrameTimeouts(self, value: bool): ...


	@property
	def JobEnableTimeoutsForScriptTasks(self) -> bool:
		"""
		
If the timeouts should apply to pre/post job script tasks.         
		"""
	@JobEnableTimeoutsForScriptTasks.setter
	def JobEnableTimeoutsForScriptTasks(self, value: bool): ...


	@property
	def JobExtraInfo0(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo0.setter
	def JobExtraInfo0(self, value: Text): ...


	@property
	def JobExtraInfo1(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo1.setter
	def JobExtraInfo1(self, value: Text): ...


	@property
	def JobExtraInfo2(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo2.setter
	def JobExtraInfo2(self, value: Text): ...


	@property
	def JobExtraInfo3(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo3.setter
	def JobExtraInfo3(self, value: Text): ...


	@property
	def JobExtraInfo4(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo4.setter
	def JobExtraInfo4(self, value: Text): ...


	@property
	def JobExtraInfo5(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo5.setter
	def JobExtraInfo5(self, value: Text): ...


	@property
	def JobExtraInfo6(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo6.setter
	def JobExtraInfo6(self, value: Text): ...


	@property
	def JobExtraInfo7(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo7.setter
	def JobExtraInfo7(self, value: Text): ...


	@property
	def JobExtraInfo8(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo8.setter
	def JobExtraInfo8(self, value: Text): ...


	@property
	def JobExtraInfo9(self) -> Text:
		"""
		
One of the Job's ten Extra Info fields.         
		"""
	@JobExtraInfo9.setter
	def JobExtraInfo9(self, value: Text): ...


	@property
	def JobFailedTasks(self) -> int:
		"""
		
The number of tasks in the failed state.         
		"""


	@property
	def JobFailureDetectionJobErrors(self) -> int:
		"""
		
If JobOverrideJobFailureDetection is enabled, this is the number of errors it takes to trigger a job failure.         
		"""
	@JobFailureDetectionJobErrors.setter
	def JobFailureDetectionJobErrors(self, value: int): ...


	@property
	def JobFailureDetectionTaskErrors(self) -> int:
		"""
		
If JobOverrideTaskFailureDetection is enabled, this is the number of errors it takes to trigger a task failure.         
		"""
	@JobFailureDetectionTaskErrors.setter
	def JobFailureDetectionTaskErrors(self, value: int): ...


	@property
	def JobForceReloadPlugin(self) -> bool:
		"""
		
Whether or not the job's plugin should be reloaded between tasks.         
		"""
	@JobForceReloadPlugin.setter
	def JobForceReloadPlugin(self, value: bool): ...


	@property
	def JobFrameDependencyOffsetEnd(self) -> int:
		"""
		
The end offset for frame depenencies.         
		"""
	@JobFrameDependencyOffsetEnd.setter
	def JobFrameDependencyOffsetEnd(self, value: int): ...


	@property
	def JobFrameDependencyOffsetStart(self) -> int:
		"""
		
The start offset for frame depenencies.         
		"""
	@JobFrameDependencyOffsetStart.setter
	def JobFrameDependencyOffsetStart(self, value: int): ...


	@property
	def JobFrames(self) -> Text:
		"""
		
The job's frame list as a string.         
		"""


	@property
	def JobFramesList(self) -> Iterable[int]:
		"""
		
The job's frame list as an array.         
		"""


	@property
	def JobFramesPerTask(self) -> int:
		"""
		
The number of frames per task.         
		"""


	@property
	def JobFridayStartTime(self) -> TimeSpan:
		"""
		
Gets or sets Friday's start time.         
		"""
	@JobFridayStartTime.setter
	def JobFridayStartTime(self, value: TimeSpan): ...


	@property
	def JobFridayStopTime(self) -> TimeSpan:
		"""
		
Gets or sets Friday's stop time.         
		"""
	@JobFridayStopTime.setter
	def JobFridayStopTime(self, value: TimeSpan): ...


	@property
	def JobGroup(self) -> Text:
		"""
		
The job's group.         
		"""
	@JobGroup.setter
	def JobGroup(self, value: Text): ...


	@property
	def JobId(self) -> Text:
		"""
		
The job's ID.         
		"""


	@property
	def JobIgnoreBadSlaveDetection(self) -> bool:
		"""
		
Whether or not this job overrides the Bad Worker Detection settings in the Repository Options.         
		"""
	@JobIgnoreBadSlaveDetection.setter
	def JobIgnoreBadSlaveDetection(self, value: bool): ...


	@property
	def JobInitializePluginTimeoutSeconds(self) -> int:
		"""
		
The timespan a job's task has to start before a timeout occurs.         
		"""
	@JobInitializePluginTimeoutSeconds.setter
	def JobInitializePluginTimeoutSeconds(self, value: int): ...


	@property
	def JobInterruptible(self) -> bool:
		"""
		
If the job is interruptible, which causes it to be canceled when a job with higher priority comes along.         
		"""
	@JobInterruptible.setter
	def JobInterruptible(self, value: bool): ...


	@property
	def JobInterruptiblePercentage(self) -> int:
		"""
		
The completion percentage that this Job must be less than in order to be interruptible.         
		"""
	@JobInterruptiblePercentage.setter
	def JobInterruptiblePercentage(self, value: int): ...


	@property
	def JobIsFrameDependent(self) -> bool:
		"""
		
If the job is frame dependent.         
		"""
	@JobIsFrameDependent.setter
	def JobIsFrameDependent(self, value: bool): ...


	@property
	def JobLimitGroups(self) -> Iterable[Text]:
		"""
		
The limit groups the job requires.         
		"""


	@property
	def JobLimitTasksToNumberOfCpus(self) -> bool:
		"""
		
Whether or not the number of concurrent tasks a Worker can dequeue for this job should be limited to the number of CPUs the Worker has.         
		"""
	@JobLimitTasksToNumberOfCpus.setter
	def JobLimitTasksToNumberOfCpus(self, value: bool): ...


	@property
	def JobListedSlaves(self) -> Iterable[Text]:
		"""
		
The list of Workers in allow or deny list for the job. Use JobWhitelistFlag to determine if the list is a deny list or an allow list.         
		"""


	@property
	def JobMachineLimit(self) -> int:
		"""
		
The machine limit for the job.         
		"""


	@property
	def JobMachineLimitProgress(self) -> float:
		"""
		
When the Worker reaches this progress for the job's task, it will release the limit group.         
		"""


	@property
	def JobMaintenanceJob(self) -> bool:
		"""
		
If this is a maintenance job.         
		"""


	@property
	def JobMaintenanceJobEndFrame(self) -> int:
		"""
		
The start frame for a maintenance job.         
		"""


	@property
	def JobMaintenanceJobStartFrame(self) -> int:
		"""
		
The start frame for a maintenance job.         
		"""


	@property
	def JobMinRenderTimeSeconds(self) -> int:
		"""
		
The minimum number of seconds a job must run to be considered successful.         
		"""
	@JobMinRenderTimeSeconds.setter
	def JobMinRenderTimeSeconds(self, value: int): ...


	@property
	def JobMondayStartTime(self) -> TimeSpan:
		"""
		
Gets or sets Monday's start time.         
		"""
	@JobMondayStartTime.setter
	def JobMondayStartTime(self, value: TimeSpan): ...


	@property
	def JobMondayStopTime(self) -> TimeSpan:
		"""
		
Gets or sets Monday's stop time.         
		"""
	@JobMondayStopTime.setter
	def JobMondayStopTime(self, value: TimeSpan): ...


	@property
	def JobName(self) -> Text:
		"""
		
The job's name.         
		"""
	@JobName.setter
	def JobName(self, value: Text): ...


	@property
	def JobNotificationEmails(self) -> Iterable[Text]:
		"""
		
Arbitrary email addresses to send notifications to when this job is complete.         
		"""


	@property
	def JobNotificationNote(self) -> Text:
		"""
		
A note to append to the notification email sent out when the job is complete.         
		"""
	@JobNotificationNote.setter
	def JobNotificationNote(self, value: Text): ...


	@property
	def JobNotificationTargets(self) -> Iterable[Text]:
		"""
		
The list of users that are to be notified when this job is complete.         
		"""


	@property
	def JobOnJobComplete(self) -> Text:
		"""
		
What the job should do when it completes. The options are "Archive", "Delete", or "Nothing".         
		"""
	@JobOnJobComplete.setter
	def JobOnJobComplete(self, value: Text): ...


	@property
	def JobOnTaskTimeout(self) -> Text:
		"""
		
What to do when a task times out. The options are "Error", "Notify", or "Both".         
		"""
	@JobOnTaskTimeout.setter
	def JobOnTaskTimeout(self, value: Text): ...


	@property
	def JobOutputDirectories(self) -> Iterable[Text]:
		"""
		
The list of output directories.         
		"""


	@property
	def JobOutputFileNames(self) -> Iterable[Text]:
		"""
		
The list of output filenames.         
		"""


	@property
	def JobOutputTileFileNames(self) -> Iterable[Iterable[Text]]:
		"""
		
The list of output filenames for tile jobs.         
		"""


	@property
	def JobOverrideAutoJobCleanup(self) -> bool:
		"""
		
If the job overrides the automatic job cleanup in the Repository Options.         
		"""
	@JobOverrideAutoJobCleanup.setter
	def JobOverrideAutoJobCleanup(self, value: bool): ...


	@property
	def JobOverrideJobCleanup(self) -> bool:
		"""
		
If the job overrides the amount of days before its cleaned up.         
		"""
	@JobOverrideJobCleanup.setter
	def JobOverrideJobCleanup(self, value: bool): ...


	@property
	def JobOverrideJobCleanupDays(self) -> int:
		"""
		
The number of days before this job will be cleaned up after it is completed. Only relevant if the override is set.         
		"""
	@JobOverrideJobCleanupDays.setter
	def JobOverrideJobCleanupDays(self, value: int): ...


	@property
	def JobOverrideJobCleanupType(self) -> AutoJobCleanupType:
		"""
		
The job cleanup mode. Only relevant if the override is set.         
		"""
	@JobOverrideJobCleanupType.setter
	def JobOverrideJobCleanupType(self, value: AutoJobCleanupType): ...


	@property
	def JobOverrideJobFailureDetection(self) -> bool:
		"""
		
Whether or not this job overrides the Job Failure Detection settings in the Repository Options.         
		"""
	@JobOverrideJobFailureDetection.setter
	def JobOverrideJobFailureDetection(self, value: bool): ...


	@property
	def JobOverrideNotificationMethod(self) -> bool:
		"""
		
If the user's notification method should be ignored.         
		"""
	@JobOverrideNotificationMethod.setter
	def JobOverrideNotificationMethod(self, value: bool): ...


	@property
	def JobOverrideTaskExtraInfoNames(self) -> bool:
		"""
		
Whether this job overrides the task extra info names.         
		"""
	@JobOverrideTaskExtraInfoNames.setter
	def JobOverrideTaskExtraInfoNames(self, value: bool): ...


	@property
	def JobOverrideTaskFailureDetection(self) -> bool:
		"""
		
Whether or not this job overrides the Task Failure Detection settings in the Repository Options.         
		"""
	@JobOverrideTaskFailureDetection.setter
	def JobOverrideTaskFailureDetection(self, value: bool): ...


	@property
	def JobPendingTasks(self) -> int:
		"""
		
The number of tasks in the pending state.         
		"""


	@property
	def JobPlugin(self) -> Text:
		"""
		
The name of the Deadline plugin the job uses.         
		"""


	@property
	def JobPool(self) -> Text:
		"""
		
The job's pool.         
		"""
	@JobPool.setter
	def JobPool(self, value: Text): ...


	@property
	def JobPopupNotification(self) -> bool:
		"""
		
If overriding the user's notification method, whether to use send a popup notification.         
		"""
	@JobPopupNotification.setter
	def JobPopupNotification(self, value: bool): ...


	@property
	def JobPostJobScript(self) -> Text:
		"""
		
The script to execute after the Job finishes. Read Only. Use RepositoryUtils.SetPostJobScript and RepositoryUtils.DeletePostJobScript.         
		"""


	@property
	def JobPostTaskScript(self) -> Text:
		"""
		
The script to execute when a job task is complete.         
		"""
	@JobPostTaskScript.setter
	def JobPostTaskScript(self, value: Text): ...


	@property
	def JobPreJobScript(self) -> Text:
		"""
		
The script to execute before the job starts. Read Only. Use RepositoryUtils.SetPreJobScript and RepositoryUtils.DeletePreJobScript.         
		"""


	@property
	def JobPreTaskScript(self) -> Text:
		"""
		
The script to execute before a job task starts.         
		"""
	@JobPreTaskScript.setter
	def JobPreTaskScript(self, value: Text): ...


	@property
	def JobPriority(self) -> int:
		"""
		
The job's priority (0 is the lowest).         
		"""
	@JobPriority.setter
	def JobPriority(self, value: int): ...


	@property
	def JobProtected(self) -> bool:
		"""
		
If set to True, the job can only be deleted or archived by the job's user, or by someone who has permissions to handle protected jobs.         
		"""
	@JobProtected.setter
	def JobProtected(self, value: bool): ...


	@property
	def JobQueuedTasks(self) -> int:
		"""
		
The number of tasks in the queued state.         
		"""


	@property
	def JobRenderingTasks(self) -> int:
		"""
		
The number of tasks in the active state.         
		"""


	@property
	def JobRequiredAssets(self) -> Iterable[AssetDependency]:
		"""
		
The assets that are required in order to render this job. The assets should contain absolute paths.         
		"""


	@property
	def JobResumeOnCompleteDependencies(self) -> bool:
		"""
		
If the job should resume on complete dependencies.         
		"""
	@JobResumeOnCompleteDependencies.setter
	def JobResumeOnCompleteDependencies(self, value: bool): ...


	@property
	def JobResumeOnDeletedDependencies(self) -> bool:
		"""
		
If the job should resume on deleted dependencies.         
		"""
	@JobResumeOnDeletedDependencies.setter
	def JobResumeOnDeletedDependencies(self, value: bool): ...


	@property
	def JobResumeOnFailedDependencies(self) -> bool:
		"""
		
If the job should resume on failed dependencies.         
		"""
	@JobResumeOnFailedDependencies.setter
	def JobResumeOnFailedDependencies(self, value: bool): ...


	@property
	def JobSaturdayStartTime(self) -> TimeSpan:
		"""
		
Gets or sets Saturday's start time.         
		"""
	@JobSaturdayStartTime.setter
	def JobSaturdayStartTime(self, value: TimeSpan): ...


	@property
	def JobSaturdayStopTime(self) -> TimeSpan:
		"""
		
Gets or sets Saturday's stop time.         
		"""
	@JobSaturdayStopTime.setter
	def JobSaturdayStopTime(self, value: TimeSpan): ...


	@property
	def JobScheduledDays(self) -> int:
		"""
		
The day interval for daily scheduled jobs.         
		"""
	@JobScheduledDays.setter
	def JobScheduledDays(self, value: int): ...


	@property
	def JobScheduledStartDateTime(self) -> DateTime:
		"""
		
The start date/time at which the scheduled job should start.         
		"""
	@JobScheduledStartDateTime.setter
	def JobScheduledStartDateTime(self, value: DateTime): ...


	@property
	def JobScheduledStopDateTime(self) -> DateTime:
		"""
		
The stop date/time at which the job should stop if it's still active.         
		"""
	@JobScheduledStopDateTime.setter
	def JobScheduledStopDateTime(self, value: DateTime): ...


	@property
	def JobScheduledType(self) -> Text:
		"""
		
The scheduling mode for this job. The options are "None", "Once", "Daily". or "Custom".         
		"""
	@JobScheduledType.setter
	def JobScheduledType(self, value: Text): ...


	@property
	def JobScriptDependencies(self) -> Iterable[ScriptDependency]:
		"""
		
The scripts that must return True in order to render this job.         
		"""


	@property
	def JobSecondaryPool(self) -> Text:
		"""
		
The Secondary Pool in which this Job belongs.         
		"""
	@JobSecondaryPool.setter
	def JobSecondaryPool(self, value: Text): ...


	@property
	def JobSendJobErrorWarning(self) -> bool:
		"""
		
If the job should send warning notifications when it reaches a certain number of errors.         
		"""
	@JobSendJobErrorWarning.setter
	def JobSendJobErrorWarning(self, value: bool): ...


	@property
	def JobSequentialJob(self) -> bool:
		"""
		
If the job is a sequential job, which ensures its tasks only render in ascending order.         
		"""
	@JobSequentialJob.setter
	def JobSequentialJob(self, value: bool): ...


	@property
	def JobStartedDateTime(self) -> DateTime:
		"""
		
The date/time at which the job started rendering.         
		"""


	@property
	def JobStartJobTimeoutSeconds(self) -> int:
		"""
		
The timespan a job's task has to start before a timeout occurs.         
		"""
	@JobStartJobTimeoutSeconds.setter
	def JobStartJobTimeoutSeconds(self, value: int): ...


	@property
	def JobStatus(self) -> Text:
		"""
		
The job's current state.         
		"""


	@property
	def JobSubmitDateTime(self) -> DateTime:
		"""
		
The date/time at which the job was submitted.         
		"""


	@property
	def JobSubmitMachine(self) -> Text:
		"""
		
This is the machine that the job was submitted from.         
		"""


	@property
	def JobSundayStartTime(self) -> TimeSpan:
		"""
		
Gets or sets Sunday's start time.         
		"""
	@JobSundayStartTime.setter
	def JobSundayStartTime(self, value: TimeSpan): ...


	@property
	def JobSundayStopTime(self) -> TimeSpan:
		"""
		
Gets or sets Sunday's stop time.         
		"""
	@JobSundayStopTime.setter
	def JobSundayStopTime(self, value: TimeSpan): ...


	@property
	def JobSuppressEvents(self) -> bool:
		"""
		
Whether or not this Job should suppress Events plugins.         
		"""
	@JobSuppressEvents.setter
	def JobSuppressEvents(self, value: bool): ...


	@property
	def JobSuspendedTasks(self) -> int:
		"""
		
The number of tasks in the suspended state.         
		"""


	@property
	def JobSynchronizeAllAuxiliaryFiles(self) -> bool:
		"""
		
If the job's auxiliary files should be synced up by the Worker between tasks.         
		"""
	@JobSynchronizeAllAuxiliaryFiles.setter
	def JobSynchronizeAllAuxiliaryFiles(self, value: bool): ...


	@property
	def JobTaskCount(self) -> int:
		"""
		
The number of tasks the job has.         
		"""


	@property
	def JobTaskExtraInfoName0(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName0.setter
	def JobTaskExtraInfoName0(self, value: Text): ...


	@property
	def JobTaskExtraInfoName1(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName1.setter
	def JobTaskExtraInfoName1(self, value: Text): ...


	@property
	def JobTaskExtraInfoName2(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName2.setter
	def JobTaskExtraInfoName2(self, value: Text): ...


	@property
	def JobTaskExtraInfoName3(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName3.setter
	def JobTaskExtraInfoName3(self, value: Text): ...


	@property
	def JobTaskExtraInfoName4(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName4.setter
	def JobTaskExtraInfoName4(self, value: Text): ...


	@property
	def JobTaskExtraInfoName5(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName5.setter
	def JobTaskExtraInfoName5(self, value: Text): ...


	@property
	def JobTaskExtraInfoName6(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName6.setter
	def JobTaskExtraInfoName6(self, value: Text): ...


	@property
	def JobTaskExtraInfoName7(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName7.setter
	def JobTaskExtraInfoName7(self, value: Text): ...


	@property
	def JobTaskExtraInfoName8(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName8.setter
	def JobTaskExtraInfoName8(self, value: Text): ...


	@property
	def JobTaskExtraInfoName9(self) -> Text:
		"""
		
One of the Task's ten Extra Info names.         
		"""
	@JobTaskExtraInfoName9.setter
	def JobTaskExtraInfoName9(self, value: Text): ...


	@property
	def JobTaskTimeoutSeconds(self) -> int:
		"""
		
The timespan a job's task has to render before a timeout occurs.         
		"""
	@JobTaskTimeoutSeconds.setter
	def JobTaskTimeoutSeconds(self, value: int): ...


	@property
	def JobThursdayStartTime(self) -> TimeSpan:
		"""
		
Gets or sets Thursday's start time.         
		"""
	@JobThursdayStartTime.setter
	def JobThursdayStartTime(self, value: TimeSpan): ...


	@property
	def JobThursdayStopTime(self) -> TimeSpan:
		"""
		
Gets or sets Thursday's stop time.         
		"""
	@JobThursdayStopTime.setter
	def JobThursdayStopTime(self, value: TimeSpan): ...


	@property
	def JobTileJob(self) -> bool:
		"""
		
If this job is a tile job.         
		"""


	@property
	def JobTileJobFrame(self) -> int:
		"""
		
The frame that the tile job is rendering.         
		"""


	@property
	def JobTileJobTileCount(self) -> int:
		"""
		
The number of tiles in a tile job.         
		"""


	@property
	def JobTileJobTilesInX(self) -> int:
		"""
		
The number of tiles in X for a tile job. This is deprecated, and is only here for backwards compatibility.         
		"""


	@property
	def JobTileJobTilesInY(self) -> int:
		"""
		
The number of tiles in Y for a tile job. This is deprecated, and is only here for backwards compatibility.         
		"""


	@property
	def JobTuesdayStartTime(self) -> TimeSpan:
		"""
		
Gets or sets Tuesday's start time.         
		"""
	@JobTuesdayStartTime.setter
	def JobTuesdayStartTime(self, value: TimeSpan): ...


	@property
	def JobTuesdayStopTime(self) -> TimeSpan:
		"""
		
Gets or sets Tuesday's stop time.         
		"""
	@JobTuesdayStopTime.setter
	def JobTuesdayStopTime(self, value: TimeSpan): ...


	@property
	def JobUseJobEnvironmentOnly(self) -> bool:
		"""
		
If only the job's environment variables should be used. If disabled, the job's environment will be merged with the current environment.         
		"""
	@JobUseJobEnvironmentOnly.setter
	def JobUseJobEnvironmentOnly(self, value: bool): ...


	@property
	def JobUserName(self) -> Text:
		"""
		
The user that submitted the job.         
		"""
	@JobUserName.setter
	def JobUserName(self, value: Text): ...


	@property
	def JobWednesdayStartTime(self) -> TimeSpan:
		"""
		
Gets or sets Wednesday's start time.         
		"""
	@JobWednesdayStartTime.setter
	def JobWednesdayStartTime(self, value: TimeSpan): ...


	@property
	def JobWednesdayStopTime(self) -> TimeSpan:
		"""
		
Gets or sets Wednesday's stop time.         
		"""
	@JobWednesdayStopTime.setter
	def JobWednesdayStopTime(self, value: TimeSpan): ...


	@property
	def JobWhitelistFlag(self) -> bool:
		"""
		
If the job's listed Workers are an allow list or a deny list.         
		"""


	@property
	def RemTimeThreshold(self) -> int:
		"""
		
The remaining time (in seconds) that this Job must have left more than in order to be interruptible.         
		"""
	@RemTimeThreshold.setter
	def RemTimeThreshold(self, value: int): ...


	@property
	def DisabledScheduleTime(self) -> TimeSpan:
		"""
		
Represents a disabled scheduled time for custom job scheduling settings.         
		"""
	@DisabledScheduleTime.setter
	def DisabledScheduleTime(self, value: TimeSpan): ...

	def DeleteJobEnvironmentKey(self, key: Text):
		"""
		Deletes the environment variable for the given key. 

		:param Text key: The key.
		:return: 
		"""

	def DeleteJobExtraInfoKey(self, key: Text):
		"""
		Deletes the extra info for the given key. 

		:param Text key: The key.
		:return: 
		"""

	def GetJobEnvironmentKeys(self, ) -> Iterable[Text]:
		"""
		Gets the keys for the job's environment variable entries. 

		
		:return: The keys, as a list of strings.
		"""

	def GetJobEnvironmentKeyValue(self, key: Text) -> Text:
		"""
		Gets the environment variable value for the given key. 

		:param Text key: The key.
		:return: The value, as a string. If the key isn't found, an empty string is returned.
		"""

	def GetJobExtraInfoKeys(self, ) -> Iterable[Text]:
		"""
		Gets the keys for the job's extra info entries. 

		
		:return: The keys, as a list of strings.
		"""

	def GetJobExtraInfoKeyValue(self, key: Text) -> Text:
		"""
		Gets the extra info value for the given key. 

		:param Text key: The key.
		:return: The value, as a string. If the key isn't found, an empty string is returned.
		"""

	def GetJobExtraInfoKeyValueWithDefault(self, key: Text, defaultValue: Text) -> Text:
		"""
		Gets the extra info value for the given key. 

		:param Text key: The key.
		:param Text defaultValue: The default value.
		:return: The value, as a string. If the key isn't found, an empty string is returned.
		"""

	def GetJobInfoKeys(self, ) -> Iterable[Text]:
		"""
		Gets the job info keys. 

		
		:return: 
		"""

	def GetJobInfoKeyValue(self, key: Text) -> Text:
		"""
		Get the job infor value for the provided key. 

		:param Text key: 
		:return: 
		"""

	def GetJobPluginInfoKeys(self, ) -> Iterable[Text]:
		"""
		Gets the keys for the job's plugin info entries. 

		
		:return: The keys, as a list of strings.
		"""

	def GetJobPluginInfoKeyValue(self, key: Text) -> Text:
		"""
		Gets the plugin info value for the given key. 

		:param Text key: The key.
		:return: The value, as a string. If the key isn't found, an empty string is returned.
		"""

	def SetJobDependencyIDs(self, jobIds: object):
		"""
		Sets the IDs of the jobs that this job is dependent on. 

		:param object jobIds: The job IDs. This should be a list of strings.
		:return: 
		"""

	def SetJobEnvironmentKeyValue(self, key: Text, value: Text):
		"""
		Sets the environment variable value for the given key. 

		:param Text key: The key.
		:param Text value: The value.
		:return: 
		"""

	def SetJobExtraInfoKeyValue(self, key: Text, value: Text):
		"""
		Sets the extra info value for the given key. 

		:param Text key: The key.
		:param Text value: The value.
		:return: 
		"""

	def SetJobLimitGroups(self, limitGroups: object):
		"""
		Sets the limit groups the job requires. 

		:param object limitGroups: The limit group names. This should be a list of strings.
		:return: 
		"""

	def SetJobNotificationEmails(self, emails: object):
		"""
		Sets the arbitrary email addresses to send notifications to when this job is complete. 

		:param object emails: The email addresses. This should be a list of strings.
		:return: 
		"""

	def SetJobNotificationTargets(self, userNames: object):
		"""
		Sets the list of users that are to be notified when this job is complete. 

		:param object userNames: The user names. This should be a list of strings.
		:return: 
		"""

	def SetJobPluginInfoKeyValue(self, key: Text, value: Text):
		"""
		Sets the plugin info value for the given key. 

		:param Text key: The key.
		:param Text value: The value.
		:return: 
		"""

	def SetJobRequiredAssets(self, assets: object):
		"""
		Sets the assets that are required in order to render this job. The assets should contain absolute paths. 

		:param object assets: The asset paths. These should be absolute paths. This should be a list of strings.
		:return: 
		"""

	def SetScriptDependencies(self, scripts: object):
		"""
		Sets the scripts that must return True in order to render this job. 

		:param object scripts: The script paths. This should be a list of strings.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Jobs import JobDependency
class JobDependency(Deadline.Jobs.OffsetDependency):
	"""
	 Job Dependency class.
	"""

	@property
	def JobID(self) -> Text:
		"""
		
The Job Id of the dependency.         
		"""
	@JobID.setter
	def JobID(self, value: Text): ...


	@property
	def OverrideResumeOn(self) -> bool:
		"""
		
If enabled this job overrides the resume on settings.         
		"""
	@OverrideResumeOn.setter
	def OverrideResumeOn(self, value: bool): ...


	@property
	def ResumeOnComplete(self) -> bool:
		"""
		
Enables resuming the dependent job when the Job Dependency completes.         
		"""
	@ResumeOnComplete.setter
	def ResumeOnComplete(self, value: bool): ...


	@property
	def ResumeOnDeleted(self) -> bool:
		"""
		
Enables resuming the dependent job when the Job Dependency is deleted.         
		"""
	@ResumeOnDeleted.setter
	def ResumeOnDeleted(self, value: bool): ...


	@property
	def ResumeOnFailed(self) -> bool:
		"""
		
Enables resuming the dependent job when the Job Dependency fails.         
		"""
	@ResumeOnFailed.setter
	def ResumeOnFailed(self, value: bool): ...


	@property
	def ResumeOnPercentageCompleted(self) -> bool:
		"""
		
Enables resuming a Job after the dependency has completed to a certain percentage.         
		"""
	@ResumeOnPercentageCompleted.setter
	def ResumeOnPercentageCompleted(self, value: bool): ...


	@property
	def ResumeOnPercentageValue(self) -> float:
		"""
		
The completion percentage value of the dependency that must be reached before the dependant job is resumed.         
		"""
	@ResumeOnPercentageValue.setter
	def ResumeOnPercentageValue(self, value: float): ...


	@property
	def m_jobID(self) -> Text:
		"""
		
        
		"""
	@m_jobID.setter
	def m_jobID(self, value: Text): ...


	@property
	def m_overrideResumeOn(self) -> bool:
		"""
		
        
		"""
	@m_overrideResumeOn.setter
	def m_overrideResumeOn(self, value: bool): ...


	@property
	def m_resumeOnComplete(self) -> bool:
		"""
		
        
		"""
	@m_resumeOnComplete.setter
	def m_resumeOnComplete(self, value: bool): ...


	@property
	def m_resumeOnDeleted(self) -> bool:
		"""
		
        
		"""
	@m_resumeOnDeleted.setter
	def m_resumeOnDeleted(self, value: bool): ...


	@property
	def m_resumeOnFailed(self) -> bool:
		"""
		
        
		"""
	@m_resumeOnFailed.setter
	def m_resumeOnFailed(self, value: bool): ...


	@property
	def m_resumeOnPercentageCompleted(self) -> bool:
		"""
		
        
		"""
	@m_resumeOnPercentageCompleted.setter
	def m_resumeOnPercentageCompleted(self, value: bool): ...


	@property
	def m_resumeOnPercentageValue(self) -> float:
		"""
		
        
		"""
	@m_resumeOnPercentageValue.setter
	def m_resumeOnPercentageValue(self, value: float): ...

	def Clone(self, ) -> newobject:
		"""
		Clones this 

		
		:return: A clone of this JobDependency.
		"""

	def Copy(self, ) -> JobDependency:
		"""
		Copies this 

		
		:return: A copy of this JobDependency.
		"""

	def Equals(self, obj: object) -> overridebool:
		"""
		Override equals 

		:param object obj: 
		:return: 
		"""

	def __init__(self, ):
		"""
		Default constructor. 

		
		:return: 
		"""

	def __init__(self, jobID: Text):
		"""
		Overloaded constructor that allows the job id to be specified. 

		:param Text jobID: 
		:return: 
		"""

	def ToString(self, ) -> overridestring:
		"""
		Returns the job ID. 

		
		:return: The job ID as a string.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class OffsetDependency(Deadline.Jobs.BaseDependency):
	"""
	 OffsetDependency class
	"""

	@property
	def EndOffset(self) -> int:
		"""
		
The end offset for the dependency.         
		"""
	@EndOffset.setter
	def EndOffset(self, value: int): ...


	@property
	def OverrideFrameOffsets(self) -> bool:
		"""
		
Whether or not to override frame offsets for this dependency.         
		"""
	@OverrideFrameOffsets.setter
	def OverrideFrameOffsets(self, value: bool): ...


	@property
	def StartOffset(self) -> int:
		"""
		
The start offset for the dependency.         
		"""
	@StartOffset.setter
	def StartOffset(self, value: int): ...


	@property
	def m_endOffset(self) -> int:
		"""
		
        
		"""
	@m_endOffset.setter
	def m_endOffset(self, value: int): ...


	@property
	def m_overrideFrameOffsets(self) -> bool:
		"""
		
        
		"""
	@m_overrideFrameOffsets.setter
	def m_overrideFrameOffsets(self, value: bool): ...


	@property
	def m_startOffset(self) -> int:
		"""
		
        
		"""
	@m_startOffset.setter
	def m_startOffset(self, value: int): ...

	def Clone(self, ) -> overrideobject:
		"""
		Clones this 

		
		:return: A clone of this OffsetDependency.
		"""

	def Equals(self, obj: object) -> overridebool:
		"""
		Override for equals 

		:param object obj: 
		:return: 
		"""

	def __init__(self, ):
		"""
		Default constructor. 

		
		:return: 
		"""

	def __init__(self, notes: Text, overrideFrameOffset: bool, startOffset: int, endOffset: int, ignoreFrameOffset: bool):
		"""
		Constructor. 

		:param Text notes: 
		:param bool overrideFrameOffset: 
		:param int startOffset: 
		:param int endOffset: 
		:param bool ignoreFrameOffset: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Jobs import ScriptDependency
class ScriptDependency(Deadline.Jobs.BaseDependency):
	"""
	 ScriptDependency class.
	"""

	@property
	def FileName(self) -> Text:
		"""
		
The file name for the script.         
		"""
	@FileName.setter
	def FileName(self, value: Text): ...


	@property
	def m_fileName(self) -> Text:
		"""
		
        
		"""
	@m_fileName.setter
	def m_fileName(self, value: Text): ...

	def Clone(self, ) -> newobject:
		"""
		Clones this script dependency and returns it. 

		
		:return: A clone of this script dependency.
		"""

	def Copy(self, ) -> ScriptDependency:
		"""
		Copies this script dependency and returns it. 

		
		:return: A copy of this script dependency.
		"""

	def Equals(self, obj: object) -> overridebool:
		"""
		Override for Equals 

		:param object obj: 
		:return: 
		"""

	def __init__(self, ):
		"""
		Default constructor. 

		
		:return: 
		"""

	def __init__(self, fileName: Text):
		"""
		Overloaded constructor that allows a filename to be passed in. 

		:param Text fileName: 
		:return: 
		"""

	def ToString(self, ) -> overridestring:
		"""
		Returns the file name. 

		
		:return: The file name as a string.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Jobs import Task
from Deadline.Jobs import TaskProperties
class Task(BaseDocument):
	"""
	 A task.
	"""

	@property
	def TaskAverageRam(self) -> long:
		"""
		
The average amount of RAM used during rendering.         
		"""


	@property
	def TaskAverageRamPercentage(self) -> int:
		"""
		
The average percentage of RAM used during rendering.         
		"""


	@property
	def TaskAverageSwap(self) -> long:
		"""
		
The average Swap used during rendering.         
		"""


	@property
	def TaskCompletedDateTime(self) -> DateTime:
		"""
		
The date/time at which the Task was completed.         
		"""


	@property
	def TaskCpuUtilisation(self) -> int:
		"""
		
The CPU utilization during rendering.         
		"""


	@property
	def TaskErrorCount(self) -> int:
		"""
		
The amount of errors on the Task.         
		"""


	@property
	def TaskFrameList(self) -> Iterable[int]:
		"""
		
The Job's frame list as an array.         
		"""


	@property
	def TaskFrameString(self) -> Text:
		"""
		
The job's frame list as a string.         
		"""


	@property
	def TaskId(self) -> Text:
		"""
		
The task's ID. This is the numeric task ID, as a string.         
		"""


	@property
	def TaskIsStarted(self) -> bool:
		"""
		
True if the Task is in the process of being started.         
		"""


	@property
	def TaskJobId(self) -> Text:
		"""
		
The ID of the Job associated with this Task.         
		"""


	@property
	def TaskName(self) -> Text:
		"""
		
The name of the Task which uniquely identifies it using the format: jobID_frameID_frameString.         
		"""


	@property
	def TaskNormalizedRenderTime(self) -> TimeSpan:
		"""
		
The normalized time taken to render the Task.         
		"""


	@property
	def TaskOutputFileSize(self) -> long:
		"""
		
The size of the output Image file.         
		"""


	@property
	def TaskPeakCpuUsage(self) -> int:
		"""
		
The peak CPU-usage during rendering.         
		"""


	@property
	def TaskPeakRamPercentage(self) -> int:
		"""
		
The peak RAM percentage used during rendering.         
		"""


	@property
	def TaskPeakRamUsage(self) -> long:
		"""
		
The peak amount of RAM used during rendering.         
		"""


	@property
	def TaskPeakSwap(self) -> long:
		"""
		
The peak Swap used during rendering.         
		"""


	@property
	def TaskProgress(self) -> Text:
		"""
		
The Task's current progress.         
		"""


	@property
	def TaskProperties(self) -> TaskProperties:
		"""
		
Container for the Task's properties. If these properties are modified, they can be committed using RepositoryUtils.UpdateTaskProperties().         
		"""


	@property
	def TaskRenderStartTime(self) -> DateTime:
		"""
		
The date/time the Task started rendering.         
		"""


	@property
	def TaskRenderStatus(self) -> Text:
		"""
		
The current status message for the Task, if it's rendering.         
		"""


	@property
	def TaskRenderTime(self) -> TimeSpan:
		"""
		
The time taken to render the Task.         
		"""


	@property
	def TaskRenderTimeMultiplier(self) -> float:
		"""
		
The normalizing multiplier.         
		"""


	@property
	def TaskSlaveName(self) -> Text:
		"""
		
The name of the Worker that rendered/is rendering this Task.         
		"""


	@property
	def TaskStatus(self) -> Text:
		"""
		
The Task's current state.         
		"""


	@property
	def TaskTotalCpuClocks(self) -> long:
		"""
		
The total CPU clocks that could have been utilized during rendering.         
		"""


	@property
	def TaskUsedCpuClocks(self) -> long:
		"""
		
The CPU clocks that were actually used during rendering.         
		"""


	@property
	def TaskWaitingToStart(self) -> bool:
		"""
		
True if the Task is waiting to be started.         
		"""

	def Equals(self, other: Task) -> bool:
		"""
		Checks whether or not this 

		:param Task other: The 
		:return: True if the task objects are deemed to be the same, False otherwise.
		"""

	@staticmethod
	def TaskPercentToString(percent: float) -> Text:
		"""
		Convert the given percentage (usually [0..100]) to a string of the form "X %". We do this operation in a few places when we convert precentages to database-stored (and network transmitted) strings. 

		:param float percent: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Jobs import Task
class TaskCollection(IEnumerable< Task >):
	"""
	 A collection of tasks.
	"""

	@property
	def TaskCollectionAllTasks(self) -> Iterable[Task]:
		"""
		
The list of all tasks, including pre and post tasks.         
		"""


	@property
	def TaskCollectionNormalTaskCount(self) -> int:
		"""
		
Returns the total task count (NOT including pre and post tasks).         
		"""


	@property
	def TaskCollectionPostTask(self) -> Task:
		"""
		
The task responsible for running the post job script. Returns None if there is no post job script.         
		"""


	@property
	def TaskCollectionPreTask(self) -> Task:
		"""
		
The task responsible for running the pre job script. Returns None if there is no pre job script.         
		"""


	@property
	def TaskCollectionTaskCount(self) -> int:
		"""
		
Returns the total task count (including pre and post tasks).         
		"""


	@property
	def TaskCollectionTasks(self) -> Iterable[Task]:
		"""
		
The list of normal tasks.         
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class TaskProperties:
	"""
	 Task properties class.
	"""

	@property
	def TaskExtraInfo0(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo0.setter
	def TaskExtraInfo0(self, value: Text): ...


	@property
	def TaskExtraInfo1(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo1.setter
	def TaskExtraInfo1(self, value: Text): ...


	@property
	def TaskExtraInfo2(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo2.setter
	def TaskExtraInfo2(self, value: Text): ...


	@property
	def TaskExtraInfo3(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo3.setter
	def TaskExtraInfo3(self, value: Text): ...


	@property
	def TaskExtraInfo4(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo4.setter
	def TaskExtraInfo4(self, value: Text): ...


	@property
	def TaskExtraInfo5(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo5.setter
	def TaskExtraInfo5(self, value: Text): ...


	@property
	def TaskExtraInfo6(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo6.setter
	def TaskExtraInfo6(self, value: Text): ...


	@property
	def TaskExtraInfo7(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo7.setter
	def TaskExtraInfo7(self, value: Text): ...


	@property
	def TaskExtraInfo8(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo8.setter
	def TaskExtraInfo8(self, value: Text): ...


	@property
	def TaskExtraInfo9(self) -> Text:
		"""
		
One of the Task's ten Extra Info fields.         
		"""
	@TaskExtraInfo9.setter
	def TaskExtraInfo9(self, value: Text): ...

	def GetTaskExtraInfoKeys(self, ) -> Iterable[Text]:
		"""
		Gets the keys for the task's extra info entries. 

		
		:return: The keys, as a list of strings.
		"""

	def GetTaskExtraInfoKeyValue(self, key: Text) -> Text:
		"""
		Gets the extra info value for the given key. 

		:param Text key: The key.
		:return: The value, as a string. If the key isn't found, an empty string is returned.
		"""

	def GetTaskExtraInfoKeyValueWithDefault(self, key: Text, defaultValue: Text) -> Text:
		"""
		Gets the extra info value for the given key. 

		:param Text key: The key.
		:param Text defaultValue: The default value.
		:return: The value, as a string. If the key isn't found, an empty string is returned.
		"""

	def SetTaskExtraInfoKeyValue(self, key: Text, value: Text):
		"""
		Sets the extra info value for the given key. 

		:param Text key: The key.
		:param Text value: The value.
		:return: 
		"""

