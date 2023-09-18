#Support vector Regression Model

from sklearn.svm import SVR
import numpy as np

class SVRModel:
    def predict(self,values):
        lr = SVR(kernel="linear")
        x = np.arange(len(values),dtype=np.float32).reshape([9,1])
        y = np.array(values,dtype=np.float32)
        lr.fit(x,y)
        x_p = np.array([[len(values)]],dtype=np.float32)
        predict = lr.predict(x_p).item()
        return predict
    
if __name__=="__main__":
    lr = SVRModel()
    print(lr.predict([1,2,3,4,5,6,7,8,9]))