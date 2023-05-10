from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import math

df = pd.read_csv('redwine.csv')

class Model:

    def __init__(self) -> None:

        self.df = df

        self.x, self.y = self.df.drop(columns=['quality']), self.df['quality']
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x,
                                                                                self.y,
                                                                                test_size=0.25,
                                                                                random_state=45)

        self.model = RandomForestClassifier()
        self.model.fit(self.x_train, self.y_train)

    def predict_model(self, param_df):
        
        return self.model.predict(param_df)


    def make_param(self, params):
        
        param_df = {}
        for i in df.columns[:-1]:
            param_df[i] = []

        key = [i for i in param_df]
        for i in range(len(key)):
            param_df[key[i]].append(params[i])

        return pd.DataFrame(param_df)
    
    def model_evaluation(self):

        mse = np.square(np.subtract(self.y_test,self.model.predict(self.x_test))).mean() 
        rmse = math.sqrt(mse)
        rsq = self.model.score(self.x_test, self.y_test)
 
        ev_df = {'Mean Squared Error':[mse],
                 'Root Mean Squared Error':[rmse],
                 'R-Square':[rsq]}
        return pd.DataFrame(ev_df)
