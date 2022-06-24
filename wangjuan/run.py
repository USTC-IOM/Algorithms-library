
from gen_feature import data_process
from model import Model

'''
data_path: the path of raw path
param_path: the path of parameters of model
'''

data_path =r'..\wangjuan\wangjuan.csv'
model1_param =  'model1_param.npz'
model2_param =  'model2_param.npz'
data = data_process().forward(data_path)
for dt in data:
    print('Input: CustomerID: %.3f, Basket_Value: %.3f, Social_Channel: %.3f, Non_Work_Hour: %.3f, First_Tier_City: %.3f, Seasonality: %.3f, Recency: %.3f, Frequency: %.3f, Monetary: %.3f, Accu_dis_per: %.3f, Relative_Social: %.3f,\
           No_Prior_Tran: %.3f, Month: %.3f, SocialID: %.3f' % (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11], dt[12], dt[13]))

    channel,amount = Model().forward(model1_param,model2_param,dt)
    print('The channel:{}. The amount:{}'.format(channel,amount))
