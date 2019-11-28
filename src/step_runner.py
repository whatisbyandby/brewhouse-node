import os
from dotenv import load_dotenv
from threading import Thread
import time
from datetime import datetime, timedelta
from confluent_kafka import Producer
from temp_reader import TempReader


load_dotenv()


class StepRunner:
    def __init__(self, step_callback):
        self.step_running = False
        self.step_thread = Thread(target=self.loop)
        self.callback = step_callback
        self.step = None
        self.remaining_time = 0
        self.start = None
        self.end = None
        self.reader = TempReader()
        self.producer = Producer({'bootstrap.servers': os.getenv('KAFKA_HOST') + ':' + os.getenv('KAFKA_PORT')})

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
                self.remaining_time = time_remaining.total_seconds()
                new_readings = self.reader.get_all_readings()
                data = {
                    'temp_readings': new_readings,
                    'timestamp': datetime.now().isoformat(' '),
                    'time_remaining': int(round(self.remaining_time)),
                }
                self.producer.produce('simple_test', key=self.step.name, value=str(data))
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
