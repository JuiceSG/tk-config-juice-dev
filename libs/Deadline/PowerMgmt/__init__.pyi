class IdleShutdownOverrideType:
	CustomDays = None # One or more custom days.           
	Weekdays = None # Monday, Tuesday, Wednesday, Thursday, and Friday.           
	Weekends = None # Saturday and Sunday.           
	EveryDay = None # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.           


from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.PowerMgmt import IdleShutdownOverride
class IdleShutdownOptions:
	"""
	 The idle shutdown options.
	"""

	@property
	def Command(self) -> Text:
		"""
		
Command to run to shutdown. If set, the command is executed instead of calling shutdown.         
		"""
	@Command.setter
	def Command(self, value: Text): ...


	@property
	def DebugMode(self) -> bool:
		"""
		
If idle shutdown is running in debug mode (no machines should be shut down).         
		"""
	@DebugMode.setter
	def DebugMode(self, value: bool): ...


	@property
	def Enabled(self) -> bool:
		"""
		
If idle shutdown is enabled.         
		"""
	@Enabled.setter
	def Enabled(self, value: bool): ...


	@property
	def HybridShutdown(self) -> bool:
		"""
		
If Hybrid shutdown should be enabled (Windows 8 and later).         
		"""
	@HybridShutdown.setter
	def HybridShutdown(self, value: bool): ...


	@property
	def ImportantProcesses(self) -> Iterable[Text]:
		"""
		
Names of important processes that, if any are running, the machine should not be shutdown.         
		"""
	@ImportantProcesses.setter
	def ImportantProcesses(self, value: Iterable[Text]): ...


	@property
	def MaximumIdleMinutes(self) -> int:
		"""
		
The number of minutes a Worker can be idle.         
		"""
	@MaximumIdleMinutes.setter
	def MaximumIdleMinutes(self, value: int): ...


	@property
	def OrderOverrideArray(self) -> Iterable[Text]:
		"""
		
A Worker array used to set the order of shutdown.         
		"""
	@OrderOverrideArray.setter
	def OrderOverrideArray(self, value: Iterable[Text]): ...


	@property
	def OverrideOrder(self) -> bool:
		"""
		
Whether or not to use the order override array or not.         
		"""
	@OverrideOrder.setter
	def OverrideOrder(self, value: bool): ...


	@property
	def ShutdownOverrides(self) -> Iterable[IdleShutdownOverride]:
		"""
		
The idle shutdown overrides.         
		"""
	@ShutdownOverrides.setter
	def ShutdownOverrides(self, value: Iterable[IdleShutdownOverride]): ...


	@property
	def SlavesToLeaveRunning(self) -> int:
		"""
		
The number of Workers to leave running.         
		"""
	@SlavesToLeaveRunning.setter
	def SlavesToLeaveRunning(self, value: int): ...


	@property
	def Standby(self) -> bool:
		"""
		
If the machine should go into stand by.         
		"""
	@Standby.setter
	def Standby(self, value: bool): ...

from typing import Iterable
from typing import Text
from typing import Dict
class IdleShutdownOverride:
	"""
	 These are used to override the default idle shutdown settings.
	"""

	@property
	def EndTime(self) -> DateTime:
		"""
		
The end time for this override. This should be TimeZone-agnostic.         
		"""
	@EndTime.setter
	def EndTime(self, value: DateTime): ...


	@property
	def MaximumIdleMinutes(self) -> int:
		"""
		
The number of minutes a Worker can be idle for before it is shutdown.         
		"""
	@MaximumIdleMinutes.setter
	def MaximumIdleMinutes(self, value: int): ...


	@property
	def OverrideDays(self) -> Iterable[DayOfWeek]:
		"""
		
The days of the week that this override applies to.         
		"""
	@OverrideDays.setter
	def OverrideDays(self, value: Iterable[DayOfWeek]): ...


	@property
	def OverrideType(self) -> IdleShutdownOverrideType:
		"""
		
The type of override.         
		"""
	@OverrideType.setter
	def OverrideType(self, value: IdleShutdownOverrideType): ...


	@property
	def SlavesToLeaveRunning(self) -> int:
		"""
		
The minimum number of Workers to leave running.         
		"""
	@SlavesToLeaveRunning.setter
	def SlavesToLeaveRunning(self, value: int): ...


	@property
	def StartTime(self) -> DateTime:
		"""
		
The start time for this override. This should be TimeZone-agnostic.         
		"""
	@StartTime.setter
	def StartTime(self, value: DateTime): ...

	def ContainsDay(self, dayOfWeek: DayOfWeek) -> bool:
		"""
		Checks if this override contains the specified day. 

		:param DayOfWeek dayOfWeek: The day.
		:return: True if this override contains the specified day.
		"""

	def IsOverrideCriteriaMet(self, dateTime: DateTime) -> bool:
		"""
		Checks if this override is valid for the specified date/time. 

		:param DateTime dateTime: The date/time.
		:return: True if this override is valid for the specified date/time.
		"""

	def IsTimeInInterval(self, dateTime: DateTime) -> bool:
		"""
		Checks if the specified time falls within this override. 

		:param DateTime dateTime: The time.
		:return: True if the specified time falls within this override.
		"""

	def ToString(self, ) -> overridestring:
		"""
		Converts the override to a human readable string. 

		
		:return: 
		"""

