from temp_reader import TempReader
from temp_controller_status import TempControllerStatus


class TemperatureController:
    def __init__(self, target_temp=65, temp_range=1):
        self.reader = TempReader()
        self.target_temp = target_temp
        self.temp_range = temp_range
        self.current_mode = TempControllerStatus.CORRECT

    def set_target_temp(self, new_target_temp):
        self.target_temp = new_target_temp

    def get_target_temp(self):
        return self.target_temp

    def set_temp_range(self, new_temp_range):
        self.temp_range = new_temp_range

    def get_temp_range(self):
        return self.temp_range

    def compare_temp(self):
        current_temp = self.reader.get_temp_reading()
        if current_temp > self.target_temp + self.temp_range and self.current_mode != TempControllerStatus.COOLER:
            self.turn_cooler_on()
        elif current_temp < self.target_temp - self.temp_range and self.current_mode != TempControllerStatus.HEATER:
            self.turn_heater_on()
        elif current_temp > self.target_temp:
            self.turn_cooler_on()
        elif current_temp < self.target_temp:
            self.turn_heater_on()
        else:
            self.correct_temp()
        return current_temp, self.target_temp, self.current_mode.name

    def turn_cooler_on(self):
        if self.current_mode == TempControllerStatus.COOLER:
            return
        self.current_mode = TempControllerStatus.COOLER

    def turn_heater_on(self):
        if self.current_mode == TempControllerStatus.HEATER:
            return
        self.current_mode = TempControllerStatus.HEATER

    def correct_temp(self):
        if self.current_mode == TempControllerStatus.CORRECT:
            return
        self.current_mode = TempControllerStatus.CORRECT

    def error_mode(self):
        print('There was an error')
        pass
