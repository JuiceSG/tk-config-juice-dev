from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Balancer import BalancerInfoSettings
from Deadline.Balancer import BalancerInfo
class BalancerUtils:
	"""
	 Balancer utility functions.
	"""
	@staticmethod
	def GetMachineIPAddresses(balancerInfos: Iterable[BalancerInfo]) -> Iterable[Text]:
		"""
		Gets the list of unique machine IP Addresses from the given balancer infos. 

		:param Iterable[BalancerInfo] balancerInfos: The list of balancer infos.
		:return: The list of unique machine IP addresses.
		"""

	@staticmethod
	def GetMachineNameOrIPAddresses(balancerInfoSettings: Iterable[BalancerInfoSettings]) -> Iterable[Text]:
		"""
		Gets the list of unique machine names or IP addresses from the given balancer info settings. If a balancer has an override for the host machine or IP address that is returned, or if the network settings are set to use balancer IP addresses. Otherwise, the machine name will be returned. 

		:param Iterable[BalancerInfoSettings] balancerInfoSettings: The list of balancer info settings.
		:return: The list of unique machine names and IP addresses.
		"""

	@staticmethod
	def GetMachineNames(balancerInfos: Iterable[BalancerInfo]) -> Iterable[Text]:
		"""
		Gets the list of unique machine names from the given balancer infos. 

		:param Iterable[BalancerInfo] balancerInfos: The list of balancer infos.
		:return: The list of unique machine names.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class ClientUtils:
	"""
	 Utility functions for the Deadline client.
	"""
	@staticmethod
	def CreateScriptTempFolder():
		"""
		Creates a temp folder for deadline scripts. 

		
		:return: 
		"""

	@staticmethod
	def CreateScriptTempFolder(prefix: Text):
		"""
		Creates a temp folder for deadline scripts. 

		:param Text prefix: The prefix for the temp folder. Defaults to 'script_'.
		:return: 
		"""

	@staticmethod
	def ExecuteCommand(args: object) -> int:
		"""
		Executes a command the same way as if you were passing arguments to deadlinecommand, and returns the exit code. 

		:param object args: The arguments. This should be a list of strings.
		:return: The exit code of the command.
		"""

	@staticmethod
	def ExecuteCommandAndGetOutput(args: object) -> Text:
		"""
		Executes a command the same way as if you were passing arguments to deadlinecommand, and returns the stdout. 

		:param object args: The arguments. This should be a list of strings.
		:return: The stdout from the command.
		"""

	@staticmethod
	def ExecuteScript(scriptFilename: Text):
		"""
		Executes a command the same way as if you were calling 'deadlinecommand -ExecuteScript'. 

		:param Text scriptFilename: The script file name.
		:return: 
		"""

	@staticmethod
	def ExecuteScript(scriptFilename: Text, args: object):
		"""
		Executes a command the same way as if you were calling 'deadlinecommand -ExecuteScript', except that arguments can also be passed to the script's 

		:param Text scriptFilename: The script file name.
		:param object args: The arguments. This should be a list of strings.
		:return: 
		"""

	@staticmethod
	def GetBinDirectory() -> Text:
		"""
		Gets the client's bin directory. 

		
		:return: The client's bin directory. The default values on each OS are:
Windows: %PROGRAMFILES%\Thinkbox\Deadline[VERSION]\binLinux: /opt/Thinkbox/Deadline[VERSION]/binOS X: /Applications/Thinkbox/Deadline[VERSION]/Resources 

		"""

	@staticmethod
	def GetCurrentUserHomeDirectory() -> Text:
		"""
		Gets the client's home directory for the current user. 

		
		:return: The client's home directory. The default values on each OS are:
Windows: %LOCALAPPDATA%\Thinkbox\Deadline[VERSION]Linux: ~/Thinkbox/Deadline[VERSION]OS X: ~/Library/Application Support/Thinkbox/Deadline[VERSION] 

		"""

	@staticmethod
	def GetDeadlineMajorVersion() -> int:
		"""
		Gets the major version as an integer. 

		
		:return: The major version.
		"""

	@staticmethod
	def GetDeadlineTempPath() -> Text:
		"""
		Gets the client's temp directory. 

		
		:return: The client's temp directory. The default values on each OS are:
Windows: %LOCALAPPDATA%\Thinkbox\Deadline[VERSION]\tempLinux: ~/Thinkbox/Deadline[VERSION]/tempOS X: ~/Library/Application Support/Thinkbox/Deadline[VERSION]/temp 

		"""

	@staticmethod
	def GetDeadlineUser() -> Text:
		"""
		Gets the client's current user. 

		
		:return: The client's current user.
		"""

	@staticmethod
	def GetDeadlineVersion() -> float:
		"""
		Gets the major and minor version as a float. 

		
		:return: The major and minor version as a float.
		"""

	@staticmethod
	def GetLogDirectory() -> Text:
		"""
		Gets the client's log directory. 

		
		:return: The client's log directory. The default values on each OS are:
Windows: %PROGRAMDATA%\Thinkbox\Deadline[VERSION]\logsLinux: /var/log/Thinkbox/Deadline[VERSION]OS X: /Library/Logs/Thinkbox/Deadline[VERSION] 

		"""

	@staticmethod
	def GetMacAddress() -> Text:
		"""
		Gets MAC address. 

		
		:return: The MAC address.
		"""

	@staticmethod
	def GetUsersHomeDirectory() -> Text:
		"""
		Gets the client's home directory for all users. 

		
		:return: The client's home directory. The default values on each OS are:
Windows: %PROGRAMDATA%\Thinkbox\Deadline[VERSION]Linux: /var/lib/Thinkbox/Deadline[VERSION]OS X: /Users/Shared/Thinkbox/Deadline[VERSION] 

		"""

	@staticmethod
	def GetUsersSettingsDirectory() -> Text:
		"""
		Gets the client's settings directory. 

		
		:return: The client's settings directory. The default values on each OS are:
Windows: %LOCALAPPDATA%\Thinkbox\Deadline[VERSION]\settingsLinux: ~/Thinkbox/Deadline[VERSION]/settingsOS X: ~/Library/Application Support/Thinkbox/Deadline[VERSION]/settings 

		"""

	@staticmethod
	def LogText(line: Text):
		"""
		Logs text to the current application's log file. 

		:param Text line: The line of text.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Cloud import CloudInstance
class CloudUtils:
	"""
	 Utility functions for controlling Cloud Instances.
	"""
	@staticmethod
	def GetDataControllerWithException() -> DataController:
		"""
		Retrieves the DataController from the DeadlineApplicationManager and creates/connects it if necessary. If the DataController still cannot be obtained, an Exception is thrown. 

		
		:return: The application DataController.
		"""

	@staticmethod
	def CloneInstance(regionID: Text, instanceID: Text, count: int) -> Iterable[CloudInstance]:
		"""
		Create a new instance using the hardware type and image of the provided instance. 

		:param Text regionID: The name of the 
		:param Text instanceID: The name of the instance you want to clone.
		:param int count: The number of instances to start.
		:return: The new cloud instance.
		"""

	@staticmethod
	def CreateInstance(regionID: Text, hardwareID: Text, imageID: Text, count: int) -> CloudInstance:
		"""
		Creates an instance using the given Hardware and OS Image. 

		:param Text regionID: The name of the 
		:param Text hardwareID: The type of Hardware to requisition for this VM.
		:param Text imageID: The OS Image with which to start the VM.
		:param int count: 
		:return: The CloudInstance object representing the newly-created VM.
		"""

	@staticmethod
	def GetActiveInstances(regionID: Text) -> Iterable[CloudInstance]:
		"""
		Returns a list of active instances based from the given region. 

		:param Text regionID: The cloud region to get active instances from.
		:return: The list of active instances.
		"""

	@staticmethod
	def GetAvailableHardwareIDs(regionID: Text) -> Iterable[Text]:
		"""
		Returns a list of available Hardware types. 

		:param Text regionID: The cloud region to query for the hardware types.
		:return: The list of hardware IDs.
		"""

	@staticmethod
	def GetAvailableImageIDs(regionID: Text) -> Iterable[Text]:
		"""
		Returns a list of available Image IDs. 

		:param Text regionID: The cloud region to query for the images.
		:return: The list of image IDs.
		"""

	@staticmethod
	def GetCloudRegionNames(invalidateCache: bool) -> Iterable[Text]:
		"""
		Returns a list of all the names of cloud regions that are defined in 

		:param bool invalidateCache: 
		:return: The list of cloud region names.
		"""

	@staticmethod
	def GetCloudRegionNames(provider: Text, invalidateCache: bool) -> Iterable[Text]:
		"""
		Returns a list of all the names of cloud regions that are defined in 

		:param Text provider: The name of the Provider (cloud plugin) to search for.
		:param bool invalidateCache: If the cache should be invalidated.
		:return: The list of cloud region names.
		"""

	@staticmethod
	def GetProviderNames() -> Iterable[Text]:
		"""
		Returns a list of available provider names (cloud plugins). 

		
		:return: The list of names.
		"""

	@staticmethod
	def RebootInstance(regionID: Text, instanceID: Text):
		"""
		Reboots the given VM. 

		:param Text regionID: The cloud region on which to start this instance.
		:param Text instanceID: The ID representing the Instance to reboot.
		:return: 
		"""

	@staticmethod
	def StartInstance(regionID: Text, instanceID: Text):
		"""
		Starts the given VM if it has been stopped. 

		:param Text regionID: The cloud region on which to start this instance.
		:param Text instanceID: The ID representing the Instance to start.
		:return: 
		"""

	@staticmethod
	def StopInstance(regionID: Text, instanceID: Text):
		"""
		Shuts down the given VM. If you don't intend to keep using this VM, use Terminate instead! 

		:param Text regionID: The cloud region on which to start this instance.
		:param Text instanceID: The ID representing the Instance to stop.
		:return: 
		"""

	@staticmethod
	def TerminateInstance(regionID: Text, instanceID: Text):
		"""
		Terminates the given VM. 

		:param Text regionID: The cloud region on which to start this instance.
		:param Text instanceID: The ID representing the Instance to terminate.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class DirectoryUtils:
	"""
	 Directory utility functions.
	"""
	@staticmethod
	def AddToPath(directory: Text):
		"""
		Adds the specified directory to the PATH environment variable for this session. 

		:param Text directory: The directory.
		:return: 
		"""

	@staticmethod
	def SearchDirectoryList(directoryList: Text) -> Text:
		"""
		Searches a semicolon separated list of directories for the first one that exists. 

		:param Text directoryList: The semicolon separated list of directories.
		:return: The first directory that exists, or "" if no directory is found.
		"""

	@staticmethod
	def SearchPath(fileName: Text) -> Text:
		"""
		Searches the PATH environment variable to see if the specified filename exists in any of the paths. 

		:param Text fileName: The file name.
		:return: The full path to the file if it exists in one of the paths, or "" if it does not.
		"""

	@staticmethod
	def SynchronizeDirectories(sourceDirectory: Text, destDirectory: Text, deepCopy: bool) -> bool:
		"""
		Synchronize two directories. If the deepCopy parameter is set to True, then it will synchronize all sub-directories as well. 

		:param Text sourceDirectory: The source directory.
		:param Text destDirectory: The destination directory.
		:param bool deepCopy: If you want to perform a deep copy.
		:return: True if synchronization was required.
		"""

	@staticmethod
	def SynchronizeFiles(sourceFiles: Iterable[Text], destDirectory: Text) -> bool:
		"""
		Synchronizes a list of files with the destination directory specified. 

		:param Iterable[Text] sourceFiles: The list of files.
		:param Text destDirectory: The destination directory.
		:return: True if synchronization was required.
		"""

	@staticmethod
	def SynchronizeFiles(sourceFiles: Iterable[Text], destDirectory: Text, skipExisting: bool) -> bool:
		"""
		Synchronizes a list of files with the destination directory specified. 

		:param Iterable[Text] sourceFiles: The list of files.
		:param Text destDirectory: The destination directory.
		:param bool skipExisting: If existing files in the dest directory should just be skipped.
		:return: True if synchronization was required.
		"""

	@staticmethod
	def SynchronizeFilesAndReturnList(sourceFiles: Iterable[Text], destDirectory: Text, skipExisting: bool) -> Iterable[Text]:
		"""
		Synchronizes a list of files with the destination directory specified. 

		:param Iterable[Text] sourceFiles: The list of files.
		:param Text destDirectory: The destination directory.
		:param bool skipExisting: If existing files in the dest directory should just be skipped.
		:return: The list of files that were copied to the destination location. This will contain the destination file paths.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class FileUtils:
	"""
	 File utility functions.
	"""
	@staticmethod
	def FileExists(fileName: Text) -> bool:
		"""
		Makes three attempts to check if a file exists, with a 10ms delay between attempts. 

		:param Text fileName: The file name.
		:return: True if the file exists, or False if all three attempts fail.
		"""

	@staticmethod
	def GetExecutableVersion(fileName: Text) -> Text:
		"""
		Gets the version string of the given executable filename (Windows only). 

		:param Text fileName: The file name.
		:return: The version as a string, or "unknown" if the version could not be found.
		"""

	@staticmethod
	def GetFileSize(fileName: Text) -> long:
		"""
		Gets the size of the given file, in bytes. 

		:param Text fileName: The file name.
		:return: The file size, or -1 if it does not exist.
		"""

	@staticmethod
	def GetIniFileKeys(fileName: Text, section: Text) -> Iterable[Text]:
		"""
		Gets the keys for the specified section in the ini file. 

		:param Text fileName: The ini file name.
		:param Text section: The section the keys are in.
		:return: The list of keys for the given section.
		"""

	@staticmethod
	def GetIniFileSections(fileName: Text) -> Iterable[Text]:
		"""
		Gets the sections for the specified ini file. 

		:param Text fileName: The ini file name.
		:return: The list of sections.
		"""

	@staticmethod
	def GetIniFileSetting(fileName: Text, section: Text, key: Text, defaultValue: Text) -> Text:
		"""
		Gets the setting for the specified key in the ini file. 

		:param Text fileName: The ini file name.
		:param Text section: The section the key is in.
		:param Text key: The key name.
		:param Text defaultValue: The default value if the key doesn't exist.
		:return: The value for the given section and key, or the default value if it doesn't exist.
		"""

	@staticmethod
	def Is64BitDllOrExe(fileName: Text) -> bool:
		"""
		Checks if the specified file is a 64 bit dll or exe. 

		:param Text fileName: The file name.
		:return: True if it is 64 bit.
		"""

	@staticmethod
	def SearchFileList(fileList: Text) -> Text:
		"""
		Searches a semicolon separated list of files for the first one that exists. For relative file paths in the list, the current directory and the PATH environment variable will be searched. 

		:param Text fileList: The semicolon separated list of files.
		:return: The first file that exists, or "" if no file is found.
		"""

	@staticmethod
	def SearchFileListFor32Bit(fileList: Text) -> Text:
		"""
		Searches a semicolon separated list of files for the first 32 bit file that exists. For relative file paths in the list, the current directory and the PATH environment variable will be searched. 

		:param Text fileList: The semicolon separated list of files.
		:return: The first file that exists, or "" if no file is found.
		"""

	@staticmethod
	def SearchFileListFor64Bit(fileList: Text) -> Text:
		"""
		Searches a semicolon separated list of files for the first 64 bit file that exists. For relative file paths in the list, the current directory and the PATH environment variable will be searched. 

		:param Text fileList: The semicolon separated list of files.
		:return: The first file that exists, or "" if no file is found.
		"""

	@staticmethod
	def SetIniFileSetting(fileName: Text, section: Text, key: Text, value: Text):
		"""
		Sets the setting for the specified key in the ini file. 

		:param Text fileName: The ini file name.
		:param Text section: The section the key is in.
		:param Text key: The key name.
		:param Text value: The new value.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class FrameUtils:
	"""
	 Frame utility functions.
	"""
	@staticmethod
	def FrameRangeValid(frameString: Text) -> bool:
		"""
		Checks if a given frame string is valid. 

		:param Text frameString: The frame string.
		:return: True if the string is valid.
		"""

	@staticmethod
	def GetFilenameWithoutPadding(filename: Text) -> Text:
		"""
		Gets the file name without the frame padding. 

		:param Text filename: The file name.
		:return: The file name without frame padding.
		"""

	@staticmethod
	def GetFrameNumberFromFilename(filename: Text) -> int:
		"""
		Gets the frame number from the padding of a file name. 

		:param Text filename: The file name.
		:return: The frame number.
		"""

	@staticmethod
	def GetFrameRangeFromFilename(filename: Text) -> Text:
		"""
		Gets the frame range from a given file by figuring out the start and end frames in a sequence. 

		:param Text filename: The file name, which is part of a sequence.
		:return: The frame range formatted as [start]-[end].
		"""

	@staticmethod
	def GetFrameStringFromFilename(filename: Text) -> Text:
		"""
		Gets the frame string from the padding of a file name. 

		:param Text filename: The file name.
		:return: The frame string.
		"""

	@staticmethod
	def GetLowerFrameFilename(filename: Text, startFrame: int, paddingSize: int) -> Text:
		"""
		Finds the name of the file with the lowest frame in a sequence. 

		:param Text filename: The file name, which is part of a sequence.
		:param int startFrame: The frame to start searching from.
		:param int paddingSize: The frame padding size.
		:return: The name of the file with the lowest frame in the sequence.
		"""

	@staticmethod
	def GetLowerFrameRange(filename: Text, startFrame: int, paddingSize: int) -> int:
		"""
		Finds the lowest frame number in a sequence. 

		:param Text filename: The file name, which is part of a sequence.
		:param int startFrame: The frame to start searching from.
		:param int paddingSize: The frame padding size.
		:return: The lowest frame in the sequence.
		"""

	@staticmethod
	def GetPaddingSizeFromFilename(filename: Text) -> int:
		"""
		Gets the frame padding size of a file name. 

		:param Text filename: The file name.
		:return: The frame padding size.
		"""

	@staticmethod
	def GetUpperFrameFilename(filename: Text, startFrame: int, paddingSize: int) -> Text:
		"""
		Finds the name of the file with the highest frame in a sequence. 

		:param Text filename: The file name, which is part of a sequence.
		:param int startFrame: The frame to start searching from.
		:param int paddingSize: The frame padding size.
		:return: The name of the file with the lowest frame in the sequence.
		"""

	@staticmethod
	def GetUpperFrameRange(filename: Text, endFrame: int, paddingSize: int) -> int:
		"""
		Finds the highest frame number in a sequence. 

		:param Text filename: The file name, which is part of a sequence.
		:param int endFrame: The frame to start searching from.
		:param int paddingSize: The frame padding size.
		:return: The highest frame in the sequence.
		"""

	@staticmethod
	def Parse(frameString: Text) -> Iterable[int]:
		"""
		Converts the frame string to a frame list. The frames are automatically placed in ascending order. 

		:param Text frameString: The frame string.
		:return: A integer array containing the frames.
		"""

	@staticmethod
	def Parse(frameString: Text, reorderFrames: bool) -> Iterable[int]:
		"""
		Converts the frame string to a frame list. 

		:param Text frameString: The frame string.
		:param bool reorderFrames: If the frames should be reordered.
		:return: A integer array containing the frames.
		"""

	@staticmethod
	def ReplaceFrameNumberWithPadding(filename: Text, padChar: char) -> Text:
		"""
		Returns a file name with the frame number replaced with padding. 

		:param Text filename: The file name.
		:param char padChar: The padding character to use.
		:return: The modified file name.
		"""

	@staticmethod
	def ReplaceFrameNumberWithPrintFPadding(filename: Text) -> Text:
		"""
		Returns a file name with the frame number replaced with printf style padding (ie: %04d). 

		:param Text filename: The file name.
		:return: The modified file name.
		"""

	@staticmethod
	def ReplacePaddingWithFrameNumber(filename: Text, frameNumber: int) -> Text:
		"""
		Returns a file name with the padding replaced with the specified frame number. 

		:param Text filename: The file name.
		:param int frameNumber: The frame number.
		:return: The modified file name.
		"""

	@staticmethod
	def RequiredPaddingSize(frame: int) -> int:
		"""
		Gets the minimum padding size required for the frame. 

		:param int frame: The frame.
		:return: The number of characters needed to pad the file.
		"""

	@staticmethod
	def SubstituteFrameNumber(filename: Text, frame: Text) -> Text:
		"""
		Substitutes the frame in the file name. 

		:param Text filename: The file name.
		:param Text frame: The frame.
		:return: The name of the file with the new frame.
		"""

	@staticmethod
	def ToChunks(framesList: Iterable[int], chunkSize: int) -> Iterable[Iterable[int]]:
		"""
		Converts the frame list into chunks. 

		:param Iterable[int] framesList: The frame list.
		:param int chunkSize: The size of the chunks.
		:return: A two-dimensional integer array of chunks. Each "chunk" is an array of frames.
		"""

	@staticmethod
	def ToFrameString(frameList: Iterable[int]) -> Text:
		"""
		Converts the frame list to a frame string. 

		:param Iterable[int] frameList: The list of frames.
		:return: The frame string.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Jobs import TaskCollection
