import time
import ctypes
from ctypes import wintypes


global charging


def check_voltage():
	pass

def check_battery():
	import ctypes
	from ctypes import wintypes

	class SYSTEM_POWER_STATUS(ctypes.Structure):
		_fields_ = [
			('ACLineStatus', wintypes.BYTE),
			('BatteryFlag', wintypes.BYTE),
			('BatteryLifePercent', wintypes.BYTE),
			('Reserved1', wintypes.BYTE),
			('BatteryLifeTime', wintypes.DWORD),
			('BatteryFullLifeTime', wintypes.DWORD),
		]

	SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

	GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
	GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
	GetSystemPowerStatus.restype = wintypes.BOOL

	status = SYSTEM_POWER_STATUS()
	if not GetSystemPowerStatus(ctypes.pointer(status)):
		raise ctypes.WinError()
	if status.ACLineStatus == 1:
		charging = True
	else:
		charging = False
	# print('ACLineStatus', status.ACLineStatus)
	if charging == True:
		print('Battery is charging and is at ' + str(status.BatteryLifePercent) + '%.')
	else:
		print('Battery is not charing and is at ' + str(status.BatteryLifePercent) + '%.')
	# print('BatteryFlag', status.BatteryFlag)
	# print('BatteryLifePercent', status.BatteryLifePercent)
	# print('BatteryLifeTime', status.BatteryLifeTime)
	# print('BatteryFullLifeTime', status.BatteryFullLifeTime)

def start_truck():
	pass

def stop_truck():
	pass



check_battery()

