
# 产品销售增量预测算法

发明人：fangjie

实验室：USTC-IOM Lab

## 算法目的：

本算法主要目的是帮助企业预测产品销量增长的速度，主要是考虑企业在不同平台上的各种功能使用行为的差异如何影响天猫平台上使用“门店同款”和“门店自提”功能的作用。

## 算法用途

通过这个算法，我们得出在企业使用“门店同款”和“门店自提”标识如何影响天猫平台上的产品销量增长；而当跨平台的功能使用差异很大时，天猫平台上的销量增长如何受到影响。

## 数据格式

|     变量名             |     说明                |     数据类型    |
|------------------------|-------------------------|-----------------|
|     store_id           |     员工ID              |     int         |
|     week               |     周数                |     Int         |
|     p_id               |     产品ID              |     Str         |
|     ln_delat_amt       |     产品销量增长        |     float       |
|     same               |     门店同款            |     byte        |
|     bops               |     门店自提            |     byte        |
|     vol_rat            |     功能数量差异        |     float       |
|     comp_ratio         |     功能种类差异        |     float       |
|     tm_unq             |     功能独特性          |     float       |
|     video              |     视频                |     byte        |
|     lnprice            |     价格                |     float       |
|     lnpri_mon_sales    |     过去月销量          |     float       |
|     lncolect           |     收藏数              |     float       |
|     store_eva          |     店铺评价1           |     float       |
|     tuikuan            |     店铺评价2           |     float       |
|     witp_tol           |     功能使用数          |     float       |
|     lnpro_no           |     店铺产品数          |     float       |
|     ln_jd_colec        |     京东平台收藏数      |     float       |
|     ln_jd_rew          |     京东平台评论数      |     float       |
|     multip             |     产品相似度          |     float       |
|     price_devia        |     价格差异            |     float       |
|     lntol_same         |     平台内门店同款数    |     float       |
|     lntol_bops         |     平台内门店自提数    |     float       |
|     lnavg_price        |     平台平均价格        |     float       |
|     lnavg_monsales     |     平台平均月销量      |     float       |
|     festival           |     节假日              |     byte        |
|     i.type21           |     产品种类            |     byte        |
|     month              |     月份                |     byte        |


## 数据处理方式
|     变量名             |     预处理方式              |
|------------------------|-----------------------------|
|     Week               |     编码处理                |
|     store_id           |     编码处理                |
|     p_id               |     编码处理                |
|     ln_delat_amt       |     取对数处理              |
|     same               |     哑变量                  |
|     bops               |     哑变量                  |
|     vol_rat            |     连续变量                |
|     comp_ratio         |     连续变量                |
|     tm_unq             |     连续变量                |
|     video              |     哑变量                  |
|     lnprice            |     取对数处理，连续变量    |
|     lnpri_mon_sales    |     取对数处理，连续变量    |
|     lncolect           |     取对数处理，连续变量    |
|     store_eva          |     连续变量                |
|     tuikuan            |     连续变量                |
|     witp_tol           |     连续变量                |
|     lnpro_no           |     取对数处理，连续变量    |
|     ln_jd_colec        |     取对数处理，连续变量    |
|     ln_jd_rew          |     取对数处理，连续变量    |
|     multip             |     连续变量                |
|     price_devia        |   连续变量                  |
|     lntol_same         |     取对数处理，连续变量    |
|     lntol_bops         |     取对数处理，连续变量    |
|     lnavg_price        |     取对数处理，连续变量    |
|     lnavg_monsales     |     取对数处理，连续变量    |
|     festival           |     类别变量                |
|     i.type21           |     哑变量                  |
|     month              |     类别变量                |



## 算法模型
  回归模型，具体见model.py文件
  
  
## 算法结果
  根据结果，帮助企业预测产品销量增长的速度，辅助企业进行决策。