from Deadline.Jobs import Job
from Deadline.Jobs import AssetDependency
from Deadline.Statistics import JobEntry
class JobUtils:
	"""
	 Job utility functions.
	"""
	@staticmethod
	def CalculateJobStatistics(job: Job, taskCollection: TaskCollection) -> JobEntry:
		"""
		Creates a new job entry object from the given job and tasks. You can then get specific stats from the job entry. 

		:param Job job: The job.
		:param TaskCollection taskCollection: The job's task collection.
		:return: A job statistics entry.
		"""

	@staticmethod
	def TestDependencies(jobID: Text) -> bool:
		"""
		Test non-frame dependent Job. 

		:param Text jobID: The job ID.
		:return: 
		"""

	@staticmethod
	def TestDependentAsset(jobID: Text, asset: Text) -> bool:
		"""
		Test non-frame dependent asset. 

		:param Text jobID: The job ID.
		:param Text asset: The path to the asset.
		:return: 
		"""

	@staticmethod
	def TestDependentJob(jobID: Text, dependentID: Text) -> bool:
		"""
		Test non-frame dependent Job. 

		:param Text jobID: The job ID.
		:param Text dependentID: The ID of the dependent job to test.
		:return: 
		"""

	@staticmethod
	def TestDependentScript(jobID: Text, script: Text) -> bool:
		"""
		Test non-frame dependent script. 

		:param Text jobID: The job ID.
		:param Text script: The script to test.
		:return: 
		"""

	@staticmethod
	def TestFrameDependencies(jobID: Text) -> Iterable[int]:
		"""
		Test non-frame dependent Job. 

		:param Text jobID: The job ID.
		:return: 
		"""

	@staticmethod
	def TestFrameDependencies(jobID: Text, taskIDs: Iterable[int]) -> Iterable[int]:
		"""
		Test non-frame dependent Job. 

		:param Text jobID: 
		:param Iterable[int] taskIDs: The ids to test, if null test all.
		:return: 
		"""

	@staticmethod
	def TestFrameDependentAsset(jobID: Text, asset: AssetDependency) -> Iterable[int]:
		"""
		Test frame dependent asset. 

		:param Text jobID: The job ID.
		:param AssetDependency asset: The asset to test.
		:return: 
		"""

	@staticmethod
	def TestFrameDependentAsset(jobID: Text, asset: AssetDependency, taskIDs: Iterable[int]) -> Iterable[int]:
		"""
		Test frame dependent asset. 

		:param Text jobID: The job ID.
		:param AssetDependency asset: The asset to test.
		:param Iterable[int] taskIDs: The IDs of the tasks to test, if null test all tasks.
		:return: 
		"""

	@staticmethod
	def TestFrameDependentJob(jobID: Text, dependentID: Text) -> Iterable[int]:
		"""
		Test frame dependent Job. 

		:param Text jobID: The job ID.
		:param Text dependentID: The ID of the dependent job to test.
		:return: 
		"""

	@staticmethod
	def TestFrameDependentJob(jobID: Text, dependentID: Text, taskIDs: Iterable[int]) -> Iterable[int]:
		"""
		Test frame dependent Job. 

		:param Text jobID: The job ID.
		:param Text dependentID: The ID of the dependent job to test.
		:param Iterable[int] taskIDs: The ids to test, if null test all.
		:return: 
		"""

	@staticmethod
	def TestFrameDependentScript(jobID: Text, script: Text) -> Iterable[int]:
		"""
		Test frame dependent script. 

		:param Text jobID: The job ID.
		:param Text script: The script to test.
		:return: 
		"""

	@staticmethod
	def TestFrameDependentScript(jobID: Text, script: Text, taskIDs: Iterable[int]) -> Iterable[int]:
		"""
		Test frame dependent script. 

		:param Text jobID: The job ID.
		:param Text script: The script to test.
		:param Iterable[int] taskIDs: The IDs of the tasks to test, if null test all tasks.
		:return: 
		"""

	@staticmethod
	def GetMonitorManagerFor(func: Text) -> MonitorManager:
		"""
		Returns the MonitorManager if it exists and throws an Exception if not. This is meant to be used by 

		:param Text func: 
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Slaves import SlaveInfoSettings
from Deadline.Reports import Report
from Deadline.Pulses import PulseSettings
from Deadline.Balancer import BalancerSettings
from Deadline.Slaves import SlaveSettings
from Deadline.Jobs import Job
from Deadline.Balancer import BalancerInfo
from Deadline.Pulses import PulseInfoSettings
from Deadline.Jobs import Task
from Deadline.Balancer import BalancerInfoSettings
from Deadline.Pulses import PulseInfo
from Deadline.LimitGroups import LimitGroup
from Deadline.Slaves import SlaveInfo
class MonitorUtils:
	"""
	 Utility functions for scripts run from the Monitor.
	"""
	@staticmethod
	def GetSelectedBalancerInfos() -> Iterable[BalancerInfo]:
		"""
		Gets the list of selected balancer infos in the Monitor. 

		
		:return: The list of balancer infos.
		"""

	@staticmethod
	def GetSelectedBalancerInfoSettings() -> Iterable[BalancerInfoSettings]:
		"""
		Gets the list of selected balancer info settings in the Monitor. 

		
		:return: The list of balancer infos.
		"""

	@staticmethod
	def GetSelectedBalancerNames() -> Iterable[Text]:
		"""
		Gets the list of selected balancer names in the Monitor. 

		
		:return: The list of balancer names.
		"""

	@staticmethod
	def GetSelectedBalancerSettings() -> Iterable[BalancerSettings]:
		"""
		Gets the list of selected balancer settings in the Monitor. 

		
		:return: The list of balancer infos.
		"""

	@staticmethod
	def GetSelectedJobIds() -> Iterable[Text]:
		"""
		Gets the list of selected job IDs in the Monitor. 

		
		:return: The list of job IDs.
		"""

	@staticmethod
	def GetSelectedJobReports() -> Iterable[Report]:
		"""
		Gets the list of selected job reports in the Monitor. 

		
		:return: The list of reports.
		"""

	@staticmethod
	def GetSelectedJobs() -> Iterable[Job]:
		"""
		Gets the list of selected jobs in the Monitor. 

		
		:return: The list of jobs.
		"""

	@staticmethod
	def GetSelectedLimitGroupNames() -> Iterable[Text]:
		"""
		Gets the list of selected limit group names in the Monitor. 

		
		:return: The list of limit group names.
		"""

	@staticmethod
	def GetSelectedLimitGroups() -> Iterable[LimitGroup]:
		"""
		Gets the list of selected limit groups in the Monitor. 

		
		:return: The list of limit groups.
		"""

	@staticmethod
	def GetSelectedPulseInfos() -> Iterable[PulseInfo]:
		"""
		Gets the list of selected pulse infos in the Monitor. 

		
		:return: The list of pulse infos.
		"""

	@staticmethod
	def GetSelectedPulseInfoSettings() -> Iterable[PulseInfoSettings]:
		"""
		Gets the list of selected pulse info settings in the Monitor. 

		
		:return: The list of pulse infos.
		"""

	@staticmethod
	def GetSelectedPulseNames() -> Iterable[Text]:
		"""
		Gets the list of selected pulse names in the Monitor. 

		
		:return: The list of pulse names.
		"""

	@staticmethod
	def GetSelectedPulseSettings() -> Iterable[PulseSettings]:
		"""
		Gets the list of selected pulse settings in the Monitor. 

		
		:return: The list of pulse infos.
		"""

	@staticmethod
	def GetSelectedSlaveInfos() -> Iterable[SlaveInfo]:
		"""
		Gets the list of selected Worker infos in the Monitor. 

		
		:return: The list of Worker infos.
		"""

	@staticmethod
	def GetSelectedSlaveInfoSettings() -> Iterable[SlaveInfoSettings]:
		"""
		Gets the list of selected Worker infos and settings in the Monitor. 

		
		:return: The list of Worker info settings.
		"""

	@staticmethod
	def GetSelectedSlaveNames() -> Iterable[Text]:
		"""
		Gets the list of selected Worker names in the Monitor. 

		
		:return: The list of Worker names.
		"""

	@staticmethod
	def GetSelectedSlaveReports() -> Iterable[Report]:
		"""
		Gets the list of selected Worker reports in the Monitor. 

		
		:return: The list of reports.
		"""

	@staticmethod
	def GetSelectedSlaveSettings() -> Iterable[SlaveSettings]:
		"""
		Gets the list of selected Worker settings in the Monitor. 

		
		:return: The list of Worker settings.
		"""

	@staticmethod
	def GetSelectedTasks() -> Iterable[Task]:
		"""
		Gets the list of selected tasks in the Monitor. 

		
		:return: The list of tasks.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class PathUtils:
	"""
	 Path utility functions.
	"""
	@staticmethod
	def ChangeFilename(path: Text, filename: Text) -> Text:
		"""
		Changes the file name in the path. 

		:param Text path: The original path, filename included.
		:param Text filename: The new file name.
		:return: The new path.
		"""

	@staticmethod
	def EnsureTrailingPathSeparator(path: Text) -> Text:
		"""
		Ensures the given path ends with the appropriate path separator for the current operating system. 

		:param Text path: The path.
		:return: The path with a trailing path separator.
		"""

	@staticmethod
	def GetApplicationPath(applicationName: Text) -> Text:
		"""
		Searches the PATH environment variable to see if the specified application exists in any of the paths. 

		:param Text applicationName: The application name.
		:return: The full path to the application if it exists, or "" if it doesn't.
		"""

	@staticmethod
	def GetFullNetworkPath(filePath: Text) -> Text:
		"""
		Returns the full Network Path of the given file by expanding mapped Network Drives to their full network Path, if applicable. 

		:param Text filePath: The File Path containing a Mapped Drive.
		:return: The expanded network path if applicable, or the unchanged filePath if it isn't a valid network path.
		"""

	@staticmethod
	def GetLocalApplicationDataPath() -> Text:
		"""
		Gets the local appliation data path for the current non-roaming user. 

		
		:return: The local application data path.
		"""

	@staticmethod
	def GetMappedDriveNetworkPath(driveName: Text) -> Text:
		"""
		Gets the network path for the given drive. 

		:param Text driveName: The drive.
		:return: The corresponding network path, or "" if the drive isn't mapped.
		"""

	@staticmethod
	def GetSystemTempPath() -> Text:
		"""
		Returns the path of the current system's temporary folder. 

		
		:return: The temporary folder.
		"""

	@staticmethod
	def IsDriveMapped(driveName: Text) -> bool:
		"""
		Checks if the given drive is mapped. 

		:param Text driveName: The drive.
		:return: True if it is mapped.
		"""

	@staticmethod
	def IsPathLocal(fileName: Text) -> bool:
		"""
		Simply checks if the root of the path is the C, D, or E drive. 

		:param Text fileName: The file name.
		:return: True if the file is on the C, D, or E drive.
		"""

	@staticmethod
	def IsPathLocal(fileName: Text, root: Text) -> bool:
		"""
		Check if the root of the given file matches the given root. 

		:param Text fileName: The file name.
		:param Text root: The root to check.
		:return: True if the root of the given file matches the given root.
		"""

	@staticmethod
	def IsPathLocal(fileName: Text, roots: Iterable[Text]) -> bool:
		"""
		Check if the root of the given file matches any of the roots in the given array. 

		:param Text fileName: The file name.
		:param Iterable[Text] roots: The roots to check.
		:return: True if the root of the given file matches any of the given roots.
		"""

	@staticmethod
	def IsPathRooted(path: Text) -> bool:
		"""
		Checks if the given path is rooted or relative. 

		:param Text path: The path.
		:return: True if the path is rooted.
		"""

	@staticmethod
	def IsPathUNC(path: Text) -> bool:
		"""
		Checks if the given path is a UNC path. 

		:param Text path: The path.
		:return: True if the path is UNC.
		"""

	@staticmethod
	def MapNetworkPath(driveName: Text, remotePath: Text, username: Text, password: Text, force: bool) -> bool:
		"""
		Maps a network path. 

		:param Text driveName: The drive.
		:param Text remotePath: The remote path.
		:param Text username: The username, can be null.
		:param Text password: The password, can be null.
		:param bool force: If an existing mapped path to the local path should be disconnected first.
		:return: Returns True if successful.
		"""

	@staticmethod
	def RegisterFont(fontFileName: Text, timeoutMilliseconds: int) -> bool:
		"""
		Registers the given font (Windows only). 

		:param Text fontFileName: The font file name.
		:param int timeoutMilliseconds: The number of milliseconds to wait per font when registering fonts.
		:return: True if successful.
		"""

	@staticmethod
	def RegisterFont(fontFileName: Text) -> bool:
		"""
		Registers the given font (Windows only). 

		:param Text fontFileName: The font file name.
		:return: True if successful.
		"""

	@staticmethod
	def RegisterFonts(fontFileNames: Iterable[Text], timeoutMilliseconds: int) -> bool:
		"""
		Registers the given fonts (Windows only). 

		:param Iterable[Text] fontFileNames: The font file names.
		:param int timeoutMilliseconds: The number of milliseconds to wait per font when registering fonts.
		:return: True if successful.
		"""

	@staticmethod
	def RegisterFonts(fontFileNames: Iterable[Text]) -> bool:
		"""
		Registers the given fonts (Windows only). 

		:param Iterable[Text] fontFileNames: The font file names.
		:return: True if successful.
		"""

	@staticmethod
	def ToPlatformIndependentPath(path: Text) -> Text:
		"""
		Replaces all path separators in the given path with the separators for the current operating system. 

		:param Text path: The path.
		:return: The path with updated path separators.
		"""

	@staticmethod
	def ToShortPathName(path: Text) -> Text:
		"""
		Converts the given path to it's equivalent short path (Windows only). 

		:param Text path: The path.
		:return: A short representation of the path.
		"""

	@staticmethod
	def UnmapNetworkPath(driveName: Text, force: bool) -> bool:
		"""
		Unmaps a network drive. 

		:param Text driveName: The drive.
		:param bool force: Specifies whether the disconnection should occur if there are open files or jobs on the connection. If this parameter is FALSE, the function fails if there are open files or jobs.
		:return: Returns True if successful.
		"""

	@staticmethod
	def UnregisterFont(fontFileName: Text) -> bool:
		"""
		Unregisters the given font (Windows only). 

		:param Text fontFileName: The font file name.
		:return: True if successful.
		"""

	@staticmethod
	def UnregisterFont(fontFileName: Text, timeoutMilliseconds: int) -> bool:
		"""
		Unregisters the given font (Windows only). 

		:param Text fontFileName: The font file name.
		:param int timeoutMilliseconds: The number of milliseconds to wait per font when registering fonts.
		:return: True if successful.
		"""

	@staticmethod
	def UnregisterFonts(fontFileNames: Iterable[Text]) -> bool:
		"""
		Unregisters the given fonts (Windows only). 

		:param Iterable[Text] fontFileNames: The font file names.
		:return: True if successful.
		"""

	@staticmethod
	def UnregisterFonts(fontFileNames: Iterable[Text], timeoutMilliseconds: int) -> bool:
		"""
		Unregisters the given fonts (Windows only). 

		:param Iterable[Text] fontFileNames: The font file names.
		:param int timeoutMilliseconds: The number of milliseconds to wait per font when registering fonts.
		:return: True if successful.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class ProcessUtils:
	"""
	 Process utility functions.
	"""
	@staticmethod
	def IsProcessRunning(name: Text) -> bool:
		"""
		Checks if a process is running. 

		:param Text name: The process name.
		:return: True if the process is running.
		"""

	@staticmethod
	def KillParentAndChildProcesses(parentId: int):
		"""
		Kill the parent process and all of its child processes. 

		:param int parentId: The parent process' ID.
		:return: 
		"""

	@staticmethod
	def KillProcesses(name: Text) -> bool:
		"""
		Kills all processes with the given name. 

		:param Text name: The process name.
		:return: True if any processes were found and killed.
		"""

	@staticmethod
	def KillProcesses(name: Text, attempts: int) -> bool:
		"""
		Attempts to kill all processes with the given name a specified number of times. 

		:param Text name: The process name.
		:param int attempts: The number of attempts before we give up.
		:return: 
		"""

	@staticmethod
	def ShellExecute(filename: Text) -> Process:
		"""
		Shell executes the specified file. 

		:param Text filename: The file name.
		:return: The process object.
		"""

	@staticmethod
	def ShellExecute(filename: Text, verb: Text) -> Process:
		"""
		Shell executes the specified file using the specified verb. 

		:param Text filename: The file name.
		:param Text verb: The verb (ie: explore). Specify null to omit the verb.
		:return: The process object.
		"""

	@staticmethod
	def SpawnProcess(executable: Text) -> Process:
		"""
		Spawns a process. 

		:param Text executable: The executable file name.
		:return: The process object.
		"""

	@staticmethod
	def SpawnProcess(executable: Text, arguments: Text) -> Process:
		"""
		Spawns a process. 

		:param Text executable: The executable file name.
		:param Text arguments: The arguments.
		:return: The process object.
		"""

	@staticmethod
	def SpawnProcess(executable: Text, arguments: Text, workingDirectory: Text) -> Process:
		"""
		Spawns a process. 

		:param Text executable: The executable file name.
		:param Text arguments: The arguments.
		:param Text workingDirectory: The working directory.
		:return: The process object.
		"""

	@staticmethod
	def SpawnProcess(executable: Text, arguments: Text, workingDirectory: Text, windowStyle: ProcessWindowStyle) -> Process:
		"""
		Spawns a process. 

		:param Text executable: The executable file name.
		:param Text arguments: The arguments.
		:param Text workingDirectory: The working directory.
		:param ProcessWindowStyle windowStyle: The window style.
		:return: The process object.
		"""

	@staticmethod
	def SpawnProcess(executable: Text, arguments: Text, workingDirectory: Text, windowStyle: ProcessWindowStyle, redirectStdOutput: bool) -> Process:
		"""
		Spawns a process. 

		:param Text executable: The executable file name.
		:param Text arguments: The arguments.
		:param Text workingDirectory: The working directory.
		:param ProcessWindowStyle windowStyle: The window style.
		:param bool redirectStdOutput: If standard output should be redirected.
		:return: The process object.
		"""

	@staticmethod
	def WaitForExit(process: Process, timeoutMilliseconds: int) -> bool:
		"""
		Waits for a process to exit. 

		:param Process process: The process object.
		:param int timeoutMilliseconds: The timeout in milliseconds. Specify -1 to wait until the process exits.
		:return: True if the process exits before the timeout.
		"""

	@staticmethod
	def WaitForProcessToStart(name: Text, timeoutMilliseconds: int) -> bool:
		"""
		Waits for a process with the given name to start. 

		:param Text name: The process name.
		:param int timeoutMilliseconds: The timeout in milliseconds. Specify -1 for no timeout.
		:return: True if the process started before the timeout.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Pulses import PulseInfo
