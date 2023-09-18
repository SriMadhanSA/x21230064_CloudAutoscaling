import pickle
import csv

# Load data from pickle file
with open('ds.pkl', 'rb') as f:
  x, y = pickle.load(f)

# Open CSV file for writing 
with open('data.csv', 'w', newline='') as csvfile:

  # Create CSV writer
  writer = csv.writer(csvfile)

  # Write column headers
  writer.writerow(['x', 'y'])

  # Write data rows
  for i in range(len(x)):
    writer.writerow([x[i], y[i]])