
from gen_feature import data_process
from model import Model

'''
data_path: the path of raw path
param_path: the path of parameters of model
'''

data_path = 'fangjie.xlsx'
model1_param =  'model1_param.npz'
model2_param =  'model2_param.npz'
data = data_process().forward(data_path)
for dt in data:
    print('Input: week: %.3f, store_id: %.3f, p_id: %.3f, lnpri_mon_sales: %.3f, festival: %.3f, month: %.3f,\
           lnavg_price: %.3f, lnavg_monsales: %.3f, lnreview: %.3f, store_eva: %.3f, lnprice: %.3f,\
           bops: %.3f, same: %.3f, video: %.3f, lncolect: %.3f, ln_delat_amt: %.3f, witp_tol: %.3f,\
           tuikuan: %.3f, vol_rat: %.3f, lnpro_no: %.3f, ln_jd_colec: %.3f, ln_jd_rew: %.3f, multip: %.3f,\
           price_devia: %.3f, comp_ratio: %.3f, tm_unq: %.3f, lntol_bops: %.3f, lntol_same: %.3f,\
           type21: %.3f' % (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6], dt[7], dt[8], dt[9], dt[10], dt[11], dt[12], dt[13], dt[14],
    dt[15], dt[16], dt[17], dt[18], dt[19], dt[20], dt[21], dt[22], dt[23], dt[24], dt[25], dt[26], dt[27], dt[28]))

    model1_result,model2_result = Model().forward(model1_param,model2_param,data)
    print('Output: The model without moderators: %.3f. The model with moderators: %.3f. '%(model1_result,model2_result))