from Deadline.Pulses import PulseInfoSettings
class PulseUtils:
	"""
	 Pulse utility functions.
	"""
	@staticmethod
	def GetCachedUserNames() -> Iterable[Text]:
		"""
		Gets the user names. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of user names.
		"""

	@staticmethod
	def GetJobTasks(jobId: Text) -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for the tasks belonging to the given job. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		:param Text jobId: The job ID.
		:return: The list of property dictionaries, or null if the job isn't cached.
		"""

	@staticmethod
	def GetLastPulseRefreshTime() -> Text:
		"""
		Gets the repository date time. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The time in the format MM/dd/yyyy HH:mm:ss.
		"""

	@staticmethod
	def GetMachineIPAddresses(pulseInfos: Iterable[PulseInfo]) -> Iterable[Text]:
		"""
		Gets the list of unique machine IP Addresses from the given pulse infos. 

		:param Iterable[PulseInfo] pulseInfos: The list of pulse infos.
		:return: The list of unique machine IP addresses.
		"""

	@staticmethod
	def GetMachineNameOrIPAddresses(pulseInfoSettings: Iterable[PulseInfoSettings]) -> Iterable[Text]:
		"""
		Gets the list of unique machine names or IP addresses from the given pulse info settings. If a pulse has an override for the host machine or IP address that is returned, or if the network settings are set to use pulse IP addresses. Otherwise, the machine name will be returned. 

		:param Iterable[PulseInfoSettings] pulseInfoSettings: The list of pulse info settings.
		:return: The list of unique machine names and IP addresses.
		"""

	@staticmethod
	def GetMachineNames(pulseInfos: Iterable[PulseInfo]) -> Iterable[Text]:
		"""
		Gets the list of unique machine names from the given pulse infos. 

		:param Iterable[PulseInfo] pulseInfos: The list of pulse infos.
		:return: The list of unique machine names.
		"""

	@staticmethod
	def GetPulseGroupNames() -> Iterable[Text]:
		"""
		Gets the list of group names. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of group names.
		"""

	@staticmethod
	def GetPulseJobIds() -> Iterable[Text]:
		"""
		Gets the job IDs. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of job IDs.
		"""

	@staticmethod
	def GetPulseJobInfo(jobID: Text) -> Dict[Text,Text]:
		"""
		Gets a dictionary of properties for a job. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		:param Text jobID: The ID of the job to retrieve.
		:return: The job's properties, or null if the job isn't cached.
		"""

	@staticmethod
	def GetPulseJobs() -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for all jobs. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of dictionaries.
		"""

	@staticmethod
	def GetPulseLimitGroupInfo(limitGroupName: Text) -> Dict[Text,Text]:
		"""
		Gets a dictionary of properties for a limit group. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		:param Text limitGroupName: The name of the limit group to retrieve.
		:return: The limit group's properties, or null if the limit group isn't cached.
		"""

	@staticmethod
	def GetPulseLimitGroupNames() -> Iterable[Text]:
		"""
		Gets the limit group names. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of limit group names.
		"""

	@staticmethod
	def GetPulseLimitGroups() -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for all limit groups. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of dictionaries.
		"""

	@staticmethod
	def GetPulseMacAddress() -> Text:
		"""
		Gets pulse's MAC address. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The MAC address.
		"""

	@staticmethod
	def GetPulsePoolNames() -> Iterable[Text]:
		"""
		Gets the list of pool names. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of pool names.
		"""

	@staticmethod
	def GetPulseSlaveInfo(slaveName: Text) -> Dict[Text,Text]:
		"""
		Gets a dictionary of properties for a Worker. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		:param Text slaveName: The name of the Worker to retrieve.
		:return: The Worker's properties, or null if the Worker isn't cached.
		"""

	@staticmethod
	def GetPulseSlaveNames() -> Iterable[Text]:
		"""
		Gets the Worker names. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of Worker names.
		"""

	@staticmethod
	def GetPulseSlaves() -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for all Workers. For Web Service scripts only. DEPRECATED: This function is only left here for backwards compatibility. call 

		
		:return: The list of dictionaries.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class RegionHealthStatus:
	"""
	 Class containing the health status for AWS resources in a region.
	"""

	@property
	def message(self) -> Text:
		"""
		
Message indicating reason for unhealthy status if unhealthy.         
		"""
	@message.setter
	def message(self, value: Text): ...


	@property
	def status(self) -> bool:
		"""
		
Status of the fleet health in this region.         
		"""
	@status.setter
	def status(self, value: bool): ...

	def __init__(self, status: bool, message: Text):
		"""
		Constructor. 

		:param bool status: Health status for the region.
		:param Text message: Health status message.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Slaves import SlaveInfoSettings
