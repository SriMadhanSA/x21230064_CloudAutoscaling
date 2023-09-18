#CNN_LSTM MOdel execution

from job import *
from scaler import *
from node import *
from cnn_lstm import *
import time
from visualizer import *

# Create a new Node object for the simulation
n1 = Node()
# Create a Scaler object with the AvgModel (moving average model) and the Node object
scaler = Scaler(CNNLSTMModel(),n1)
# Create a Loader object with the Scaler object
l1 = Loader(scaler)
# Start the Loader thread to simulate job execution
l1.start()
# Wait for the Loader thread to finish execution
l1.join()

# Save the Node object's state to a pickle file for later analysis
import pickle
f = open('cnn_lstm.pkl','wb')
pickle.dump(n1,f)
f.close()

# Create a Visualizer object to generate and save graphs
v1 = Visualizer(n1,"CNN_LSTM")

# Plot the graph of predicted capacity vs load and resource overuse vs underuse
v1.plot_load_vs_capacity()
v1.plot_underuse_overuse()