from enum import Enum


class TempControllerStatus(Enum):
    COOLER = 0
    HEATER = 1
    CORRECT = 2
    ERROR = 3