from Deadline.Reports import Report
from Deadline.Pulses import PulseSettings
from Deadline.Reports import JobReportCollection
from Deadline.Balancer import BalancerSettings
from Deadline.Slaves import SlaveSettings
from Deadline.Plugins import PluginConfig
from Deadline.Jobs import Job
from Deadline.Balancer import BalancerInfo
from Deadline.Scripting import RegionHealthStatus
from Deadline.Reports import SlaveReportCollection
from Deadline.Pulses import PulseInfoSettings
from Deadline.Jobs import Task
from Deadline.Pulses import PulseInfo
from Deadline.Balancer import BalancerInfoSettings
from Deadline.LimitGroups import LimitGroup
from Deadline.Slaves import SlaveInfo
from Deadline.Jobs import TaskCollection
from Deadline.PowerMgmt import PowerManagementOptions
class RepositoryUtils:
	"""
	 Repository utility functions.
	"""
	@staticmethod
	def GetDataControllerWithException() -> DataController:
		"""
		Retrieves the DataController from the DeadlineApplicationManager and creates/connects it if necessary. If the DataController still cannot be obtained, an Exception is thrown. 

		
		:return: The application DataController.
		"""

	@staticmethod
	def AddAuxiliaryFile(job: Job, newAuxFilePath: Iterable[Text]):
		"""
		Adds an aux file to the specified job. 

		:param Job job: The job.
		:param Iterable[Text] newAuxFilePath: An auxiliary data file name. This should be the full path including the file name to a data file.
		:return: 
		"""

	@staticmethod
	def AddBadSlaveForJob(job: Job, slaveName: Text):
		"""
		Adds a Worker to a job's Bad Worker list. 

		:param Job job: The job.
		:param Text slaveName: The name of the Worker to add to the list.
		:return: 
		"""

	@staticmethod
	def AddGroup(groupName: Text):
		"""
		Adds a group to the repository. 

		:param Text groupName: The group name.
		:return: 
		"""

	@staticmethod
	def AddGroupToSlave(slaveName: Text, groupName: Text):
		"""
		Adds a group to the given Worker. 

		:param Text slaveName: The Worker name.
		:param Text groupName: The group name.
		:return: 
		"""

	@staticmethod
	def AddJobHistoryEntry(jobId: Text, entry: Text):
		"""
		Adds a job history entry. 

		:param Text jobId: The job's ID.
		:param Text entry: The history text.
		:return: 
		"""

	@staticmethod
	def AddPool(poolName: Text):
		"""
		Adds a pool to the repository. 

		:param Text poolName: The pool name.
		:return: 
		"""

	@staticmethod
	def AddPoolToSlave(slaveName: Text, poolName: Text):
		"""
		Adds a pool to the given Worker. 

		:param Text slaveName: The Worker name.
		:param Text poolName: The pool name.
		:return: 
		"""

	@staticmethod
	def AddRepositoryHistoryEntry(entry: Text):
		"""
		Adds a repository history entry. 

		:param Text entry: The history text.
		:return: 
		"""

	@staticmethod
	def AddSlaveHistoryEntry(slaveName: Text, entry: Text):
		"""
		Adds a Worker history entry. 

		:param Text slaveName: The Worker name.
		:param Text entry: The history text.
		:return: 
		"""

	@staticmethod
	def AddSlavesToLimitGroupList(name: Text, slaveNames: object):
		"""
		Adds Workers to a limit group's list of Workers. 

		:param Text name: The limit group name.
		:param object slaveNames: The list of Workers to add.
		:return: 
		"""

	@staticmethod
	def AddSlavesToMachineLimitList(jobId: Text, slaveNames: object):
		"""
		Adds Workers to a job machine limit's list of Workers. 

		:param Text jobId: The job ID.
		:param object slaveNames: The list of Workers to add.
		:return: 
		"""

	@staticmethod
	def AddUsersToUserGroups(users: Iterable[Text], userGroups: Iterable[Text]):
		"""
		Adds all the users given to the provided user groups. 

		:param Iterable[Text] users: The users to add.
		:param Iterable[Text] userGroups: The user groups to add to.
		:return: 
		"""

	@staticmethod
	def AppendJobFrameRange(job: Job, frameList: Text):
		"""
		Appends to a job's frame range without affecting the existing tasks. The only exception is if the job's chunk size is greater than one, and the last task is having frames appended to it. 

		:param Job job: The job.
		:param Text frameList: The additional frames to append.
		:return: 
		"""

	@staticmethod
	def ArchiveJob(job: Job, deleteFromDB: bool, archiveFolderOverride: Text):
		"""
		Archive a non-queued, non-rendering job. 

		:param Job job: The job to archive.
		:param bool deleteFromDB: If True, the job will be deleted from the repository after it is archived.
		:param Text archiveFolderOverride: If not null, the archived job will be placed in this folder instead of the jobsArchived folder in the repository.
		:return: 
		"""

	@staticmethod
	def BalancerExists(balancerName: Text) -> bool:
		"""
		Checks whether or not a 

		:param Text balancerName: The balancer name to check.
		:return: Whether or not the Balancer exists.
		"""

	@staticmethod
	def CheckPathMapping(path: Text) -> Text:
		"""
		Performs path mapping on the given path. Uses the path mappings in the Repository Options. 

		:param Text path: The path.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMapping(path: Text, forceSeparator: Text) -> Text:
		"""
		Performs path mapping on the given path. Uses the path mappings in the Repository Options. 

		:param Text path: The path.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMapping(path: Text, verbose: bool) -> Text:
		"""
		Performs path mapping on the given path. Uses the path mappings in the Repository Options. 

		:param Text path: The path.
		:param bool verbose: If verbose logging should be enabled.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMapping(path: Text, forceSeparator: Text, verbose: bool) -> Text:
		"""
		Performs path mapping on the given path. Uses the path mappings in the Repository Options. 

		:param Text path: The path.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:param bool verbose: If verbose logging should be enabled.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMappingForMultiplePaths(paths: Iterable[Text]) -> Iterable[Text]:
		"""
		Performs path mapping on the given paths. Uses the path mappings in the Repository Options. 

		:param Iterable[Text] paths: The paths.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMappingForMultiplePaths(paths: Iterable[Text], forceSeparator: Text) -> Iterable[Text]:
		"""
		Performs path mapping on the given paths. Uses the path mappings in the Repository Options. 

		:param Iterable[Text] paths: The paths.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMappingForMultiplePaths(paths: Iterable[Text], verbose: bool) -> Iterable[Text]:
		"""
		Performs path mapping on the given paths. Uses the path mappings in the Repository Options. 

		:param Iterable[Text] paths: The paths.
		:param bool verbose: If verbose logging should be enabled.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMappingForMultiplePaths(paths: Iterable[Text], forceSeparator: Text, verbose: bool) -> Iterable[Text]:
		"""
		Performs path mapping on the given paths. Uses the path mappings in the Repository Options. 

		:param Iterable[Text] paths: The paths.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:param bool verbose: If verbose logging should be enabled.
		:return: The resulting path.
		"""

	@staticmethod
	def CheckPathMappingInFile(inFileName: Text, outFileName: Text):
		"""
		Performs path mapping on the contents of the given file. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFile(inFileName: Text, outFileName: Text, readFileAsBytes: bool):
		"""
		Performs path mapping on the contents of the given file. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param bool readFileAsBytes: If set to True, the input file will be processed byte-by-byte. However, this is known to have issues with UTF16 or UTF32 encoded files.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFile(inFileName: Text, outFileName: Text, forceSeparator: Text):
		"""
		Performs path mapping on the contents of the given file. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFile(inFileName: Text, outFileName: Text, forceSeparator: Text, readFileAsBytes: bool):
		"""
		Performs path mapping on the contents of the given file. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:param bool readFileAsBytes: If set to True, the input file will be processed byte-by-byte. However, this is known to have issues with UTF16 ro UTF32 encoded files.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplace(inFileName: Text, outFileName: Text, stringsToReplace: Iterable[Text], newStrings: Iterable[Text]):
		"""
		Performs path mapping on the contents of the given file, and replaces a list of given strings in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Iterable[Text] stringsToReplace: The list of strings to replace.
		:param Iterable[Text] newStrings: The list of new strings. Must be the same number of strings as stringsToReplace.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplace(inFileName: Text, outFileName: Text, stringsToReplace: Iterable[Text], newStrings: Iterable[Text], readFileAsBytes: bool):
		"""
		Performs path mapping on the contents of the given file, and replaces a list of given strings in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Iterable[Text] stringsToReplace: The list of strings to replace.
		:param Iterable[Text] newStrings: The list of new strings. Must be the same number of strings as stringsToReplace.
		:param bool readFileAsBytes: If set to True, the input file will be processed byte-by-byte. However, this is known to have issues with UTF16 or UTF32 encoded files.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplace(inFileName: Text, outFileName: Text, forceSeparator: Text, stringsToReplace: Iterable[Text], newStrings: Iterable[Text]):
		"""
		Performs path mapping on the contents of the given file, and replaces a list of given strings in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:param Iterable[Text] stringsToReplace: The list of strings to replace.
		:param Iterable[Text] newStrings: The list of new strings. Must be the same number of strings as stringsToReplace.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplace(inFileName: Text, outFileName: Text, forceSeparator: Text, stringsToReplace: Iterable[Text], newStrings: Iterable[Text], readFileAsBytes: bool):
		"""
		Performs path mapping on the contents of the given file, and replaces a list of given strings in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:param Iterable[Text] stringsToReplace: The list of strings to replace.
		:param Iterable[Text] newStrings: The list of new strings. Must be the same number of strings as stringsToReplace.
		:param bool readFileAsBytes: If set to True, the input file will be processed byte-by-byte. However, this is known to have issues with UTF16 ro UTF32 encoded files.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplaceSeparator(inFileName: Text, outFileName: Text, separatorToReplace: Text, newSeparator: Text):
		"""
		Performs path mapping on the contents of the given file, and updates all path separators in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text separatorToReplace: The path separator to replace.
		:param Text newSeparator: The new path separator.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplaceSeparator(inFileName: Text, outFileName: Text, separatorToReplace: Text, newSeparator: Text, readFileAsBytes: bool):
		"""
		Performs path mapping on the contents of the given file, and updates all path separators in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text separatorToReplace: The path separator to replace.
		:param Text newSeparator: The new path separator.
		:param bool readFileAsBytes: If set to True, the input file will be processed byte-by-byte. However, this is known to have issues with UTF16 or UTF32 encoded files.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplaceSeparator(inFileName: Text, outFileName: Text, forceSeparator: Text, separatorToReplace: Text, newSeparator: Text):
		"""
		Performs path mapping on the contents of the given file, and updates all path separators in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:param Text separatorToReplace: The path separator to replace.
		:param Text newSeparator: The new path separator.
		:return: 
		"""

	@staticmethod
	def CheckPathMappingInFileAndReplaceSeparator(inFileName: Text, outFileName: Text, forceSeparator: Text, separatorToReplace: Text, newSeparator: Text, readFileAsBytes: bool):
		"""
		Performs path mapping on the contents of the given file, and updates all path separators in any paths that are mapped. Uses the path mappings in the Repository Options. 

		:param Text inFileName: The original file name.
		:param Text outFileName: The new file name where the mapped contents will be stored.
		:param Text forceSeparator: All path separators in the replacement path will be replaced with this before the original path is mapped. For example, if this is set to "/", and "/mnt/server/" is being replaced with "Y:\", the resulting path will contain "Y:/" instead of the original "Y:\". If set to null, this will be ignored.
		:param Text separatorToReplace: The path separator to replace.
		:param Text newSeparator: The new path separator.
		:param bool readFileAsBytes: If set to True, the input file will be processed byte-by-byte. However, this is known to have issues with UTF16 ro UTF32 encoded files.
		:return: 
		"""

	@staticmethod
	def CompleteJob(job: Job):
		"""
		Completes a job. All incomplete tasks for the job will be marked as complete. 

		:param Job job: The job to complete.
		:return: 
		"""

	@staticmethod
	def CompleteTasks(job: Job, tasks: Iterable[Task], slaveName: Text) -> bool:
		"""
		Complete tasks for a job. 

		:param Job job: The job.
		:param Iterable[Task] tasks: The list of tasks to complete.
		:param Text slaveName: This is the Worker that will show up as completing the tasks.
		:return: Returns True if the job is now complete.
		"""

	@staticmethod
	def CreateAWSResourceTracker(awsRegion: Text, awsProfile: Text, accessKey: Text, secretKey: Text, sessionToken: Text):
		"""
		The 

		:param Text awsRegion: AWS Region.
		:param Text awsProfile: AWS Profile Name.
		:param Text accessKey: AWS Access Key.
		:param Text secretKey: AWS Secret Access Key.
		:param Text sessionToken: AWS Session Token.
		:return: 
		"""

	@staticmethod
	def CreateJobSubmissionFiles(job: Job, jobInfoFileName: Text, pluginInfoFileName: Text):
		"""
		Creates the job info and plugin info files that were originally used to submit the given job. 

		:param Job job: The job.
		:param Text jobInfoFileName: The file name where the job info settings will be saved.
		:param Text pluginInfoFileName: The file name where the plugin info settings will be saved.
		:return: 
		"""

	@staticmethod
	def DeleteAllBadSlavesForJob(job: Job):
		"""
		Deletes all Workers from a job's Bad Worker list. 

		:param Job job: The job.
		:return: 
		"""

	@staticmethod
	def DeleteAllJobReports(jobId: Text):
		"""
		Deletes all reports for a job. 

		:param Text jobId: The job's ID.
		:return: 
		"""

	@staticmethod
	def DeleteAllSlaveReports(slaveName: Text):
		"""
		Deletes all reports for a Worker. 

		:param Text slaveName: The Worker's name.
		:return: 
		"""

	@staticmethod
	def DeleteAWSResourceTracker(awsRegion: Text, awsProfile: Text, accessKey: Text, secretKey: Text, sessionToken: Text):
		"""
		Deletes the 

		:param Text awsRegion: AWS Region.
		:param Text awsProfile: AWS Profile Name.
		:param Text accessKey: AWS Access Key.
		:param Text secretKey: AWS Secret Access Key.
		:param Text sessionToken: AWS Session Token.
		:return: 
		"""

	@staticmethod
	def DeleteBadSlaveForJob(job: Job, slaveName: Text):
		"""
		Deletes a Worker from a job's Bad Worker list. 

		:param Job job: The job.
		:param Text slaveName: The name of the Worker to remove from the list.
		:return: 
		"""

	@staticmethod
	def DeleteBadSlavesForJob(job: Job, slaveNames: object):
		"""
		Deletes a list of Workers from a job's Bad Worker list. 

		:param Job job: The job.
		:param object slaveNames: The list of Worker names to remove from the list.
		:return: 
		"""

	@staticmethod
	def DeleteBalancer(balancerName: Text):
		"""
		Deletes a specified 

		:param Text balancerName: The balancer name.
		:return: 
		"""

	@staticmethod
	def DeleteGroup(groupName: Text):
		"""
		Removes a group from the repository. 

		:param Text groupName: The group name.
		:return: 
		"""

	@staticmethod
	def DeleteJob(job: Job):
		"""
		Delete a job. 

		:param Job job: The job to delete.
		:return: 
		"""

	@staticmethod
	def DeleteJobReport(jobId: Text, report: Report):
		"""
		Deletes the given report for a job. 

		:param Text jobId: The job's ID.
		:param Report report: The report to delete.
		:return: 
		"""

	@staticmethod
	def DeleteJobReports(jobId: Text, reports: Iterable[Report]):
		"""
		Deletes the given reports for a job. 

		:param Text jobId: The job's ID.
		:param Iterable[Report] reports: The reports to delete.
		:return: 
		"""

	@staticmethod
	def DeletePool(poolName: Text):
		"""
		Removes a pool from the repository. 

		:param Text poolName: The pool name.
		:return: 
		"""

	@staticmethod
	def DeletePostJobScript(job: Job):
		"""
		Deletes the jobs post job script. 

		:param Job job: The job.
		:return: 
		"""

	@staticmethod
	def DeletePreJobScript(job: Job):
		"""
		Deletes the jobs pre job script. 

		:param Job job: The job.
		:return: 
		"""

	@staticmethod
	def DeleteProxyServer(proxyName: Text):
		"""
		Delete the specified Remote Connection Server. 

		:param Text proxyName: The Remote Connection Server name.
		:return: 
		"""

	@staticmethod
	def DeletePulse(pulseName: Text):
		"""
		Delete the specified pulse. 

		:param Text pulseName: The pulse name.
		:return: 
		"""

	@staticmethod
	def DeleteSlave(slaveName: Text):
		"""
		Deletes a specified Worker. 

		:param Text slaveName: The Worker name.
		:return: 
		"""

	@staticmethod
	def DeleteSlaveReport(slaveName: Text, report: Report):
		"""
		Deletes the given report for a Worker. 

		:param Text slaveName: The Worker's name.
		:param Report report: The report to delete.
		:return: 
		"""

	@staticmethod
	def DeleteSlaveReports(slaveName: Text, reports: Iterable[Report]):
		"""
		Deletes the given reports for a Worker. 

		:param Text slaveName: The Worker's name.
		:param Iterable[Report] reports: The reports to delete.
		:return: 
		"""

	@staticmethod
	def DeleteUserGroup(userGroupName: Text):
		"""
		Deletes a user groups. 

		:param Text userGroupName: The user group name to delete.
		:return: 
		"""

	@staticmethod
	def DescribeAWSResourceTrackerStatus(awsRegion: Text, awsProfile: Text, accessKey: Text, secretKey: Text, sessionToken: Text) -> Text:
		"""
		Checks the status of the 

		:param Text awsRegion: AWS Region.
		:param Text awsProfile: AWS Profile Name.
		:param Text accessKey: AWS Access Key.
		:param Text secretKey: AWS Secret Access Key.
		:param Text sessionToken: AWS Session Token.
		:return: String representation of the stack status.
		"""

	@staticmethod
	def DescribeRegionHealth(region: Text, awsProfile: Text, awsAccessKeyId: Text, awsSecretAccessKey: Text, awsSessionToken: Text) -> RegionHealthStatus:
		"""
		Fetch Fleet health data from AWS(DynamoDB) and update it in the repository if allowed and return it to the caller. Credentials provisioning chain: 

		:param Text region: AWS Region for the Fleets to fetch and update the health for.
		:param Text awsProfile: AWS profile with the authentication params.
		:param Text awsAccessKeyId: AWS access key ID.
		:param Text awsSecretAccessKey: AWS secret access key.
		:param Text awsSessionToken: AWS session token that must be provided if using AWS temporary security credentials with AWS STS.
		:return: 
		"""

	@staticmethod
	def FailJob(job: Job):
		"""
		Fails a job. All incomplete tasks for the job will be marked as failed. 

		:param Job job: The job to fail.
		:return: 
		"""

	@staticmethod
	def FailTasks(job: Job, tasks: Iterable[Task]) -> bool:
		"""
		Changes the given list of Tasks to the Failed status. 

		:param Job job: The Job to which the Tasks belong.
		:param Iterable[Task] tasks: The list of tasks to fail.
		:return: True if failing the Tasks resulted in the Job being failed. False otherwise.
		"""

	@staticmethod
	def FailTasks(job: Job, tasks: Iterable[Task], slaveName: Text) -> bool:
		"""
		Changes the given list of Tasks to the Failed status. 

		:param Job job: The Job to which the Tasks belong.
		:param Iterable[Task] tasks: The list of tasks to fail.
		:param Text slaveName: The name of the Worker to list as having failed the Tasks.
		:return: True if failing the Tasks resulted in the Job being failed. False otherwise.
		"""

	@staticmethod
	def GetAlternateAuxiliaryPath() -> Text:
		"""
		Gets the alternate auxiliary file directory based on the current operating system. 

		
		:return: The auxiliary directory.
		"""

	@staticmethod
	def GetAPISyncFolder() -> Text:
		"""
		Gets the pythonsync folder. 

		
		:return: The pythonsync folder.
		"""

	@staticmethod
	def GetAWSPortalFleetRequest(requestId: Text) -> DashFleetRequest:
		"""
		Returns a DashFleetRequest with the given id. 

		:param Text requestId: 
		:return: 
		"""

	@staticmethod
	def GetAWSPortalFleetRequests() -> Iterable[DashFleetRequest]:
		"""
		Returns all the AWS Portal Spot Fleet Requests. 

		
		:return: 
		"""

	@staticmethod
	def GetAWSPortalFleetRequests(requestIds: Iterable[Text]) -> Iterable[DashFleetRequest]:
		"""
		Returns the requested set of AWS Portal Spot Fleet Requests. 

		:param Iterable[Text] requestIds: 
		:return: 
		"""

	@staticmethod
	def GetAWSPortalInfrastructures() -> Iterable[AWSPortalInfrastructure]:
		"""
		Returns all the DAWS infrastructure objects. 

		
		:return: 
		"""

	@staticmethod
	def GetAWSPortalInstance(instanceId: Text) -> DashFleetInstance:
		"""
		Returns the DashFleetInstance with the given instance id. 

		:param Text instanceId: 
		:return: 
		"""

	@staticmethod
	def GetAWSPortalInstances() -> Iterable[DashFleetInstance]:
		"""
		Returns all the AWS Portal Instance objects. 

		
		:return: 
		"""

	@staticmethod
	def GetAWSPortalInstances(instanceIds: Iterable[Text]) -> Iterable[DashFleetInstance]:
		"""
		Returns a set of DashFleetInstances with the given ids. 

		:param Iterable[Text] instanceIds: 
		:return: 
		"""

	@staticmethod
	def GetAWSPortalRequestTypeEnumName(value: int) -> Text:
		"""
		Returns the string representation of the AWSPortalRequestType enum for the given value. 

		:param int value: 
		:return: 
		"""

	@staticmethod
	def GetAWSPortalRequestTypeEnumValue(name: Text) -> int:
		"""
		Returns the int representation of the AWSPortalRequestType enum with the string matching 'name'. 

		:param Text name: 
		:return: 
		"""

	@staticmethod
	def GetAWSPortalSettings() -> AWSPortalSettings:
		"""
		Gets the DAWS settings. 

		
		:return: 
		"""

	@staticmethod
	def GetBalancerInfo(balancerName: Text, invalidateCache: bool) -> BalancerInfo:
		"""
		Gets a balancer info. 

		:param Text balancerName: The balancer name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The balancer info.
		"""

	@staticmethod
	def GetBalancerInfos(invalidateCache: bool) -> Iterable[BalancerInfo]:
		"""
		Gets all the balancer infos. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of balancer infos.
		"""

	@staticmethod
	def GetBalancerInfos(balancerNames: Iterable[Text], invalidateCache: bool) -> Iterable[BalancerInfo]:
		"""
		Gets a list of balancer infos. 

		:param Iterable[Text] balancerNames: The list of balancer names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of balancer infos.
		"""

	@staticmethod
	def GetBalancerInfoSettings(invalidateCache: bool) -> Iterable[BalancerInfoSettings]:
		"""
		Gets all the balancer info settings. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of balancer info settings.
		"""

	@staticmethod
	def GetBalancerInfoSettings(balancerNames: Iterable[Text], invalidateCache: bool) -> Iterable[BalancerInfoSettings]:
		"""
		Gets a list of balancer info settings. 

		:param Iterable[Text] balancerNames: The list of balancer names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of balancer info settings.
		"""

	@staticmethod
	def GetBalancerNames(invalidateCache: bool) -> Iterable[Text]:
		"""
		Gets all the balancer names. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of balancer names.
		"""

	@staticmethod
	def GetBalancerSettings(balancerName: Text, invalidateCache: bool) -> BalancerSettings:
		"""
		Gets settings for a balancer. 

		:param Text balancerName: The balancer name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The balancer settings.
		"""

	@staticmethod
	def GetBalancerSettingsList(invalidateCache: bool) -> Iterable[BalancerSettings]:
		"""
		Gets all the balancer settings. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of balancer settings.
		"""

	@staticmethod
	def GetBalancerSettingsList(balancerNames: Iterable[Text], invalidateCache: bool) -> Iterable[BalancerSettings]:
		"""
		Gets a list of balancer settings. 

		:param Iterable[Text] balancerNames: The list of balancer names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of balancer settings.
		"""

	@staticmethod
	def GetBinDirectory() -> Text:
		"""
		Gets the repository bin directory. 

		
		:return: The bin directory.
		"""

	@staticmethod
	def GetCloudPluginsDirectory() -> Text:
		"""
		Gets the repository cloud plugins directory. 

		
		:return: The cloud plugins directory.
		"""

	@staticmethod
	def GetCustomEventsDirectory() -> Text:
		"""
		Gets the repository custom events directory. 

		
		:return: The custom events directory.
		"""

	@staticmethod
	def GetCustomPluginsDirectory() -> Text:
		"""
		Gets the repository custom plugins directory. 

		
		:return: The custom plugins directory.
		"""

	@staticmethod
	def GetCustomScriptsDirectory() -> Text:
		"""
		Gets the repository custom scripts directory. 

		
		:return: The custom scripts directory.
		"""

	@staticmethod
	def GetDatabaseConnectionString() -> Text:
		"""
		Gets the database connection string in the form of (server:port,server:port...). If there is only one server configured, it will be in the form of (server:port). 

		
		:return: The database connection string.
		"""

	@staticmethod
	def GetDeletedJob(jobId: Text) -> Job:
		"""
		Gets a deleted job. 

		:param Text jobId: The deleted job ID.
		:return: The deleted job.
		"""

	@staticmethod
	def GetDeletedJobIds() -> Iterable[Text]:
		"""
		Gets all the deleted job IDs. 

		
		:return: The list of deleted job IDs.
		"""

	@staticmethod
	def GetDeletedJobs() -> Iterable[Job]:
		"""
		Gets all the deleted jobs. 

		
		:return: The list of deleted jobs.
		"""

	@staticmethod
	def GetEventPluginConfig(eventPluginName: Text) -> PluginConfig:
		"""
		Gets the configuration settings for an event plugin. 

		:param Text eventPluginName: The event plugin name.
		:return: The event plugin configuration.
		"""

	@staticmethod
	def GetEventPluginConfigMetaDataDictionary(eventPluginName: Text) -> Dict[Text,Text]:
		"""
		Get the metadata dictionary from the PluginConfigSettings for the given eventPluginName. 

		:param Text eventPluginName: The event plugin name.
		:return: The metadata dictionary for the given plugin.
		"""

	@staticmethod
	def GetEventPluginDirectory(eventPluginName: Text) -> Text:
		"""
		Returns the directory in which the given event plugin is located. 

		:param Text eventPluginName: The name of the event plugin to look for.
		:return: The event plugin directory.
		"""

	@staticmethod
	def GetEventPluginNames() -> Iterable[Text]:
		"""
		Gets the event plugin names. 

		
		:return: The list of event plugin names.
		"""

	@staticmethod
	def GetEventsDirectory() -> Text:
		"""
		Gets the repository events directory. 

		
		:return: The events directory.
		"""

	@staticmethod
	def GetGroupNames() -> Iterable[Text]:
		"""
		Gets the group names. 

		
		:return: The list of group names.
		"""

	@staticmethod
	def GetJob(jobId: Text, invalidate: bool) -> Job:
		"""
		Gets a job. 

		:param Text jobId: The job ID.
		:param bool invalidate: Specify True to update the cache, or False to use the data currently cached.
		:return: The job.
		"""

	@staticmethod
	def GetJobAuxiliaryPath(job: Job) -> Text:
		"""
		Gets the auxiliary file directory for the given job. 

		:param Job job: The job.
		:return: The auxiliary directory.
		"""

	@staticmethod
	def GetJobDetails(jobs: Iterable[Job]) -> Dict[Text,Dict[Text,Dict[Text,Text]]]:
		"""
		Gets a dictionary of job details for the provided jobs. 

		:param Iterable[Job] jobs: The list of jobs.
		:return: A dictionary containing the job details.
		"""

	@staticmethod
	def GetJobIds(invalidateCache: bool) -> Iterable[Text]:
		"""
		Gets all the job IDs. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of IDs.
		"""

	@staticmethod
	def GetJobIds() -> Iterable[Text]:
		"""
		Gets the job IDs. For Web Service scripts only. 

		
		:return: The list of job IDs.
		"""

	@staticmethod
	def GetJobReportLog(report: Report) -> Text:
		"""
		Gets the report log for a job report. 

		:param Report report: The report.
		:return: The report log.
		"""

	@staticmethod
	def GetJobReportLogFileName(report: Report) -> Text:
		"""
		Gets the full path to the report log file for a job report. Note that the file is a bzip file. 

		:param Report report: The report.
		:return: The report log file name. This will be an empty string if there was an error saving the report to the Repository.
		"""

	@staticmethod
	def GetJobReports(jobId: Text) -> JobReportCollection:
		"""
		Gets the reports for a job. 

		:param Text jobId: The job ID.
		:return: The collection of reports.
		"""

	@staticmethod
	def GetJobs(invalidateCache: bool) -> Iterable[Job]:
		"""
		Gets all the jobs. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of jobs.
		"""

	@staticmethod
	def GetJobs(jobIds: Iterable[Text], invalidate: bool) -> Iterable[Job]:
		"""
		Gets a list of jobs. 

		:param Iterable[Text] jobIds: The list of job IDs.
		:param bool invalidate: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of jobs.
		"""

	@staticmethod
	def GetJobsInState(states: object) -> Iterable[Job]:
		"""
		Gets all the jobs in the given state(s). 

		:param object states: A list of job states, or a string containing a single state. Valid states are Active, Suspended, Completed, Failed, and Pending. Note that Active covers both Queued and Rendering jobs.
		:return: The list of jobs in the given state(s).
		"""

	@staticmethod
	def GetJobTaskLimit() -> int:
		"""
		Gets the job task limit. 

		
		:return: The job task limit.
		"""

	@staticmethod
	def GetJobTasks(job: Job, invalidate: bool) -> TaskCollection:
		"""
		Gets the tasks for a job. 

		:param Job job: The job.
		:param bool invalidate: Specify True to update the cache, or False to use the data currently cached.
		:return: The job's task collection.
		"""

	@staticmethod
	def GetLimitGroup(limitGroupName: Text, invalidate: bool) -> LimitGroup:
		"""
		Gets a limit group. 

		:param Text limitGroupName: The limit group name.
		:param bool invalidate: Specify True to update the cache, or False to use the data currently cached.
		:return: The limit group.
		"""

	@staticmethod
	def GetLimitGroupNames(invalidateCache: bool) -> Iterable[Text]:
		"""
		Gets all the limit group names. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of user group names.
		"""

	@staticmethod
	def GetLimitGroups(limitGroupNames: Iterable[Text], invalidate: bool) -> Iterable[LimitGroup]:
		"""
		Gets a list of limit groups. 

		:param Iterable[Text] limitGroupNames: The list of limit group names.
		:param bool invalidate: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of limit groups.
		"""

	@staticmethod
	def GetLimitGroups(invalidate: bool) -> Iterable[LimitGroup]:
		"""
		Gets all the limit groups. 

		:param bool invalidate: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of limit groups.
		"""

	@staticmethod
	def GetLinuxAlternateAuxiliaryPath() -> Text:
		"""
		Gets the alternate auxiliary file directory for Linux. 

		
		:return: The auxiliary directory.
		"""

	@staticmethod
	def GetMacAlternateAuxiliaryPath() -> Text:
		"""
		Gets the alternate auxiliary file directory for Mac OSX. 

		
		:return: The auxiliary directory.
		"""

	@staticmethod
	def GetMachineLimit(jobId: Text, invalidate: bool) -> LimitGroup:
		"""
		Gets the machine limit for a job. 

		:param Text jobId: The job ID.
		:param bool invalidate: Specify True to update the cache, or False to use the data currently cached.
		:return: The machine limit, which is just a specialized limit group.
		"""

	@staticmethod
	def GetMachinesRenderingJob(jobId: Text, ipAddresses: bool) -> Iterable[Text]:
		"""
		Gets the host names of the machines rendering the specified job. 

		:param Text jobId: The job ID.
		:param bool ipAddresses: If True, the machine IP addresses will be returned instead of the host names.
		:return: The list of machines.
		"""

	@staticmethod
	def GetMachinesRenderingJob(jobId: Text, ipAddresses: bool, duplicates: bool) -> Iterable[Text]:
		"""
		Gets the host names of the machines rendering the specified job. 

		:param Text jobId: The job ID.
		:param bool ipAddresses: If True, the machine IP addresses will be returned instead of the host names.
		:param bool duplicates: If True, duplicate IP addresses and hostnames will be returned.
		:return: The list of machines.
		"""

	@staticmethod
	def GetMaximumPriority() -> int:
		"""
		Gets the maximum job priority. 

		
		:return: The maximum job priority.
		"""

	@staticmethod
	def GetNetworkSettings() -> IDeadlineNetworkSettings:
		"""
		Gets the network settings. 

		
		:return: The network settings.
		"""

	@staticmethod
	def GetPathMappings() -> Iterable[Iterable[Text]]:
		"""
		Gets the list of relevant path mappings as defined in Repository Options. 

		
		:return: List of [from] -> [to] path mappings relevant to the current operating system.
		"""

	@staticmethod
	def GetPluginConfig(pluginName: Text) -> PluginConfig:
		"""
		Gets the configuration settings for a plugin. 

		:param Text pluginName: The plugin name.
		:return: The plugin configuration.
		"""

	@staticmethod
	def GetPluginConfig(pluginName: Text, altCustomPluginDirectory: Text) -> PluginConfig:
		"""
		Gets the configuration settings for a plugin. 

		:param Text pluginName: The plugin name.
		:param Text altCustomPluginDirectory: A custom directory to get the plugin config from.
		:return: The plugin configuration.
		"""

	@staticmethod
	def GetPluginDirectory(pluginName: Text) -> Text:
		"""
		Returns the directory in which the given plugin is located. 

		:param Text pluginName: The name of the plugin to look for.
		:return: The directory for the plugin.
		"""

	@staticmethod
	def GetPluginLimitGroups(pluginName: Text) -> Iterable[Text]:
		"""
		Retrieve PluginConfigSettings.LimitNames for a specified 

		:param Text pluginName: Name of a 
		:return: Returns array containing the names of limit groups assigned to a Plugin.
		"""

	@staticmethod
	def GetPluginNames() -> Iterable[Text]:
		"""
		Gets the plugin names. 

		
		:return: The list of plugin names.
		"""

	@staticmethod
	def GetPluginsDirectory() -> Text:
		"""
		Gets the repository plugins directory. 

		
		:return: The plugins directory.
		"""

	@staticmethod
	def GetPoolNames() -> Iterable[Text]:
		"""
		Gets the pool names. 

		
		:return: The list of pool names.
		"""

	@staticmethod
	def GetPowerManagementOptions() -> PowerManagementOptions:
		"""
		Gets the power management options. 

		
		:return: The power management options.
		"""

	@staticmethod
	def GetProxyServerInfo(proxyName: Text, invalidateCache: bool) -> ProxyServerInfo:
		"""
		Gets ProxyServerInfo for a specified Remote Connection Server. 

		:param Text proxyName: The Remote Connection Server name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The requested ProxyServerInfo.
		"""

	@staticmethod
	def GetProxyServerInfos(invalidateCache: bool) -> Iterable[ProxyServerInfo]:
		"""
		Gets ProxyServerInfo objects for all Remote Connection Servers. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of ProxyServerInfo objects.
		"""

	@staticmethod
	def GetProxyServerInfos(proxyNames: Iterable[Text], invalidateCache: bool) -> Iterable[ProxyServerInfo]:
		"""
		Gets ProxyServerInfo objects for all specified Remote Connection Servers. 

		:param Iterable[Text] proxyNames: The list of Remote Connection Server names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse infos.
		"""

	@staticmethod
	def GetProxyServerInfoSettings(invalidateCache: bool) -> Iterable[ProxyServerInfoSettings]:
		"""
		Gets ProxyServerInfoSettings objects for all Remote Connection Servers. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of ProxyServerInfoSettings.
		"""

	@staticmethod
	def GetProxyServerInfoSettings(proxyNames: Iterable[Text], invalidateCache: bool) -> Iterable[ProxyServerInfoSettings]:
		"""
		Gets ProxyServerInfoSettings objects for all specified Remote Connection Servers. 

		:param Iterable[Text] proxyNames: The list of Remote Connection Server names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of ProxyServerInfoSettings.
		"""

	@staticmethod
	def GetProxyServerNames(invalidateCache: bool) -> Iterable[Text]:
		"""
		Gets all the Remote Connection Server names. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of Remote Connection Server names.
		"""

	@staticmethod
	def GetProxyServerSettings(proxyName: Text, invalidateCache: bool) -> ProxyServerSettings:
		"""
		Gets ProxyServerSettings for a specified Remote Connection Server. 

		:param Text proxyName: Name of the Remote Connection Server.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The requested ProxyServerSettings.
		"""

	@staticmethod
	def GetProxyServerSettingsList(invalidateCache: bool) -> Iterable[ProxyServerSettings]:
		"""
		Gets ProxyServerSettings objects for all Remote Connection Servers. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of ProxyServerSettings objects.
		"""

	@staticmethod
	def GetProxyServerSettingsList(proxyNames: Iterable[Text], invalidateCache: bool) -> Iterable[ProxyServerSettings]:
		"""
		Gets ProxyServerSettings objects for all specified Remote Connection Servers. 

		:param Iterable[Text] proxyNames: The list of Remote Connection Server names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of ProxyServerSettings.
		"""

	@staticmethod
	def GetPulseInfo(pulseName: Text, invalidateCache: bool) -> PulseInfo:
		"""
		Gets a pulse info. 

		:param Text pulseName: The pulse name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The pulse info.
		"""

	@staticmethod
	def GetPulseInfos(invalidateCache: bool) -> Iterable[PulseInfo]:
		"""
		Gets all the pulse infos. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse infos.
		"""

	@staticmethod
	def GetPulseInfos(pulseNames: Iterable[Text], invalidateCache: bool) -> Iterable[PulseInfo]:
		"""
		Gets a list of pulse infos. 

		:param Iterable[Text] pulseNames: The list of pulse names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse infos.
		"""

	@staticmethod
	def GetPulseInfoSettings(invalidateCache: bool) -> Iterable[PulseInfoSettings]:
		"""
		Gets all the pulse info settings. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse info settings.
		"""

	@staticmethod
	def GetPulseInfoSettings(pulseNames: Iterable[Text], invalidateCache: bool) -> Iterable[PulseInfoSettings]:
		"""
		Gets a list of pulse info settings. 

		:param Iterable[Text] pulseNames: The list of pulse names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse info settings.
		"""

	@staticmethod
	def GetPulseNames(invalidateCache: bool) -> Iterable[Text]:
		"""
		Gets all the pulse names. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse names.
		"""

	@staticmethod
	def GetPulseSettings(pulseName: Text, invalidateCache: bool) -> PulseSettings:
		"""
		Gets settings for a pulse. 

		:param Text pulseName: The pulse name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The pulse settings.
		"""

	@staticmethod
	def GetPulseSettingsList(invalidateCache: bool) -> Iterable[PulseSettings]:
		"""
		Gets all the pulse settings. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse settings.
		"""

	@staticmethod
	def GetPulseSettingsList(pulseNames: Iterable[Text], invalidateCache: bool) -> Iterable[PulseSettings]:
		"""
		Gets a list of pulse settings. 

		:param Iterable[Text] pulseNames: The list of pulse names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of pulse settings.
		"""

	@staticmethod
	def GetRegionNameFromId(regionName: Text) -> Text:
		"""
		Gets the name of the Region or 

		:param Text regionName: The region ID.
		:return: The region name, or an empty string if the region ID does not exist.
		"""

	@staticmethod
	def GetRepositoryDateTime() -> DateTime:
		"""
		Gets the current Repository DateTime. 

		
		:return: The DateTime.
		"""

	@staticmethod
	def GetRepositoryFilePath(filePath: Text, checkCustom: bool) -> Text:
		"""
		Returns the appropriate full path to the given file in the Repository. 

		:param Text filePath: The repository's file to retrieve.
		:param bool checkCustom: Whether or not to check the Custom folder first.
		:return: The path to the given file.
		"""

	@staticmethod
	def GetRepositoryPath(subFolder: Text, checkCustom: bool) -> Text:
		"""
		Returns the appropriate full path to the given subdirectory of the Repository. 

		:param Text subFolder: The repository's sub-directory to retrieve.
		:param bool checkCustom: Whether or not to check the Custom folder first.
		:return: The root directory for the given subfolder.
		"""

	@staticmethod
	def GetRootDirectory() -> Text:
		"""
		Gets the repository root directory. 

		
		:return: The root directory.
		"""

	@staticmethod
	def GetRootDirectory(subFolder: Text) -> Text:
		"""
		Gets the repository root directory with sync arguments. 

		:param Text subFolder: The subfolder to get the directory path for.
		:return: The root directory for the given subfolder.
		"""

	@staticmethod
	def GetScriptsDirectory() -> Text:
		"""
		Gets the repository scripts directory. 

		
		:return: The scripts directory.
		"""

	@staticmethod
	def GetSettingsDirectory() -> Text:
		"""
		Gets the repository settings directory. 

		
		:return: The settings directory.
		"""

	@staticmethod
	def GetSlaveInfo(slaveName: Text, invalidateCache: bool) -> SlaveInfo:
		"""
		Gets a Worker info. 

		:param Text slaveName: The Worker name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The Worker info.
		"""

	@staticmethod
	def GetSlaveInfos(invalidateCache: bool) -> Iterable[SlaveInfo]:
		"""
		Gets all the Worker infos. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of Worker infos.
		"""

	@staticmethod
	def GetSlaveInfos(slaveNames: Iterable[Text], invalidateCache: bool) -> Iterable[SlaveInfo]:
		"""
		Gets a list of Worker infos. 

		:param Iterable[Text] slaveNames: The list of Worker names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of Worker infos.
		"""

	@staticmethod
	def GetSlaveInfoSettings(invalidateCache: bool) -> Iterable[SlaveInfoSettings]:
		"""
		Gets all the Worker info settings. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of Worker info settings.
		"""

	@staticmethod
	def GetSlaveInfoSettings(slaveNames: Iterable[Text], invalidateCache: bool) -> Iterable[SlaveInfoSettings]:
		"""
		Gets a list of Worker info settings. 

		:param Iterable[Text] slaveNames: The list of Worker names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of Worker info settings.
		"""

	@staticmethod
	def GetSlaveNames(invalidateCache: bool) -> Iterable[Text]:
		"""
		Gets all the Worker names. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of slave names.
		"""

	@staticmethod
	def GetSlaveReportLog(report: Report) -> Text:
		"""
		Gets the log for a Worker report. 

		:param Report report: The report.
		:return: The log.
		"""

	@staticmethod
	def GetSlaveReportLogFileName(report: Report) -> Text:
		"""
		Gets the full path to the report log file for a Worker report. Note that the file is a bzip file. 

		:param Report report: The report.
		:return: The report log file name. This will be an empty string if there was an error saving the report to the Repository.
		"""

	@staticmethod
	def GetSlaveReports(slaveName: Text) -> SlaveReportCollection:
		"""
		Gets the reports for a Worker. 

		:param Text slaveName: The Worker name.
		:return: The collection of reports.
		"""

	@staticmethod
	def GetSlaveSettings(slaveName: Text, invalidateCache: bool) -> SlaveSettings:
		"""
		Gets settings for a Worker. 

		:param Text slaveName: The Worker name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The Worker settings.
		"""

	@staticmethod
	def GetSlaveSettingsList(invalidateCache: bool) -> Iterable[SlaveSettings]:
		"""
		Gets all the Worker settings. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of Worker settings.
		"""

	@staticmethod
	def GetSlaveSettingsList(slaveNames: Iterable[Text], invalidateCache: bool) -> Iterable[SlaveSettings]:
		"""
		Gets a list of Worker settings. 

		:param Iterable[Text] slaveNames: The list of Worker names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of Worker settings.
		"""

	@staticmethod
	def GetSlavesRenderingJob(jobId: Text) -> Iterable[Text]:
		"""
		Gets the names of the Workers rendering the specified job. 

		:param Text jobId: The job ID.
		:return: The list of Workers.
		"""

	@staticmethod
	def GetSlaveStatusEnumName(value: int) -> Text:
		"""
		Gets the string representation of the SlaveStatus enum for the given value. 

		:param int value: 
		:return: 
		"""

	@staticmethod
	def GetSlaveStatusEnumValue(name: Text) -> int:
		"""
		Returns the int representation of the SlaveStatus enum with the string matching 'name'. 

		:param Text name: 
		:return: 
		"""

	@staticmethod
	def GetUserGroup(userGroupName: Text) -> Iterable[Text]:
		"""
		Gets the users for the user group with the given name. 

		:param Text userGroupName: The user group to get the user for.
		:return: A list of user names for that user group.
		"""

	@staticmethod
	def GetUserGroupNames() -> Iterable[Text]:
		"""
		Gets all the user group names. 

		
		:return: The list of user group names.
		"""

	@staticmethod
	def GetUserGroupsForUser(user: Text) -> Iterable[Text]:
		"""
		Get the user group names for the provided user. 

		:param Text user: The user to get the user group names for.
		:return: The user groups the user belongs to.
		"""

	@staticmethod
	def GetUserInfo(userName: Text, invalidateCache: bool) -> IUserInfo:
		"""
		Gets a user's info. 

		:param Text userName: The user name.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The user info.
		"""

	@staticmethod
	def GetUserInfos(invalidateCache: bool) -> Iterable[IUserInfo]:
		"""
		Gets all the user infos. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of user infos.
		"""

	@staticmethod
	def GetUserInfos(userNames: Iterable[Text], invalidateCache: bool) -> Iterable[IUserInfo]:
		"""
		Gets a list of user infos. 

		:param Iterable[Text] userNames: The list of user names.
		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of user infos.
		"""

	@staticmethod
	def GetUserNames(invalidateCache: bool) -> Iterable[Text]:
		"""
		Gets all the user names. 

		:param bool invalidateCache: Specify True to update the cache, or False to use the data currently cached.
		:return: The list of user names.
		"""

	@staticmethod
	def GetWindowsAlternateAuxiliaryPath() -> Text:
		"""
		Gets the alternate auxiliary file directory for Windows. 

		
		:return: The auxiliary directory.
		"""

	@staticmethod
	def ImportJob(archivedJobFile: Text, deleteArchive: bool) -> Job:
		"""
		Imports an archived job and returns it. 

		:param Text archivedJobFile: The path to the archived job file.
		:param bool deleteArchive: If True, the archived file will be deleted after the job is imported.
		:return: The imported job.
		"""

	@staticmethod
	def JobExists(jobId: Text) -> bool:
		"""
		Checks if a job exists. 

		:param Text jobId: The job ID.
		:return: True if the job exists.
		"""

	@staticmethod
	def NewUserGroup(userGroupName: Text):
		"""
		Creates a new user group with the given name if it does not already exist. 

		:param Text userGroupName: The user group name to create.
		:return: 
		"""

	@staticmethod
	def NewUserGroups(userGroupNames: Iterable[Text]):
		"""
		Creates new user groups with the given names if they do not already exist. 

		:param Iterable[Text] userGroupNames: The user group names to create.
		:return: 
		"""

	@staticmethod
	def PathMappingRequired(path: Text) -> bool:
		"""
		Checks if the given path matches a path mapping setting in the Repository Options. 

		:param Text path: The path.
		:return: If path mapping is required for this path.
		"""

	@staticmethod
	def PendJob(job: Job):
		"""
		Place a job with dependencies in the pending state. 

		:param Job job: The job to pend.
		:return: 
		"""

	@staticmethod
	def PendTasks(job: Job, tasks: Iterable[Task]) -> bool:
		"""
		Pends tasks for a job. This is only supported if the job is frame dependent. 

		:param Job job: The job.
		:param Iterable[Task] tasks: The list of tasks to pend.
		:return: Returns True if the job is now in the pending state.
		"""

	@staticmethod
	def ProxyServerExists(proxyName: Text) -> bool:
		"""
		Checks if a specified Remote Connection Server exists. 

		:param Text proxyName: The Remote Connection Server name to check.
		:return: True if the Remote Connection Server exists, false otherwise.
		"""

	@staticmethod
	def PulseExists(pulseName: Text) -> bool:
		"""
		Checks whether or not a Pulse with the given name exists. 

		:param Text pulseName: The pulse name to check.
		:return: Whether or not the Pulse exists.
		"""

	@staticmethod
	def PurgeDeletedJobs(jobID: Text):
		"""
		Purge deleted job. 

		:param Text jobID: The deleted job ID to purge.
		:return: 
		"""

	@staticmethod
	def PurgeDeletedJobs(jobIDs: Iterable[Text]):
		"""
		Purge deleted jobs. 

		:param Iterable[Text] jobIDs: The deleted job IDs to purge.
		:return: 
		"""

	@staticmethod
	def ReleasePendingJob(job: Job):
		"""
		Releases a pending job. 

		:param Job job: The pending job to release.
		:return: 
		"""

	@staticmethod
	def ReleasePendingTasks(job: Job, tasks: Iterable[Task]):
		"""
		Releases pending tasks for a job. This is only supported if the job is frame dependent. 

		:param Job job: The job.
		:param Iterable[Task] tasks: The list of pending tasks to resume.
		:return: 
		"""

	@staticmethod
	def RemoveGroupFromSlave(slaveName: Text, groupName: Text):
		"""
		Removes a group from the given Worker. 

		:param Text slaveName: The Worker name.
		:param Text groupName: The group name.
		:return: 
		"""

	@staticmethod
	def RemovePoolFromSlave(slaveName: Text, poolName: Text):
		"""
		Removes a pool from the given Worker. 

		:param Text slaveName: The Worker name.
		:param Text poolName: The pool name.
		:return: 
		"""

	@staticmethod
	def RemoveSlavesFromLimitGroupList(name: Text, slaveNames: object):
		"""
		Removes Workers from a limit group's list of Workers. 

		:param Text name: The limit group name.
		:param object slaveNames: The list of Workers to remove.
		:return: 
		"""

	@staticmethod
	def RemoveSlavesFromMachineLimitList(jobId: Text, slaveNames: object):
		"""
		Removes Workers from a job machine limit's list of Workers. 

		:param Text jobId: The job ID.
		:param object slaveNames: The list of Workers to remove.
		:return: 
		"""

	@staticmethod
	def RemoveUsersFromUserGroups(users: Iterable[Text], userGroups: Iterable[Text]):
		"""
		Removes all the users given from the provided user groups. 

		:param Iterable[Text] users: The users to remove.
		:param Iterable[Text] userGroups: The user groups to remove from.
		:return: 
		"""

	@staticmethod
	def RequeueJob(job: Job):
		"""
		Requeues a job. All rendering and completed tasks for the job will be requeued. 

		:param Job job: The job to requeue.
		:return: 
		"""

	@staticmethod
	def RequeueTasks(job: Job, tasks: Iterable[Task]):
		"""
		Requeue tasks for a job. 

		:param Job job: The job.
		:param Iterable[Task] tasks: The list of tasks to requeue.
		:return: 
		"""

	@staticmethod
	def ResetLimitGroup(limitGroupName: Text):
		"""
		Resets the usage counts for a limit group. 

		:param Text limitGroupName: The limit group name.
		:return: 
		"""

	@staticmethod
	def ResubmitJob(job: Job, frameList: Text, chunkSize: int, submitSuspended: bool) -> Job:
		"""
		Resubmits an existing job to 

		:param Job job: The job to resubmit.
		:param Text frameList: The new list of frames.
		:param int chunkSize: The new chunk size.
		:param bool submitSuspended: If the job should be submitted in the suspended state.
		:return: The new job object.
		"""

	@staticmethod
	def ResumeFailedJob(job: Job):
		"""
		Resume a failed job. 

		:param Job job: The failed job to resume.
		:return: 
		"""

	@staticmethod
	def ResumeFailedTasks(job: Job, tasks: Iterable[Task]):
		"""
		Resumes failed tasks for a job. 

		:param Job job: The job.
		:param Iterable[Task] tasks: The list of failed tasks to resume.
		:return: 
		"""

	@staticmethod
	def ResumeJob(job: Job):
		"""
		Resume a suspended job. 

		:param Job job: The job to resume.
		:return: 
		"""

	@staticmethod
	def ResumeTasks(job: Job, tasks: Iterable[Task]):
		"""
		Resumes suspended tasks for a job. 

		:param Job job: The job.
		:param Iterable[Task] tasks: The list of tasks to resume.
		:return: 
		"""

	@staticmethod
	def SaveAWSPortalSettings(settings: AWSPortalSettings) -> bool:
		"""
		Saves the DAWS settings. 

		:param AWSPortalSettings settings: 
		:return: 
		"""

	@staticmethod
	def SaveBalancerInfo(balancerInfo: BalancerInfo):
		"""
		Saves a balancer info to the database. 

		:param BalancerInfo balancerInfo: The balancer info.
		:return: 
		"""

	@staticmethod
	def SaveBalancerSettings(balancerSettings: BalancerSettings):
		"""
		Saves settings for a balancer to the database. 

		:param BalancerSettings balancerSettings: The balancer settings.
		:return: 
		"""

	@staticmethod
	def SaveJob(job: Job):
		"""
		Updates a job's properties in the database. 

		:param Job job: The job.
		:return: 
		"""

	@staticmethod
	def SaveLimitGroup(limitGroup: LimitGroup):
		"""
		Updates a limit group's properties in the database. 

		:param LimitGroup limitGroup: The limit group.
		:return: 
		"""

	@staticmethod
	def SaveNetworkSettings(networkSettings: IDeadlineNetworkSettings) -> bool:
		"""
		Saves the network settings to the repository. 

		:param IDeadlineNetworkSettings networkSettings: The network settings to save.
		:return: True if the settings were saved.
		"""

	@staticmethod
	def SavePowerManagementOptions(options: PowerManagementOptions) -> bool:
		"""
		Saves the power management options. 

		:param PowerManagementOptions options: The power management options.
		:return: True if the options were saved.
		"""

	@staticmethod
	def SaveProxyServerInfo(proxyInfo: ProxyServerInfo):
		"""
		Save a ProxyServerInfo object to the Database. 

		:param ProxyServerInfo proxyInfo: The ProxyServerInfo.
		:return: 
		"""

	@staticmethod
	def SaveProxyServerSettings(proxySettings: ProxyServerSettings):
		"""
		Save a ProxyServerInfo object to the Database. 

		:param ProxyServerSettings proxySettings: The ProxyServerSettings.
		:return: 
		"""

	@staticmethod
	def SavePulseInfo(pulseInfo: PulseInfo):
		"""
		Saves a pulse info to the database. 

		:param PulseInfo pulseInfo: The pulse info.
		:return: 
		"""

	@staticmethod
	def SavePulseSettings(pulseSettings: PulseSettings):
		"""
		Saves settings for a pulse to the database. 

		:param PulseSettings pulseSettings: The pulse settings.
		:return: 
		"""

	@staticmethod
	def SaveSlaveInfo(slaveInfo: SlaveInfo):
		"""
		Saves a Worker info to the database. 

		:param SlaveInfo slaveInfo: The Worker info.
		:return: 
		"""

	@staticmethod
	def SaveSlaveSettings(slaveSettings: SlaveSettings):
		"""
		Saves settings for a Worker to the database. 

		:param SlaveSettings slaveSettings: The Worker settings.
		:return: 
		"""

	@staticmethod
	def SaveUserInfo(userInfo: IUserInfo):
		"""
		Saves a user info to the database. 

		:param IUserInfo userInfo: The user info.
		:return: 
		"""

	@staticmethod
	def SetGroupsForSlave(slaveName: Text, groupNames: Iterable[Text]):
		"""
		Sets the list of groups for the given Worker. 

		:param Text slaveName: The Worker name.
		:param Iterable[Text] groupNames: The group names.
		:return: 
		"""

	@staticmethod
	def SetJobFrameRange(job: Job, frameList: Text, chunkSize: int):
		"""
		Modifies a job's frame range. If the job is currently being rendered, any rendering tasks will be requeued to perform this operation. 

		:param Job job: The job.
		:param Text frameList: The frame list.
		:param int chunkSize: The chunk size.
		:return: 
		"""

	@staticmethod
	def SetJobOutputDirectories(job: Job, outputDirectories: object):
		"""
		Sets the job's output directories. 

		:param Job job: The job.
		:param object outputDirectories: The list of output directories.
		:return: 
		"""

	@staticmethod
	def SetLimitGroup(name: Text, limit: int, listedSlaves: object, isWhiteList: bool, excludedSlaves: object, releaseProgress: float) -> LimitGroup:
		"""
		Creates a limit group if it doesn't exist, or updates its properties if it does. 

		:param Text name: The limit group name.
		:param int limit: The limit.
		:param object listedSlaves: The list of Workers.
		:param bool isWhiteList: True if the list of Workers is an allow list.
		:param object excludedSlaves: The list of Workers that will ignore this limit group.
		:param float releaseProgress: The release percentage.
		:return: 
		"""

	@staticmethod
	def SetLimitGroupListedSlaves(name: Text, slaveNames: object):
		"""
		Sets the listed Workers for a limit group. 

		:param Text name: The limit group name.
		:param object slaveNames: The list of Worker names.
		:return: 
		"""

	@staticmethod
	def SetLimitGroupMaximum(name: Text, limit: int):
		"""
		Sets the limit for a limit group. 

		:param Text name: The limit group name.
		:param int limit: The limit.
		:return: 
		"""

	@staticmethod
	def SetLimitGroupReleaseProgress(name: Text, releaseProgress: float):
		"""
		Sets the release progres for a limit group. 

		:param Text name: The limit group name.
		:param float releaseProgress: The release progress.
		:return: 
		"""

	@staticmethod
	def SetLimitGroupWhiteListFlag(name: Text, isWhiteList: bool):
		"""
		Sets if the Worker list for a limit group is an allow list or a deny list. 

		:param Text name: The limit group name.
		:param bool isWhiteList: True if the list should be an allow list.
		:return: 
		"""

	@staticmethod
	def SetMachineLimit(jobId: Text, limit: int, listedSlaves: object, isWhiteList: bool, releaseProgress: float) -> LimitGroup:
		"""
		Creates a machine limit for a job if it doesn't exist, or updates its properties if it does. 

		:param Text jobId: The job ID.
		:param int limit: The machine limit.
		:param object listedSlaves: The list of Workers.
		:param bool isWhiteList: True if the list of Workers is an allow list.
		:param float releaseProgress: The release percentage.
		:return: 
		"""

	@staticmethod
	def SetMachineLimitListedSlaves(jobId: Text, slaveNames: object):
		"""
		Sets the listed Workers for a job's machine limit. 

		:param Text jobId: The job ID.
		:param object slaveNames: The list of Worker names.
		:return: 
		"""

	@staticmethod
	def SetMachineLimitMaximum(jobId: Text, limit: int):
		"""
		Sets the limit for a job's machine limit. 

		:param Text jobId: The job ID.
		:param int limit: The limit.
		:return: 
		"""

	@staticmethod
	def SetMachineLimitReleaseProgress(jobId: Text, releaseProgress: float):
		"""
		Sets the release progres for a job's machine limit. 

		:param Text jobId: The job ID.
		:param float releaseProgress: The release progress.
		:return: 
		"""

	@staticmethod
	def SetMachineLimitWhiteListFlag(jobId: Text, isWhiteList: bool):
		"""
		Sets if the Worker list for a job's machine limit is an allow list or a deny list. 

		:param Text jobId: The job ID.
		:param bool isWhiteList: True if the list should be an allow list.
		:return: 
		"""

	@staticmethod
	def SetPluginLimitGroups(pluginName: Text, limitGroupNames: Iterable[Text]):
		"""
		Set PluginConfigSettings.LimitNames property for a specified 

		:param Text pluginName: Name of a 
		:param Iterable[Text] limitGroupNames: Names of LimitGroup records to be assigned to the specified 
		:return: 
		"""

	@staticmethod
	def SetPoolsForSlave(slaveName: Text, poolNames: Iterable[Text]):
		"""
		Sets the list of pools for the given Worker. 

		:param Text slaveName: The Worker name.
		:param Iterable[Text] poolNames: The pool names.
		:return: 
		"""

	@staticmethod
	def SetPostJobScript(job: Job, script: Text):
		"""
		Sets a jobs post job script. 

		:param Job job: The job.
		:param Text script: The script.
		:return: 
		"""

	@staticmethod
	def SetPreJobScript(job: Job, script: Text):
		"""
		Sets a jobs pre job script. 

		:param Job job: The job.
		:param Text script: The script.
		:return: 
		"""

	@staticmethod
	def SetUsersForUserGroups(users: Iterable[Text], userGroups: Iterable[Text]):
		"""
		Sets the user list for the provided user groups to contain the provided users, overriding the old lists. 

		:param Iterable[Text] users: The users to set.
		:param Iterable[Text] userGroups: The user groups to set.
		:return: 
		"""

	@staticmethod
	def SlaveExists(slaveName: Text) -> bool:
		"""
		Checks whether or not a Worker with the given name exists. 

		:param Text slaveName: The Worker name to check.
		:return: Whether or not the Worker exists.
		"""

	@staticmethod
	def SubmitJob(jobFiles: Iterable[Text]) -> Job:
		"""
		Submits a job to 

		:param Iterable[Text] jobFiles: The job files that build up the job (job info file, plugin info file, and then any auxiliary files).
		:return: The job object.
		"""

	@staticmethod
	def SuspendJob(job: Job):
		"""
		Suspend a queued, rendering, or pending job. 

		:param Job job: The job to suspend.
		:return: 
		"""

	@staticmethod
	def SuspendNonRenderingTasks(job: Job):
		"""
		Suspend the non rendering tasks for a queued or pending job. 

		:param Job job: The job to suspend the non rendering tasks for.
		:return: 
		"""

	@staticmethod
	def SuspendTasks(job: Job, tasks: Iterable[Task]) -> bool:
		"""
		Suspends tasks for a job. 

		:param Job job: The job.
		:param Iterable[Task] tasks: The list of tasks to suspend.
		:return: Returns True if the job is now suspended.
		"""

	@staticmethod
	def UndeleteJob(job: Job):
		"""
		Undelete a job. 

		:param Job job: The job to undelete.
		:return: 
		"""

	@staticmethod
	def UndeleteJobs(jobs: Iterable[Job]):
		"""
		Undelete jobs. 

		:param Iterable[Job] jobs: The jobs to undelete.
		:return: 
		"""

	@staticmethod
	def UpdateJobOutputFileNames(job: Job, outputFileNames: object):
		"""
		Sets the job's output file names. 

		:param Job job: The job.
		:param object outputFileNames: The list of output file names. These should be full paths including the file name.
		:return: 
		"""

	@staticmethod
	def UpdateJobOutputTileFileNames(job: Job, outputTileFileNames: Text):
		"""
		Sets the job's output tile file names. 

		:param Job job: The job.
		:param Text outputTileFileNames: The 2 dimensional list of output tile file names. These should be full paths including the file name.
		:return: 
		"""

	@staticmethod
	def UpdateJobSubmissionDate(job: Job):
		"""
		Sets the job's submission date to the current time. 

		:param Job job: The job.
		:return: 
		"""

	@staticmethod
	def UpdateTaskProperties(jobID: Text, task: Task):
		"""
		Updates some of the task properties for the given task. Note that only the settings in the task's TaskProperties container can be updated this way. 

		:param Text jobID: The job ID for the task.
		:param Task task: The task to update.
		:return: 
		"""

	@staticmethod
	def UpdateTaskProperties(jobID: Text, tasks: Iterable[Task]):
		"""
		Updates some of the task properties for the given tasks. Note that only the settings in the task's TaskProperties container can be updated this way. 

		:param Text jobID: The job ID for the tasks.
		:param Iterable[Task] tasks: The tasks to update.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.Slaves import SlaveInfoSettings
