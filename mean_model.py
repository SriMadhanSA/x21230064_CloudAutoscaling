# Rule-based (Moving_average) Model

class AvgModel:
    def predict(self,values):
        return sum(values)/len(values)  # calculate average of the values

if __name__=="__main__":
    am = AvgModel()
    print(am.predict([1,2,3,4,5]))