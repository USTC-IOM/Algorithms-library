
from gen_feature import data_process
from model import Model

'''
data_path: the path of raw path
param_path: the path of parameters of model
'''

data_path = 'data_demo.xlsx'
param_path =  'parameters.npz'
data = data_process().forward(data_path)
for dt in data:
    print('Input：files_ln: %.3f, dayes_ln: %.3f, likes_ln: %.3f, summary_ln: %.3f, restrict2: %.3f, skill: %.3f, category: %.3f, '
          'customizer: %.3f, volume: %.3f, div1: %.3f, coupling: %.3f'%(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],
                                                                      dt[9],dt[10]))
    result = Model().forward(param_path,dt)
    print('Output: %.3f'%(result))