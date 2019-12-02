import unittest
from step_controller import StepController
from test_utils import get_test_steps

test_steps = [
    {
        'name': 'First Step',
        'hold_time': 1,
        'start_temp': 60,
        'end_temp': 60
    },
    {
        'name': 'Second Step',
        'hold_time': 1,
        'start_temp': 60,
        'end_temp': 60
    }
]


class StepControllerTest(unittest.TestCase):

    def setUp(self):
        self.controller = StepController()
        self.controller.set_steps(get_test_steps(test_steps))

    def test_list_length_parsing(self):
        self.assertEqual(len(self.controller.steps), 2,
                         'incorrect step list length')

    def test_hold_time_parsing(self):
        for index, step in enumerate(self.controller.steps):
            self.assertEqual(step.hold_time, test_steps[index]["hold_time"], 'incorrect hold time parsing')

    def test_start_temp_parsing(self):
        for index, step in enumerate(self.controller.steps):
            self.assertEqual(step.start_temp, test_steps[index]["start_temp"], 'incorrect start temp parsing')
