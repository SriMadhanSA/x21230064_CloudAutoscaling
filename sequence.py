import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pickle

SCALE = 1 #amplitude of the wave
VARIANCE = 0.1 # deviation from sin wave
INCREMENT = math.pi/36 #increment in each step

# Function to generate sinusoidal cloud workload
def generate_load_value(angle):
    N = math.sin(angle) + (random.random()*VARIANCE)*SCALE
    M = math.cos(angle)*(SCALE)
    return abs(M)+abs(N)

if __name__=="__main__":
    angle = 0.1

    # Lists to store x and y (generated load value) values
    x = []
    y = []

    # Generate load values for 180 time intervals
    for i in range(180):
        angle += INCREMENT
        x.append(angle)
        y.append(generate_load_value(angle))
    
    with open('ds.pkl', 'wb') as f:
     pickle.dump((x, y), f)

    # Plot the generated load values
    plt.plot(x,y)
    plt.xlabel('Time Intervals') 
    plt.ylabel('Resource Required(Load')
    plt.show()