from typing import Iterable
from typing import Text
from typing import Dict
class MachineRestartOptions:
	"""
	 The machine restart options.
	"""

	@property
	def Command(self) -> Text:
		"""
		
Command to run to restart. If set, the command is executed instead of calling restart.         
		"""
	@Command.setter
	def Command(self, value: Text): ...


	@property
	def DebugMode(self) -> bool:
		"""
		
If machine restart is running in debug mode.         
		"""
	@DebugMode.setter
	def DebugMode(self, value: bool): ...


	@property
	def Enabled(self) -> bool:
		"""
		
If machine restart is enabled.         
		"""
	@Enabled.setter
	def Enabled(self, value: bool): ...


	@property
	def RestartIntervalMinutes(self) -> int:
		"""
		
How often machines in the group should be restarted.         
		"""
	@RestartIntervalMinutes.setter
	def RestartIntervalMinutes(self, value: int): ...

from typing import Iterable
from typing import Text
from typing import Dict
class MachineStartupOptions:
	"""
	 The options for wake on LAN.
	"""

	@property
	def Command(self) -> Text:
		"""
		
The command to run if WakeOnLan is disabled.         
		"""
	@Command.setter
	def Command(self, value: Text): ...


	@property
	def DebugMode(self) -> bool:
		"""
		
If machine startup is running in debug mode.         
		"""
	@DebugMode.setter
	def DebugMode(self, value: bool): ...


	@property
	def DisabledByThermalShutdown(self) -> bool:
		"""
		
If the group was disabled by thermal shutdown.         
		"""
	@DisabledByThermalShutdown.setter
	def DisabledByThermalShutdown(self, value: bool): ...


	@property
	def Enabled(self) -> bool:
		"""
		
If machine startup is enabled.         
		"""
	@Enabled.setter
	def Enabled(self, value: bool): ...


	@property
	def MillisecondsBetweenWOLPackects(self) -> int:
		"""
		
The number of milliseconds between each machine Wake On LAN Packet.         
		"""
	@MillisecondsBetweenWOLPackects.setter
	def MillisecondsBetweenWOLPackects(self, value: int): ...


	@property
	def OrderOverrideArray(self) -> Iterable[Text]:
		"""
		
A Worker array used to set the order of startup.         
		"""
	@OrderOverrideArray.setter
	def OrderOverrideArray(self, value: Iterable[Text]): ...


	@property
	def OverrideOrder(self) -> bool:
		"""
		
Whether or not to use the order override array or not.         
		"""
	@OverrideOrder.setter
	def OverrideOrder(self, value: bool): ...


	@property
	def SendStartSlaveCommand(self) -> bool:
		"""
		
If the "Start Worker" remote command should be sent in addition to waking up the machine.         
		"""
	@SendStartSlaveCommand.setter
	def SendStartSlaveCommand(self, value: bool): ...


	@property
	def SlavesToWakeupPerInterval(self) -> int:
		"""
		
The number of machines to wake up per interval.         
		"""
	@SlavesToWakeupPerInterval.setter
	def SlavesToWakeupPerInterval(self, value: int): ...


	@property
	def TargetExtraIdleSlaves(self) -> int:
		"""
		
The target number of extra idle Workers available.         
		"""
	@TargetExtraIdleSlaves.setter
	def TargetExtraIdleSlaves(self, value: int): ...


	@property
	def WakeOnLan(self) -> bool:
		"""
		
If the group uses Wake On LAN.         
		"""
	@WakeOnLan.setter
	def WakeOnLan(self, value: bool): ...

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.PowerMgmt import MachineStartupOptions
from Deadline.PowerMgmt import MachineRestartOptions
from Deadline.PowerMgmt import ThermalShutdownOptions
from Deadline.PowerMgmt import IdleShutdownOptions
class PowerManagementGroup:
	"""
	 A class for storing a power management group.
	"""

	@property
	def AllSlaves(self) -> bool:
		"""
		
If all Workers should be included in this group.         
		"""
	@AllSlaves.setter
	def AllSlaves(self, value: bool): ...


	@property
	def Enabled(self) -> bool:
		"""
		
If power management group is enabled.         
		"""
	@Enabled.setter
	def Enabled(self, value: bool): ...


	@property
	def IdleShutdownOptions(self) -> IdleShutdownOptions:
		"""
		
The idle shutdown options for this group.         
		"""
	@IdleShutdownOptions.setter
	def IdleShutdownOptions(self, value: IdleShutdownOptions): ...


	@property
	def MachineRestartOptions(self) -> MachineRestartOptions:
		"""
		
The machine restart options for this group.         
		"""
	@MachineRestartOptions.setter
	def MachineRestartOptions(self, value: MachineRestartOptions): ...


	@property
	def MachineStartupOptions(self) -> MachineStartupOptions:
		"""
		
The machine startup options for this group.         
		"""
	@MachineStartupOptions.setter
	def MachineStartupOptions(self, value: MachineStartupOptions): ...


	@property
	def Name(self) -> Text:
		"""
		
The group name.         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def SlaveNames(self) -> Iterable[Text]:
		"""
		
