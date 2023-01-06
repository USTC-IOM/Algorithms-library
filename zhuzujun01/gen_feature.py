import math
import pandas as pd
import numpy as np

class data_process():
    def read_data(self,path):
        df = pd.read_excel(path)
        return df



    def generate_features(self,df):
        Funding_performance = df.Funding_performance.apply(lambda x:math.log(x + 1,math.e))
        Funding_goal = df.Funding_goal.apply(lambda x: math.log(x + 1,math.e))
        Available_days = df.Available_days.apply(lambda x: math.log(x + 1,math.e))
        Information_update = df.Information_update.apply(lambda x: math.log(x + 1, math.e))
        Interactive_message = df.Interactive_message.apply(lambda x: math.log(x+ 1,math.e))

        Competition_intensity = df.Competition_intensity.apply(lambda x: math.log(x + 1, math.e))
        Approving = df.Approving.apply(lambda x: math.log(x + 1, math.e))
        Foundation_experience = df.Foundation_experience
        Investing_experience = df.Investing_experience
        Delivery_days = df.Delivery_days.apply(lambda x: math.log(x + 1, math.e))

        return np.array([Funding_performance,Funding_goal,Available_days,Information_update,
                         Interactive_message,Competition_intensity,Approving,Foundation_experience,
                         Investing_experience,Delivery_days]).T


    def forward(self,data_path):
        df = self.read_data(data_path)
        data = self.generate_features(df)

        return data


