from step_runner import StepRunner
from step import Step


class StepController:
    def __init__(self):
        self.steps = []
        self.current_step = 0
        self.step_runner = StepRunner(self.next_step)

    def get_steps(self):
        return self.steps

    def set_steps(self, step_data):
        for step in step_data:
            new_step = Step(**step)
            self.steps.append(new_step)
        return self.steps

    def update_step(self, new_step_data):
        return self.current_step

    def delete_step(self):
        self.step_runner.delete_step()
        return None

    def start(self):
        self.step_runner.set_step(self.steps[self.current_step])
        self.step_runner.run_step()
        print('Step ' + str(self.current_step) + ' Running')

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

