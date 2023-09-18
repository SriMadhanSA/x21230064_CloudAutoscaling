#Random Forest Model

from sklearn.ensemble import RandomForestRegressor
import numpy as np

class RFModel:
    def predict(self,values):
        lr = RandomForestRegressor(max_depth=2, random_state=0)
        x = np.arange(len(values),dtype=np.float32).reshape([9,1])
        y = np.array(values,dtype=np.float32)
        lr.fit(x,y)
        x_p = np.array([[len(values)]],dtype=np.float32)
        predict = lr.predict(x_p).item()
        return predict
    
if __name__=="__main__":
    lr = RFModel()
    print(lr.predict([1,2,3,4,5,6,7,8,9]))