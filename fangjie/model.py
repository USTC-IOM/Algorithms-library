import numpy as np
import torch
import math


class Model():
    def load_parameter(self,param_path):
        param = np.load(param_path,allow_pickle=True)
        return param['param'].tolist()


    def model1(self, dt, param):
        # result = (dt*param).sum()

        result = param['a0'] + param['a1']*dt[12] + param['a2']*dt[11] + param['a3']*dt[13] +param['a4']*dt[10] + \
                 param['a5']*dt[3] + param['a6']*dt[14] + param['a7'] * dt[9] + param['a8'] * dt[17] + \
                 param['a9'] *dt[16] + param['a10'] * dt[19] + param['a11'] * dt[20] + param['a12'] *dt[21] + param['a13'] * dt[22] + \
                 param['a14'] * dt[23]+ param['a15'] * dt[27] + param['a16'] * dt[26] + param['a17'] *dt[6] + param['a18'] * dt[7] + param['a19'] * dt[4]

        result = math.exp(result) - 1


        return result

    def model2(self, dt, param):
        # result = (dt*param).sum()

        result = param['a0'] + param['a1']*dt[12] + param['a2']*dt[11] + param['a3']*dt[18] +\
                 param['a4']*dt[24] + param['a5']*dt[25] + param['a6']*dt[12]* dt[18]+ \
                 param['a7'] *dt[12]* dt[24] + param['a8']  *dt[12]* dt[25] + \
                 param['a9'] *dt[11]* dt[25] + param['a10']*dt[11]* dt[18]  + param['a11'] * dt[11] * dt[24]+ \
                 param['a12'] *dt[11]*dt[25] + param['a13'] * dt[13] + param['a14'] * dt[10]+ \
                 param['a15'] * dt[3] + param['a16'] * dt[14] + param['a17'] * dt[9] + param['a18'] * dt[17] + param[
                     'a19'] * dt[16] + param['a20'] * dt[19]+ \
                 param['a21'] * dt[20] + param['a22'] * dt[21] + param['a23'] * dt[22] + param['a24'] * dt[23] + param[
                     'a25'] * dt[27] + param['a26'] * dt[26]+ param['a27'] * dt[6] + param['a28'] * dt[7] + param['a29'] * dt[4]


        result = math.exp(result) - 1

        return result


    def forward(self, model1_param_path,model2_param_path,data):

            param = self.load_parameter(model1_param_path,)
            model1_result = self.model1(data,param)



            param = self.load_parameter(model2_param_path, )
            model2_result = self.model2(data, param)

            return model1_result,model2_result
