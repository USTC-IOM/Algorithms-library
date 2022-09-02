# 产品再创新判别算法

发明人：liuyang and chenwei

实验室：USTC-IOM Lab

## 算法目的：

根据产品的模块数量，模块异质性以及模块之间的相互依赖性来预测该产品在多大程度下会被用来进行再创新并产生更加新颖的产品设计。

## 算法用途

通过这个算法，我们得出在企业决策时，应当注重考虑将产品进行模块化设计，并提供在线设计工具来帮助用户进行再创新。

## 数据格式

|     变量名          |     说明                                            |     数据类型       |
|---------------------|-----------------------------------------------------|--------------------|
|     files           |     平台上每个design的文件数量                      |     整形（int）    |
|     Category        |     平台上每个design所在的category                  |     整形（int）    |
|     Restrict        |     平台上每个design的license                       |     整形（int）    |
|     Days            |     平台上每个design在平台上开放下载的天数          |     整形（int）    |
|     Likes           |     平台上每个design的流行程度                      |     整形（int）    |
|     Summary         |     平台上每个design描述的字数                      |     整形（int）    |
|     Skill           |     平台上每个design设计师的技能                    |     整形（int）    |
|     Customizer      |     平台上每个design是否被user   toolkit支持        |     整形（int）    |
|     Div1            |     平台上每个design所包含的模块的多样性            |     整形（int）    |
|     Volume          |     平台上每个design所包含的模块的数量              |     整形（int）    |
|     Coupling        |     平台上每个design所包含的模块之间的相互依赖性    |     整形（int）    |
|     Sum_funcdis3    |     平台上每个design所产生的衍生品的新颖性          |     整形（int）    |


## 数据处理方式
|     变量名        |     预处理方式                  |
|-------------------|---------------------------------|
|     Files_ln      |     对files数据进行log处理      |
|     Days_ln       |     对days数据进行log处理       |
|     Likes_ln      |     对likes数据进行log处理      |
|     Summary_ln    |     对summary数据进行log处理    |



## 算法模型
  回归模型，具体见model.py文件
  
  
## 算法结果
  根据结果，辅助企业进行决策。