from Deadline.Slaves import SlaveInfo
class SlaveUtils:
	"""
	 Worker utility functions.
	"""
	@staticmethod
	def GetMachineIPAddresses(slaveInfos: Iterable[SlaveInfo]) -> Iterable[Text]:
		"""
		Gets the list of unique machine IP Addresses from the given Worker infos. 

		:param Iterable[SlaveInfo] slaveInfos: The list of Worker infos.
		:return: The list of unique machine IP addresses.
		"""

	@staticmethod
	def GetMachineNameOrIPAddresses(slaveInfoSettings: Iterable[SlaveInfoSettings]) -> Iterable[Text]:
		"""
		Gets the list of unique machine names or IP addresses from the given Worker info settings. If a Worker has an override for the host machine or IP address that is returned, or if the network settings are set to use Worker IP addresses. Otherwise, the machine name will be returned. 

		:param Iterable[SlaveInfoSettings] slaveInfoSettings: The list of Worker info settings.
		:return: The list of unique machine names and IP addresses.
		"""

	@staticmethod
	def GetMachineNames(slaveInfos: Iterable[SlaveInfo]) -> Iterable[Text]:
		"""
		Gets the list of unique machine names from the given Worker infos. 

		:param Iterable[SlaveInfo] slaveInfos: The list of Worker infos.
		:return: The list of unique machine names.
		"""

	@staticmethod
	def SendRemoteCommand(machineName: Text, command: Text):
		"""
		Send a remote command to the specified machine. Scripts that utilize this function are intended to be executed only from the Monitor. Use "SendRemoteCommandWithResults" to wait on a response from the 

		:param Text machineName: The machine to send the command to.
		:param Text command: The command.
		:return: 
		"""

	@staticmethod
	def SendRemoteCommandNoWait(machineName: Text, command: Text):
		"""
		Send a remote command to the specified machine and don't wait for a response. If this script is running from the Monitor, the remote command will be added to the Remote Commands panel. 

		:param Text machineName: The machine to send the command to.
		:param Text command: The command.
		:return: 
		"""

	@staticmethod
	def SendRemoteCommandWithResults(machineName: Text, command: Text) -> Text:
		"""
		Send a remote command to the specified machine. If this script is running from the Monitor, the remote command will NOT be added to the Remote Commands panel because the results are returned. 

		:param Text machineName: The machine to send the command to.
		:param Text command: The command.
		:return: Returns the results from the command.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class StringUtils:
	"""
	 String utility functions.
	"""
	@staticmethod
	def BlankIfEitherIsBlank(str1: Text, str2: Text) -> Text:
		"""
		If both strings are non-empty, they are combined and returned as the result. If either string is empty, an empty string is returned. 

		:param Text str1: The first string.
		:param Text str2: The second string.
		:return: The result string.
		"""

	@staticmethod
	def ContainsOnlyWordCharacters(str: Text) -> bool:
		"""
		Returns true if the given string is non-empty, and only contains letters, numbers, underscores, and hyphens. 

		:param Text str: The string.
		:return: True if the string only contains word characters.
		"""

	@staticmethod
	def FromCommaSeparatedString(list: Text) -> Iterable[Text]:
		"""
		Converts a comma separated string into a list of strings. 

		:param Text list: The list as a string.
		:return: An list of strings.
		"""

	@staticmethod
	def FromCommaSeparatedString(list: Text, allowEmptyTokens: bool) -> Iterable[Text]:
		"""
		Converts a comma separated string into a list of strings. 

		:param Text list: The list as a string.
		:param bool allowEmptyTokens: Whether to allow empty tokens in the result.
		:return: An list of strings.
		"""

	@staticmethod
	def FromSemicolonSeparatedString(list: Text, allowEmptyTokens: bool) -> Iterable[Text]:
		"""
		Converts a semicolon separated string into a list of strings. 

		:param Text list: The list as a string.
		:param bool allowEmptyTokens: Whether to allow empty tokens in the result.
		:return: An list of strings.
		"""

	@staticmethod
	def FromSemicolonSeparatedString(list: Text) -> Iterable[Text]:
		"""
		Converts a semicolon separated string into a list of strings. 

		:param Text list: The list as a string.
		:return: An list of strings.
		"""

	@staticmethod
	def GetDecryptedVncPasswordString(str: Text) -> Text:
		"""
		Decrypts the password from the given encrypted VNC string. 

		:param Text str: The encrypted VNC string.
		:return: The decrypted password.
		"""

	@staticmethod
	def GetEncryptedVncPasswordString(password: Text) -> Text:
		"""
		Gets an encrypted VNC password string from the given password. 

		:param Text password: The password.
		:return: The encrypted string.
		"""

	@staticmethod
	def GetNumeralKeyFromPath(pathWithNumeralKey: Text, numeralKeyChars: Iterable[char]) -> Text:
		"""
		Retrieves the numeral key (based on the specified numeral key characters) from the specified path. 

		:param Text pathWithNumeralKey: The path with a numeral key.
		:param Iterable[char] numeralKeyChars: The character(s) which represent a numerical key. For example: '#' or '?'.
		:return: The numeral key.
		"""

	@staticmethod
	def GetNumeralKeyFromPath(pathWithNumeralKey: Text, numeralKeyChars: Iterable[char], allowEmptyNumeralKey: bool) -> Text:
		"""
		Retrieves the numeral key (based on the specified numeral key characters) from the specified path. 

		:param Text pathWithNumeralKey: The path with a numeral key.
		:param Iterable[char] numeralKeyChars: The character(s) which represent a numerical key. For example: '#' or '?'.
		:param bool allowEmptyNumeralKey: If False, an error will be thrown if the specified path doesn't contain a numerical key.
		:return: The numeral key.
		"""

	@staticmethod
	def IsEmpty(str: Text) -> bool:
		"""
		Checks if the specified string is empty. 

		:param Text str: The string.
		:return: True if the string is null or has length of 0.
		"""

	@staticmethod
	def Pad(str: Text, desiredLength: int, fillCharacter: char) -> Text:
		"""
		Pads the specified string with the fill character to achieve the desired length. 

		:param Text str: The string.
		:param int desiredLength: The desired length.
		:param char fillCharacter: The fill character.
		:return: The padded string.
		"""

	@staticmethod
	def ParseBoolean(s: Text) -> bool:
		"""
		Parses a boolean value from the string. Throws an error if a boolean value could not be parsed. 

		:param Text s: The string.
		:return: The boolean value.
		"""

	@staticmethod
	def ParseBooleanWithDefault(s: Text, defaultValue: bool) -> bool:
		"""
		Parses a boolean value from the string. Returns the default value if a boolean value could not be parsed. 

		:param Text s: The string.
		:param bool defaultValue: The default value.
		:return: The boolean value.
		"""

	@staticmethod
	def ParseLeadingNumber(s: Text) -> float:
		"""
		Parses the number at the begining of the specified string. 

		:param Text s: The string.
		:return: The number, or 0 if no number could be found.
		"""

	@staticmethod
	def RemoveWhitespace(str: Text) -> Text:
		"""
		Removes all whitespace from the specified string, including tabs and end of line characters. 

		:param Text str: The string.
		:return: The string without any whitespace.
		"""

	@staticmethod
	def ReplaceNumeralKey(pathWithNumeralKey: Text, numeralKey: Text, index: int, padExtra: bool) -> Text:
		"""
		Replaces the specified numeralKey in the specified path with the specified index. 

		:param Text pathWithNumeralKey: The path with the numeral key.
		:param Text numeralKey: The numeral key to replace.
		:param int index: The number to replace the numeral key with.
		:param bool padExtra: If True, extra padding will be added if necessary to ensure the entire number is inserted into the numeral key.
		:return: The path with the numeral key replaced.
		"""

	@staticmethod
	def ToCommaSeparatedString(strings: Iterable[Text], includeSpaces: bool) -> Text:
		"""
		Converts a list of strings to a comma separated string. 

		:param Iterable[Text] strings: The string list.
		:param bool includeSpaces: If spaces should be inserted after each comma.
		:return: The comma separated string.
		"""

	@staticmethod
	def ToSemicolonSeparatedString(strings: Iterable[Text], includeSpaces: bool) -> Text:
		"""
		Converts a list of strings to a semicolon separated string. 

		:param Iterable[Text] strings: The string list.
		:param bool includeSpaces: If spaces should be inserted after each semicolon.
		:return: The semicolon separated string.
		"""

	@staticmethod
	def ToZeroPaddedString(value: int, length: int) -> Text:
		"""
		Creates a string of the desired length containing the given value, padded with zeros. 

		:param int value: The number to pad with zeros.
		:param int length: The length the resulting string should be.
		:return: The value padded with zeros.
		"""

	@staticmethod
	def ToZeroPaddedString(value: int, length: int, strictLength: bool) -> Text:
		"""
		Creates a string of the desired length containing the given value, padded with zeros. 

		:param int value: The number to pad with zeros.
		:param int length: The length the resulting string should be.
		:param bool strictLength: If False, an error will be thrown if the result is longer than the given length.
		:return: The value padded with zeros.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class SystemUtils:
	"""
	 System utility functions.
	"""
	@staticmethod
	def GetAvailableRam() -> long:
		"""
		Gets the system's available memory. 

		
		:return: The memory in bytes.
		"""

	@staticmethod
	def GetCpuCount() -> int:
		"""
		Gets the system's CPU count. 

		
		:return: The number of CPUs.
		"""

	@staticmethod
	def GetRegistryKeyValue(keyName: Text, valueName: Text, defaultValue: Text) -> Text:
		"""
		Gets a value from the system's registry (Windows only). 

		:param Text keyName: The registry key name.
		:param Text valueName: The value name.
		:param Text defaultValue: The default value if the key or value doesn't exist.
		:return: The result.
		"""

	@staticmethod
	def GetTotalRam() -> long:
		"""
		Gets the system's total memory. 

		
		:return: The memory in bytes.
		"""

	@staticmethod
	def GetUsedRam() -> long:
		"""
		Gets the system's memory that is currently in use. 

		
		:return: The memory in bytes.
		"""

	@staticmethod
	def Is64Bit() -> bool:
		"""
		Checks if the system is 64 bit. 

		
		:return: True if it is 64 bit.
		"""

	@staticmethod
	def IsRunningOnLinux() -> bool:
		"""
		Checks if the system is Linux. 

		
		:return: True if it is Linux.
		"""

	@staticmethod
	def IsRunningOnMac() -> bool:
		"""
		Checks if the system is Mac OSX. 

		
		:return: True if it is Mac OSX.
		"""

	@staticmethod
	def IsRunningOnWindows() -> bool:
		"""
		Checks if the system is Windows. 

		
		:return: True if it is Windows.
		"""

	@staticmethod
	def Sleep(milliseconds: int):
		"""
		Sleep for the specified time. 

		:param int milliseconds: The time to sleep, in milliseconds.
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class WebServiceUtils:
	"""
	 Web Service Utils function.
	"""
	@staticmethod
	def GetJobInfo(jobID: Text) -> Dict[Text,Text]:
		"""
		Gets a dictionary of properties for a job. For Web Service scripts only. 

		:param Text jobID: The ID of the job to retrieve.
		:return: The job's properties, or null if the job isn't cached.
		"""

	@staticmethod
	def GetJobs() -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for all jobs. For Web Service scripts only. 

		
		:return: The list of dictionaries.
		"""

	@staticmethod
	def GetJobTasks(jobId: Text) -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for the tasks belonging to the given job. For Web Service scripts only. 

		:param Text jobId: The job ID.
		:return: The list of property dictionaries, or null if the job isn't cached.
		"""

	@staticmethod
	def GetLimitGroupInfo(limitGroupName: Text) -> Dict[Text,Text]:
		"""
		Gets a dictionary of properties for a limit group. For Web Service scripts only. 

		:param Text limitGroupName: The name of the limit group to retrieve.
		:return: The limit group's properties, or null if the limit group isn't cached.
		"""

	@staticmethod
	def GetLimitGroups() -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for all limit groups. For Web Service scripts only. 

		
		:return: The list of dictionaries.
		"""

	@staticmethod
	def GetSlaveInfo(slaveName: Text) -> Dict[Text,Text]:
		"""
		Gets a dictionary of properties for a Worker. For Web Service scripts only. 

		:param Text slaveName: The name of the Worker to retrieve.
		:return: The Worker's properties, or null if the Worker isn't cached.
		"""

	@staticmethod
	def GetSlaves() -> Iterable[Dict[Text,Text]]:
		"""
		Gets a list of property dictionaries for all Workers. For Web Service scripts only. 

		
		:return: The list of dictionaries.
		"""

