from threading import Thread
import time
from datetime import datetime, timedelta


class ProcessRunner:
    def __init__(self, duration, callback):
        self.process_running = False
        self.process_thread = Thread(target=self.process)
        self.callback = callback
        self.duration = duration
        self.remaining_time = 0
        self.start = None
        self.end = None

    def run_process(self):
        if self.process_running:
            return
        self.process_running = True
        self.start = datetime.now()
        self.end = self.start + timedelta(minutes=self.duration)
        print('Process end time', self.end)
        self.process_thread.start()

    def process(self):
        while self.process_running:
            current_time = datetime.now()
            if current_time > self.end:
                print('Time is up')
                self.process_running = False
            else:
                time_remaining = self.end - current_time
                self.remaining_time = time_remaining.total_seconds
                print(self.remaining_time())
                time.sleep(1)
        self.process_finished()

    def process_finished(self):
        self.callback()
        self.process_thread.join()

    def stop_process(self):
        self.process_running = False
