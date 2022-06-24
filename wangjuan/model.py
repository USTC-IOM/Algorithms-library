import numpy as np
import torch
import math


class Model():
    def load_parameter(self,param_path):
        param = np.load(param_path,allow_pickle=True)
        return param['param'].tolist()


    def model1(self, dt, param):
        # result = (dt*param).sum()

        result = param['a0']*dt[7] + param['a1']*dt[8] + param['a2']*dt[9] + param['a3']*dt[4] +param['a4']*dt[10] + \
                 param['a5']*dt[13] + param['a6']*dt[11]

        # result = math.exp(result) - 1


        return result

    def model2(self, dt, param,model1_result):
        # result = (dt*param).sum()

        result = -(-param['a0']*model1_result + param['a1']*model1_result*dt[3] + param['a2']*dt[3] + param['a3']*dt[5] +param['a4']*dt[6] + \
                 param['a5']*dt[7] + param['a6']*dt[8] + param['a7'] * dt[9] + param['a8'] * dt[4])

        # result = math.exp(result) - 1

        return result


    def forward(self, model1_param_path,model2_param_path,data):

            param = self.load_parameter(model1_param_path)
            model1_result = self.model1(data,param)
            channel= ''
            if model1_result>0:
                channel =  'Choose the social channel'
            elif model1_result<=0:
                channel =  'Choose the app channel'



            param = self.load_parameter(model2_param_path)
            model2_result = self.model2(data, param,model1_result)
            amount = model2_result
            return channel,amount
