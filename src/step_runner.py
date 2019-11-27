import os
from dotenv import load_dotenv
from threading import Thread
import time
from datetime import datetime, timedelta
from confluent_kafka import Producer

load_dotenv()


class StepRunner:
    def __init__(self):
        self.step_running = False
        self.step_thread = Thread(target=self.loop)
        self.callback = lambda message: print(message)
        self.step = None
        self.remaining_time = 0
        self.start = None
        self.end = None
        self.producer = Producer({'bootstrap.servers': os.getenv('KAFKA_HOST') + ':' + os.getenv('KAFKA_PORT')})

    def set_step(self, step):
        self.step = step

    def run_step(self):
        if self.step_running:
            return
        self.step_running = True
        self.start = datetime.now()
        self.end = self.start + timedelta(minutes=1)
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
                self.producer.produce('simple_test', key='time_remaining', value=str(self.remaining_time))
                time.sleep(1)
        self.step_finished()

    def step_finished(self):
        self.callback('Finished')

    def stop_step(self):
        self.step_running = False

    def delete_step(self):
        self.step_running = False
        self.step = None
