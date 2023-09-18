#loaded component is responsible for generating jobs with varying loads

import time
import datetime
import threading
from sequence import *

# class to represent a job
class Job:
    def __init__(self, load_factor, cycle_number):
        self.load_factor = load_factor      # Load factor of the job
        self.cycle_number = cycle_number    # Cycle number when the job was created

# class to simulate job loading and execution
class Loader(threading.Thread):
    def __init__(self, scaler):
        self.angle = 0.0        # Angle for generating load values
        self.cycle = 0
        self.scaler = scaler    # Scaler component for managing resource scaling
        for i in range(9):
            self.add_load()     # Initialize the loader with initial load values
        threading.Thread.__init__(self, name="loader")

    def add_load(self):
        # Generate a load value based on the angle and create a job instance
        load = generate_load_value(self.angle)
        job = Job(load, self.cycle)
        self.scaler.add_load(job)   # Add the job to the scaler's historical data
        self.angle += INCREMENT     # Increment the angle for the next load value
        self.cycle += 1             
        print(f"Added job with load value: {load}, Cycle: {self.cycle}")
        return job

    def run(self):
        counter = 0
        print("Loader is executing")
        while counter <= 990:
            job = self.add_load()           # Add a new job with load value
            print("Executing scaler for job load:", job.load_factor)
            self.scaler.execute_load(job)   # Execute resource scaling based on job load
            print("Scaler executed for job load:", job.load_factor)
            counter += 1
            print()                         # empty line to separate cycles

    def join(self, timeout=None):
        threading.Thread.join(self, timeout)
