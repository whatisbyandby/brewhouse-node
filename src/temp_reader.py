from mock_testing import get_mock_sensors

class TempReader:
    def __init__(self):
        self.sensors = get_mock_sensors(3)

    def get_all_readings(self):
        new_reading = {}
        for sensor in self.sensors:
            sensor.get_temperature()
            new_reading[sensor.get_id()] = sensor.get_temperature()

        return new_reading


if __name__ == '__main__':
    reader = TempReader()
    print(reader.get_all_readings())
