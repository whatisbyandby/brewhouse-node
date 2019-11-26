from threading import Thread
import time
from datetime import datetime, timedelta


class StepRunner:
    def __init__(self):
        self.step_running = False
        self.step_thread = Thread(target=self.loop)
        self.callback = None
        self.step = None
        self.remaining_time = 0
        self.start = None
        self.end = None

    def set_step(self, step):
        self.step = step

    def run_step(self):
        if self.step_running:
            return
        self.step_running = True
        self.start = datetime.now()
        self.end = self.start + timedelta(minutes=self.step.hold_time)
        print('Process end time', self.end)
        self.step_thread.start()

    def loop(self):
        while self.step_running:
            current_time = datetime.now()
            if current_time > self.end:
                self.step_running = False
            else:
                time_remaining = self.end - current_time
                self.remaining_time = time_remaining.total_seconds
                print(self.remaining_time())
                time.sleep(1)
        self.step_finished()

    def step_finished(self):
        self.callback()
        self.step_thread.join()

    def stop_step(self):
        self.step_running = False

    def delete_step(self):
        self.step_running = False
        self.step = None
