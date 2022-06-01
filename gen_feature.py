import math
import pandas as pd
import numpy as np

class data_process():
    def read_data(self,path):
        df = pd.read_excel(path)
        return df

    def generate_features(self,df):
        files_ln = df.files.apply(lambda x:math.log(x + 1,math.e))
        days_ln = df.days.apply(lambda x: math.log(x+ 1,math.e))
        likes_ln = df.likes.apply(lambda x: math.log(x + 1,math.e))
        summary_ln = df.summary.apply(lambda x: math.log(x+ 1,math.e))
        restrict2 = df.restrict2
        skill = df.skill
        category = df.category
        customizer = df.customizer
        volume  = df.volume
        div1 = df.div1
        coupling = df.coupling

        return np.array([files_ln,days_ln,likes_ln,summary_ln,restrict2,skill,category,customizer,volume,div1,coupling]).T


    def forward(self,data_path):
        df = self.read_data(data_path)
        data = self.generate_features(df)

        return data


