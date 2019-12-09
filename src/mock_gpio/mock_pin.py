from mock_state import MockState

class MockPin:
    def __init__(self,  pin_number, pin_type, default_state=MockState.LOW):
        self.type = pin_type
        self.default_state = default_state
        self.pin_number = pin_number
        self.current_state = default_state

    def set_state(self, state):
        self.current_state = state

    def get_state(self):
        return self.current_state
