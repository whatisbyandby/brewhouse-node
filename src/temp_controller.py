import json
from process_runner import ProcessRunner
from step import Step



class TempController:
    def __init__(self):
        self.current_step = None
        self.step_runner = ProcessRunner(1, self.get_next_step)

    def get_next_step(self):
        print('This is the callback')
        #This can be a REST call to get the next step

    def get_step(self):
        return self.current_step

    def add_step(self, step):
        self.current_step = Step(**step)
        return self.current_step

    def update_step(self, new_step_data):
        self.current_step = new_step_data
        return self.current_step

    def delete_step(self):
        self.current_step = None
        return None

    def run_step(self):
        self.step_runner.run_process()
        print('Step Running')

    def stop(self):
        self.step_runner.stop_process()
        print('process stopped')