The Workers in this group.         
		"""
	@SlaveNames.setter
	def SlaveNames(self, value: Iterable[Text]): ...


	@property
	def ThermalShutdownOptions(self) -> ThermalShutdownOptions:
		"""
		
The thermal shutdown options for this group.         
		"""
	@ThermalShutdownOptions.setter
	def ThermalShutdownOptions(self, value: ThermalShutdownOptions): ...

from typing import Iterable
from typing import Text
from typing import Dict
from Deadline.PowerMgmt import PowerManagementGroup
class PowerManagementOptions(BaseDocument):
	"""
	 A class for storing power management options.
	"""

	@property
	def Groups(self) -> Iterable[PowerManagementGroup]:
		"""
		
The idle shutdown groups.         
		"""
	@Groups.setter
	def Groups(self, value: Iterable[PowerManagementGroup]): ...

from typing import Iterable
from typing import Text
from typing import Dict
from FranticX.Units import Temperature
from Deadline.PowerMgmt import ThermalShutdownThreshold
from Deadline.PowerMgmt import ThermalShutdownSensor
class ThermalShutdownOptions:
	"""
	 The thermal shutdown options.
	"""

	@property
	def DebugMode(self) -> bool:
		"""
		
If thermal shutdown is running in debug mode.         
		"""
	@DebugMode.setter
	def DebugMode(self, value: bool): ...


	@property
	def DisableStartup(self) -> bool:
		"""
		
Whether or not to disable Machine Startup.         
		"""
	@DisableStartup.setter
	def DisableStartup(self, value: bool): ...


	@property
	def Enabled(self) -> bool:
		"""
		
If thermal shutdown is enabled.         
		"""
	@Enabled.setter
	def Enabled(self, value: bool): ...


	@property
	def OrderOverrideArray(self) -> Iterable[Text]:
		"""
		
A Worker array used to override the order of shutdown.         
		"""
	@OrderOverrideArray.setter
	def OrderOverrideArray(self, value: Iterable[Text]): ...


	@property
	def OverrideOrder(self) -> bool:
		"""
		
Whether or not to use the order override array or not.         
		"""
	@OverrideOrder.setter
	def OverrideOrder(self, value: bool): ...


	@property
	def ReEnableStartup(self) -> bool:
		"""
		
Whether or not to re-enable Machine Startup.         
		"""
	@ReEnableStartup.setter
	def ReEnableStartup(self, value: bool): ...


	@property
	def ReEnableStartupTemp(self) -> Temperature:
		"""
		
The Re-enable startup temperature.         
		"""
	@ReEnableStartupTemp.setter
	def ReEnableStartupTemp(self, value: Temperature): ...


	@property
	def SensorOfflineTimeoutMinutes(self) -> int:
		"""
		
