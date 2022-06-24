import math
import pandas as pd
import numpy as np

class data_process():
    def read_data(self,path):
        df = pd.read_csv(path)
        return df



    def forward(self,data_path):
        df = self.read_data(data_path)
        data = df.values

        return data


