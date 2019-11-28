import random
import uuid


class MockTempSensor:
    def __init__(self, low_range=60, high_range=70):
        self.id = uuid.uuid4()
        self.low_range = low_range
        self.high_range = high_range

    def get_id(self):
        return str(self.id)

    def get_temperature(self):
        new_reading = random.uniform(self.low_range, self.high_range)
        return new_reading


if __name__ == '__main__':
    sensor = MockTempSensor()
    print(sensor.get_id())
    print(sensor.get_temperature())