The amount of time the sensor(s) can be unreachable before the Workers are shutdown.         
		"""
	@SensorOfflineTimeoutMinutes.setter
	def SensorOfflineTimeoutMinutes(self, value: int): ...


	@property
	def Sensors(self) -> Iterable[ThermalShutdownSensor]:
		"""
		
The sensors in this zone.         
		"""
	@Sensors.setter
	def Sensors(self, value: Iterable[ThermalShutdownSensor]): ...


	@property
	def ShutdownSlavesIfSensorsOffline(self) -> bool:
		"""
		
If Workers in this zone should shutdown if the sensor(s) cannot be reached.         
		"""
	@ShutdownSlavesIfSensorsOffline.setter
	def ShutdownSlavesIfSensorsOffline(self, value: bool): ...


	@property
	def TemperatureUnit(self) -> TemperatureUnits:
		"""
		
The temperature unit that thermal data is displayed in.         
		"""
	@TemperatureUnit.setter
	def TemperatureUnit(self, value: TemperatureUnits): ...


	@property
	def Thresholds(self) -> Iterable[ThermalShutdownThreshold]:
		"""
		
The temperature thresholds for this zone.         
		"""
	@Thresholds.setter
	def Thresholds(self, value: Iterable[ThermalShutdownThreshold]): ...

from typing import Iterable
from typing import Text
from typing import Dict
from FranticX.Units import Temperature
class ThermalShutdownSensor:
	"""
	 A class which represents a thermal sensor.
	"""

	@property
	def Community(self) -> Text:
		"""
		
The sensor SNMP community.         
		"""
	@Community.setter
	def Community(self, value: Text): ...


	@property
	def Host(self) -> Text:
		"""
		
The sensor hostname or IP address.         
		"""
	@Host.setter
	def Host(self, value: Text): ...


	@property
	def IsTestSensor(self) -> bool:
		"""
		
If this is a test sensor. A test sensor returns the TestTemperature value as the current temperature.         
		"""
	@IsTestSensor.setter
	def IsTestSensor(self, value: bool): ...


	@property
	def Name(self) -> Text:
		"""
		
Gets or sets the name of the sensor.         
		"""
	@Name.setter
	def Name(self, value: Text): ...


	@property
	def OID(self) -> Text:
		"""
		
The sensor object identifier.         
		"""
	@OID.setter
	def OID(self, value: Text): ...


	@property
	def TemperatureUnit(self) -> TemperatureUnits:
		"""
		
The temperature units that the sensor reports temperature in.         
		"""
	@TemperatureUnit.setter
	def TemperatureUnit(self, value: TemperatureUnits): ...


	@property
	def TestTemperature(self) -> int:
		"""
		
The temperature to use for testing (if this is a test sensor).         
		"""
	@TestTemperature.setter
	def TestTemperature(self, value: int): ...


	@property
	def TimeoutMilliseconds(self) -> int:
		"""
		
The timeout for reaching the sensor.         
		"""
	@TimeoutMilliseconds.setter
	def TimeoutMilliseconds(self, value: int): ...

	def GetTemperature(self, temperatureUnit: TemperatureUnits) -> Temperature:
		"""
		Gets the current sensor temperature. 

		:param TemperatureUnits temperatureUnit: The units to return the temperature in.
		:return: The current temperature.
		"""

	def GetTemperatureAsCelcius(self, ) -> Temperature:
		"""
		Gets the current sensor temperature in Celcius. 

		
		:return: The current temperature in Celcius.
		"""

	def GetTemperatureAsFahrenheit(self, ) -> Temperature:
		"""
		Gets the current sensor temperature in Fahrenheit. 

		
		:return: The current temperature in Fahrenheit.
		"""

	def GetTemperatureAsKelvin(self, ) -> Temperature:
		"""
		Gets the current sensor temperature in Kelvin. 

		
		:return: The current temperature in Kelvin.
		"""

from typing import Iterable
from typing import Text
from typing import Dict
from FranticX.Units import Temperature
class ThermalShutdownThreshold(IComparable):
	"""
	 A thermal shutdown threshold.
	"""

	@property
	def SlavesToShutdownPerInterval(self) -> int:
		"""
		
The number of Workers to shutdown per interval for this threshold.         
		"""
	@SlavesToShutdownPerInterval.setter
	def SlavesToShutdownPerInterval(self, value: int): ...


	@property
	def Temperature(self) -> Temperature:
		"""
		
The threshold temperature.         
		"""
	@Temperature.setter
	def Temperature(self, value: Temperature): ...

