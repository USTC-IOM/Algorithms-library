
from gen_feature import data_process
from model import Model

'''
data_path: the path of raw path
param_path: the path of parameters of model
'''

data_path = 'data_demo.xlsx'
param_path =  'model_param.npz'
data = data_process().forward(data_path)
for dt in data:
    print('Input：Age: %.3f, AA: %.3f, Prevention: %.3f, Promotion : %.3f,  '
          'BSE: %.3f, Marriage: %.3f, '
          'OG: %.3f'%(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7]))
    result = Model().forward(param_path,dt)
    print('Output: %.3f'%(result))