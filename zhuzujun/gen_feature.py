import math
import pandas as pd
import numpy as np

class data_process():
    def read_data(self,path):
        df = pd.read_excel(path)
        return df

    def generate_features(self,df):
        Funding_goal = df.Funding_goal.apply(lambda x:math.log(x + 1,math.e))
        Heuristic_cues = df.Heuristic_cues
        Follower_number = df.Follower_number.apply(lambda x: math.log(x + 1,math.e))
        Approver_number = df.Approver_number.apply(lambda x: math.log(x+ 1,math.e))
        Information_update = df.Information_update.apply(lambda x: math.log(x + 1, math.e))
        Comments_number = df.Comments_number.apply(lambda x: math.log(x + 1, math.e))
        Founding_experience = df.Founding_experience.apply(lambda x: math.log(x + 1, math.e))
        Investing_experience = df.Investing_experience.apply(lambda x: math.log(x + 1, math.e))
        Delivery_days = df.Delivery_days.apply(lambda x: math.log(x + 1, math.e))
        Platform_competition_intensity = df.Platform_competition_intensity.apply(lambda x: math.log(x + 1, math.e))

        return np.array([Funding_goal,Heuristic_cues,Follower_number,Approver_number,Information_update,Comments_number,Founding_experience,Investing_experience,Delivery_days,Platform_competition_intensity]).T


    def forward(self,data_path):
        df = self.read_data(data_path)
        data = self.generate_features(df)

        return data


