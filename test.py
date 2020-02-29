import numpy as np
import pandas as pd

class sqdRegressor:
    def setModel(self, modelName):
        self.usedModel = modelName
        return 1

    def getModel(self):
        print(self.usedModel)
        return self.usedModel

    def trainModel(self):
        #TODO change code to something meaningfull
        for i in range(1, 5):
            print(i)
        return 1

    def __init__(self):
        self.accuracy = np.nan
        self.RMS = np.nan
        self.usedModel = "linreg"


def doPreprocessing(df):
    df2 = df.copy()
    for i in df.head():
        if df[i].dtype == 'object':
            df2[i] = pd.Categorical(df[i])
            df2[i] = df2[i].cat.codes
    return df2

if __name__ == "__main__":
    df = pd.read_excel(r'C:\Users\alexf\PycharmProjects\TF-Test\coolData.xlsx')
    df_allNumbers = doPreprocessing(df)
    print(df)
    print(df_allNumbers)

#   myRegressor = sqdRegressor()
#   myRegressor.getModel()
#   myRegressor.setModel("test")
#   myRegressor.getModel()
#   myRegressor.trainModel()




