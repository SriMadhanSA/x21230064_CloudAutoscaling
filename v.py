import matplotlib.pyplot as plt 
import numpy as np
import pickle

import os
os.environ["AWS_ACCESS_KEY_ID"] = "AKIA46NI5ZVIHX4D4NES"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"

import boto3

s3 = boto3.client('s3')
bucket_name = 'x21230064'

class Visualizer:

  def __init__(self, node, model_name):
    self.node = node
    self.model_name = model_name
    
    # Create S3 client
    self.s3 = boto3.client('s3')

  def plot_and_upload(self, fig, filename):
    fig.savefig(filename)
    plt.close(fig)

    bucket_name = 'x21230064'
    self.s3.upload_file(filename, bucket_name, filename) 

  def plot_load_vs_capacity(self):
    load = np.array(self.node.load_history[:50], dtype=np.float32)
    capacity = np.array(self.node.capacity_history[:50], dtype=np.float32)

    fig = plt.figure()
    plt.title(f'load vs capacity ({self.model_name})')
    plt.plot(load,label='load')
    plt.plot(capacity,label="capacity")
    plt.xlabel('Time Interval')
    plt.ylabel('Computation In Flops')
    plt.legend()
    
    self.plot_and_upload(fig, f'Load_vs_Capacity{self.model_name}.png')

  def plot_underuse_overuse(self):
    load = np.array(self.node.load_history[:50], dtype=np.float32)
    capacity = np.array(self.node.capacity_history[:50], dtype=np.float32)

    y = load - capacity

    fig = plt.figure() 
    plt.plot(np.zeros(load.shape))
    plt.title(f'Resource Utilization - Overusage vs Underusage ({self.model_name})')
    plt.plot(y, label='Underuse-Overuse')
    plt.xlabel('Time Interval')
    plt.ylabel('Computation in FLOPs')
    plt.legend()

    self.plot_and_upload(fig, f'Overused_vs_Underused_{self.model_name}.png')

  def plot_combined_error(self):

      #Load error data for different models
        f = open('avg.pkl','rb')
        avg_n1 = pickle.load(f)
        f.close()
        avg_error = np.sum(np.abs(np.array(avg_n1.error_history)))
        f = open('rf.pkl','rb')
        lr_n1 = pickle.load(f)
        f.close()
        lr_error = np.sum(np.abs(np.array(lr_n1.error_history)))
        f = open('svr.pkl','rb')
        svr_n1 = pickle.load(f)
        f.close()
        svr_error = np.sum(np.abs(np.array(svr_n1.error_history)))
        f = open('gru.pkl','rb')
        gru_n1 = pickle.load(f)
        f.close()
        gru_error = np.sum(np.abs(np.array(gru_n1.error_history)))
        f = open('cnn_lstm.pkl','rb')
        gru_ffn_n1 = pickle.load(f)
        f.close()
        gru_ffn_error = np.sum(np.abs(np.array(gru_ffn_n1.error_history)))

        #plot bar graph for the combined error created
        plt.bar(x=['MVG_AVG','RF','SVR','GRU','CNN_LSTM'],height=[avg_error,lr_error,svr_error,gru_error,gru_ffn_error],color=['red','green','blue','orange','cyan','red'],label=[avg_error,lr_error,svr_error,gru_error,gru_ffn_error],width=0.2)
        plt.title("Scaling Error In Each Model ")
        plt.legend()
    
        self.plot_and_upload(fig, 'error_bar_chart.png',)

  def plot_delayed_tasks(self):
    # Load data and compute delayed tasks



        fig = plt.figure()
# Load delayed task data for different models
        f = open('avg.pkl','rb')
        avg_n1 = pickle.load(f)
        f.close()
        delayed = np.array(avg_n1.error_history)
        delayed = delayed[delayed>0]
        avg_error = np.sum(np.sum(delayed))

        f = open('rf.pkl','rb')
        lr_n1 = pickle.load(f)
        f.close()
        delayed = np.array(lr_n1.error_history)
        delayed = delayed[delayed>0]
        lr_error = np.sum(np.sum(delayed))

        f = open('svr.pkl','rb')
        svr_n1 = pickle.load(f)
        delayed = np.array(svr_n1.error_history)
        delayed = delayed[delayed>0]
        f.close()
        svr_error = np.sum(np.sum(delayed))
        
        f = open('gru.pkl','rb')
        gru_n1 = pickle.load(f)
        delayed = np.array(gru_n1.error_history)
        delayed = delayed[delayed>0]
        f.close()
        gru_error = np.sum(np.sum(delayed))
        
        f = open('cnn_lstm.pkl','rb')
        gru_ffn_n1 = pickle.load(f)
        f.close()
        delayed = np.array(gru_ffn_n1.error_history)
        delayed = delayed[delayed>0]
        gru_ffn_error = np.sum(np.sum(delayed))

        #plot bar graph for the delayed tasks values calculated
        plt.bar(x=['MVG_AVG','RF','SVR','GRU','CNN_LSTM'],height=[avg_error,lr_error,svr_error,gru_error,gru_ffn_error],color=['red','green','blue','orange','cyan','red'],label=[avg_error,lr_error,svr_error,gru_error,gru_ffn_error],width=0.2)
        plt.title("Delayed Tasks In Each Model")
        plt.legend()

        self.plot_and_upload(fig, 'delay_bar_chart.png',s3.upload_file(filename, bucket_name, filename))


  def plot_all(self):
    self.plot_load_vs_capacity()
    self.plot_underuse_overuse()
    self.plot_combined_error()

    visualizer = Visualizer(node, 'model')
    visualizer.plot_all()
