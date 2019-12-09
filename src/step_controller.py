from step_runner import StepRunner
from test_utils import get_test_steps
from step import Step


class StepController:
    def __init__(self):
        self.steps = []
        self.current_step = 0
        self.step_runner = StepRunner(self.next_step)

    def get_steps(self):
        return self.steps

    def set_steps(self, steps):
        new_steps = []
        for step in steps:
            new_step = Step(**step)
            new_steps.append(new_step)
        self.steps = new_steps
        return self.steps

    def start(self):
        if len(self.steps) > 0:
            self.step_runner.set_step(self.steps[self.current_step])
            self.step_runner.run_step()
            return True
        else:
            return False

    def next_step(self):
        self.current_step = self.current_step + 1
        if len(self.steps) > self.current_step:
            self.start()
        else:
            self.current_step = 0
            self.steps = []

    def stop(self):
        self.step_runner.stop_step()
        print('process stopped')
