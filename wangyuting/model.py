import numpy as np
import torch
import math

class Model():
    def load_parameter(self,param_path):
        param = np.load(param_path)
        return param


    def build_model(self, dt, param):



        result = math.e**(param['a4']*dt[2]+param['a5']*dt[3]+param['a7']*dt[6]*dt[2]+param['a8']*dt[6]* dt[3])

        return result


    def forward(self, param_path,data):
        param = self.load_parameter(param_path)
        result = self.build_model(data,param)

        return result
