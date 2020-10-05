# Deep Closet Point: Learning Representation for Point Cloud Registration

## 摘要
传统ICP算法容易陷入局部最优，对于初始误差比较大的情况不适用；
本文提出的DCP算法由以下3部分组成：
1. a Point cloud embedding network
2. 注意力模块+pointer生成层，用于近似进行组合匹配
3. SVD层用于计算最终的刚体变换

## 相关工作
### 点云配准算法
ICP
Go-ICP
Descriptor learning methods
3DMatch
3DFeatNet
3DSmoothNet

### 基于点云和图学习的方法
