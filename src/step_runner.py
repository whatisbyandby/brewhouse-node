from threading import Thread
import time
from datetime import datetime, timedelta
from temperature_controller import TemperatureController
import requests


class StepRunner:
    def __init__(self, step_callback):
        self.step_running = False
        self.step_thread = Thread(target=self.loop)
        self.callback = step_callback
        self.step = None
        self.remaining_time = 0
        self.start = None
        self.end = None
        self.temp_controller = TemperatureController()

    def set_step(self, step):
        self.step = step

    def run_step(self):
        if self.step_running:
            return
        self.step_running = True
        self.start = datetime.now()
        self.end = self.start + timedelta(minutes=self.step.hold_time)
        self.step_thread.start()

    def loop(self):
        print('loop')
        while self.step_running:
            current_time = datetime.now()
            if current_time > self.end:
                self.step_running = False
            else:
                time_remaining = self.end - current_time
                self.remaining_time = time_remaining.total_seconds()
                temp_data = self.temp_controller.compare_temp()
                print(temp_data)
                data = {
                    'temp': temp_data,
                    'timestamp': datetime.now().isoformat(' '),
                    'time_remaining': int(round(self.remaining_time)),
                }
                try:
                    requests.post('http://localhost:3001/fermentation', json=data)
                except Exception as error:
                    print(error)
                    return
                time.sleep(1)
        self.step_finished()

    def step_finished(self):
        self.step_thread = Thread(target=self.loop)
        self.callback()

    def stop_step(self):
        self.step_running = False

    def delete_step(self):
        self.step_running = False
        self.step = None
