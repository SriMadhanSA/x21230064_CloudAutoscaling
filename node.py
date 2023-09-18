#node component is where the generated jobs execute on virtual instances


# class to represent a virtual machine node
class Node:
    def __init__(self):
        self.error_history = []         # (Job load - node capacity)
        self.load_history = []          # historical job load factors
        self.capacity_history = []      # historical node capacity values
        self.capacity = 0               # Current capacity of the node

    # scale the capacity of the node based on a given value
    def scale(self, value):
        self.capacity = value                       # Update the capacity of the node
        self.capacity_history.append(value)         # Add the new capacity value to the history
        print(f"Node capacity scaled to: {value}")  

    # execute a job on the node
    def execute(self, job):
        load_difference = job.load_factor - self.capacity  
        self.error_history.append(load_difference)          # Adding load difference to the error history
        self.load_history.append(job.load_factor)           # Adding the job load factor to the load history
        
        if load_difference < 0:
            print(f"Job with load factor {job.load_factor} executed successfully.")
        else:
            print(f"Job with load factor {job.load_factor} delayed due to resource underuse.")
