
# 众筹项目最终筹资绩效预测

发明人：zhuzujun

实验室：USTC-IOM Lab

## 算法目的：

本算法的主要目的是帮助众筹项目筹资者预测项目的最终筹资绩效。根据众筹项目已有筹资信息如是否提供启发式线索（代言、品牌信息等），筹资目标，项目的点赞人数，关注人数，信息更新，评论数量，在筹项目的数量，潜在市场需求等进行预测项目的最终筹资额度或者筹资比例。

## 算法用途

通过这个算法，我们得出在筹资者在决策时，可以根据预计的筹资绩效进行合理配置相应生产材料、计划以及资金预算，比如后期的投资计划等，降低资金预算的不确定性。

## 数据格式

|     变量名                      |     说明                              |     测度方式                                |
|---------------------------------|---------------------------------------|---------------------------------------------|
|     Crowdfunding_performance    |     项目最终筹资绩效                  |     最终筹资金额/筹资目标金额               |
|     Funding_goal                |     发起人设置的筹资目标金额          |     Log10(筹资目标金额)                     |
|     Follower_number             |     获得的关注人数                    |     Log10 (关注项目的人数+1)                |
|     Approver_number             |     获得的点赞人数                    |     Log10 (项目获得点赞的人数+1)            |
|     Information_update          |     信息更新次数                      |     Log10 (项目信息更新的次数+1)            |
|     Comments_number             |     项目筹资期间讨论交流数量          |     Log10 (项目筹资期间讨论交流次数+1)      |
|     Founding_experience         |     目标项目之外发起其他项目次数      |     Log10 (项目发起人以前发起项目个数+1)    |
|     Investing_experience        |      目标项目之外投资其他项目次数     |     Log10 (项目发起人投资其他项目个数+1)    |
|     Delivery_days               |     筹资结束后至发货产品的交货周期    |     Log10 (交货日期+1)                      |
|     Heuristic_cues              |     有无启发式线索                    |     有启发式线索则为1，否则为0              |
|     Competition_intensity       |     同类别在筹项目数量                |     Log10（同类别在筹项目数量）             |






## 算法模型
  回归模型，具体见model.py文件
  
  
## 算法结果
  根据结果，预测项目的最终筹资额度或者筹资比例。


