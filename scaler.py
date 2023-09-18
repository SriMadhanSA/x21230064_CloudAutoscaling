#scaler component is repsonsible for predecting the autoscaling factor 

class Scaler:
    def __init__(self, model, executing_node):
        self.model = model  # Model inputs the last 5 historical values and outputs the next value
        self.history = []
        self.executing_node = executing_node

    def add_load(self, job):
        self.history.append(job)

    def execute_load(self, job):
        # Get the last 5 historical load values
        load_values = [load.load_factor for load in self.history[-9:]]
        
        # Feed load values into the model to predict the next capacity value
        predicted_capacity = self.model.predict(load_values)
        print(f"Predicted capacity: {predicted_capacity}")

        # Scale the node's capacity based on the predicted capacity
        self.executing_node.scale(predicted_capacity)
        
        # Execute the job on the node
        self.executing_node.execute(job)
        print(f"Job executed on node with load factor: {job.load_factor}")
