from bluepy.btle import Peripheral, DefaultDelegate, UUID
import time

class BatteryService:

    def _init_(self, battery_level=100):
        self.battery_level = battery_level
        self.service_uuid = UUID("0000180f-0000-1000-8000-00805f9b34fb")
        self.char_uuid = UUID("00002a19-0000-1000-8000-00805f9b34fb")

    def set_battery_level(self, level):
        self.battery_level = level

    def get_battery_level(self):
        return self.battery_level

class BatteryCharacteristic(DefaultDelegate):

    def _init_(self, service):
        self.service = service
        self.char_uuid = service.char_uuid
        self.handle = None
        DefaultDelegate._init_(self)

    def handleNotification(self, cHandle, data):
        print("Battery Level notification received. Data:", data)

    def handleRead(self, data):
        print("Battery Level read request received")
        return self.service.get_battery_level().to_bytes(1, byteorder='little')

class BatteryPeripheral:

    def _init_(self, service):
        self.service = service
        self.peripheral = Peripheral()
        self.peripheral.setDelegate(BatteryCharacteristic(self.service))

    def start(self):
        self.peripheral.addService(self.service)
        self.peripheral.startAdvertising(0)
        while True:
            self.peripheral.waitForNotifications(0.1)

if _name_ == '_main_':
    service = BatteryService()
    battery_characteristic = BatteryCharacteristic(service)
    battery_service = BatteryPeripheral(service)
    battery_service.start()