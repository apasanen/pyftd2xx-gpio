import ftd2xx
import pprint

devNum = ftd2xx.createDeviceInfoList()
getDeviceInfoDetail = [ftd2xx.getDeviceInfoDetail(devnum=i, update=False) for i in range(devNum)]
dev = ftd2xx.open(0)
dev.setChars(False, 0, False, 0)
dev.setTimeouts(5000, 5000)
dev.setLatencyTimer(2)
dev.setBaudRate(300)
AsynchronousBitBang = 0x01
dev.setBitMode(0x00, AsynchronousBitBang)

value = None
while True:
	rxBytes = dev.getQueueStatus()
	if rxBytes:
		rxbuffer = dev.read(rxBytes);
		newValue = rxbuffer[-1]
		if value != newValue:
			print(hex(newValue))
			value = newValue
