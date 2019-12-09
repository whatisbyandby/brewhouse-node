from mock_testing import get_mock_sensors


class TempReader:
    def __init__(self):
        self.sensor = get_mock_sensors()

    def get_temp_reading(self):
        return self.sensor.get_temperature()
