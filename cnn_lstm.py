#CNN_LSTM Model

import tensorflow as tf
import numpy as np

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu,True)

class CNNLSTMModel:
    def __init__(self):
        self.model = tf.keras.models.load_model("cnn_lstm")

    def predict(self,values):
        x = tf.constant(values,dtype=tf.float32)
        x = tf.reshape(x,shape=[1,9])
        predict = self.model.predict(x)
        return predict.item()
    
if __name__=="__main__":
    g = CNNLSTMModel()

    import pickle
    f = open("ds.pkl",'rb')
    x,y = pickle.load(f)
    f.close()
    print(g.predict(x[:1]))
    print(y[0])