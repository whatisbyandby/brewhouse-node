from mock_temp_sensor import MockTempSensor


def get_mock_sensors(num_sensors):
    sensor_list = []
    for _ in range(num_sensors):
        sensor_list.append(MockTempSensor())
    return sensor_list
