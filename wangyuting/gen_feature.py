import math
import pandas as pd
import numpy as np

class data_process():
    def read_data(self,path):
        df = pd.read_csv(path)
        return df



    def generate_features(self,df):
        Age = df.Age
        AA = df.AA
        Prevention = df.Prevention
        Promotion = df.Promotion
        BSE = df.BSE
        Marriage = df.Marriage
        OG = df.OG


        return np.array([Age,AA,Prevention,Promotion,BSE,Marriage,OG]).T


    def forward(self,data_path):
        df = self.read_data(data_path)
        data = self.generate_features(df)

        return data


