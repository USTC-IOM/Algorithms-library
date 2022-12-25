import numpy as np
import torch


class Model():
    def load_parameter(self,param_path):
        param = np.load(param_path)
        return param


    def build_model(self, dt, param):
        # result = (dt*param).sum()

        result = param['a0'] + param['a1']*dt[0] + param['a2']*dt[1] + param['a3']*dt[2] +param['a4']*dt[3] + \
                 param['a5']*dt[4] + param['a6']*dt[5] + param['a7'] * dt[6] + param['a8'] * dt[7] + \
                 param['a9'] *dt[8] + param['a10'] * dt[9] +param['a11'] *dt[1]* dt[9]


        return result


    def forward(self, param_path,data):
        param = self.load_parameter(param_path)
        result = self.build_model(data,param)

        return result
