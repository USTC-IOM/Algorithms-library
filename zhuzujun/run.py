
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
    print('Input：Funding_goal: %.3f, Heuristic_cues: %.3f, Follower_number: %.3f, Approver_number: %.3f, Information_update : %.3f,  Comments_number: %.3f, Founding_experience: %.3f, '
          'Investing_experience: %.3f, Delivery_days: %.3f, Platform_competition_intensity: %.3f'%(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],
                                                                      dt[9]))
    result = Model().forward(param_path,dt)
    print('Output: %.3f'%(result))