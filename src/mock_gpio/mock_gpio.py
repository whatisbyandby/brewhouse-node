from mock_pin import MockPin
from pin_type import PinType
from mock_state import MockState

class MockGPIO:
    def __init__(self):
        self.pins = []

    def setup(self, pin_number, pin_type):
        new_pin = MockPin(pin_number, pin_type)
        self.pins.append(new_pin)

    def output(self, pin_number, new_state):
        for pin in self.pins:
            if pin.pin_number == pin_number:
                pin.set_state(new_state)
                return True
        return False

    def input(self, pin_number):
        for pin in self.pins:
            if pin.pin_number == pin_number:
                return pin.get_state()
        return None

    def get_all_pins(self):
        pin_state = {}
        for pin in self.pins:
            pin_state[pin.pin_number] = pin.current_state
        return pin_state


if __name__ == '__main__':
    gpio = MockGPIO()
    gpio.setup(2, PinType.OUTPUT)
    gpio.setup(3, PinType.OUTPUT)
    gpio.output(2, MockState.HIGH)
    gpio.output(3, MockState.LOW)
    gpio.output(3, MockState.HIGH)

    print(gpio.get_all_pins())
    print(MockState.LOW.value is False)
