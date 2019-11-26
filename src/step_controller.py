from step_runner import StepRunner
from step import Step


class StepController:
    def __init__(self):
        self.steps = []
        self.step_runner = StepRunner()

    def get_steps(self):
        return self.steps

    def set_steps(self, step_data):
        for step in step_data:
            new_step = Step(**step)
            self.steps.append(new_step)
        return self.steps

    def update_step(self, new_step_data):
        self.current_step = new_step_data
        return self.current_step

    def delete_step(self):
        self.step_runner.delete_step()
        return None

    def start(self):
        self.step_runner.run_step()
        print('Step Running')

    def stop(self):
        self.step_runner.stop_step()
        print('process stopped')

