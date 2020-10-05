# 介绍
Mesh Registration开源代码库MeshMonk的代码说明。

# 内容
## Downsampler：mesh降采样

>1. 基于OpenMesh的Decimater 实现
>2. 将边缘的点锁住不进行处理

## NeighbourFinder：邻域检索，并返回邻接点的距离

1. 基于nanoflann实现
2. 设置源点：set_source_points
3. 设置检索点：set_queried_points
4. 建立kdtree索引：new nanoflann::KDTreeEigenMatrixAdaptor<VecMatType>(*_inSourcePoints,_leafSize)
5. 执行搜索：_kdTree->index->findNeighbors()

## BaseCorrespondenceFilter ：寻找对应点

### CorrespondenceFilter

1. 设置浮动点：set_floating_input
2. 设置目标点：set_target_points
3. 设置相关参数：搜索邻域点个数、flag阈值（设置能够形成点对的相似性阈值要求）
4. 更新affinity matrix：类似于邻接矩阵，根据距离计算target上点到source上点的关联度（只记录最邻近的N个点，稀疏矩阵）。
5. update：核心函数
   > 1. 更新affinity矩阵
   > 2. 根据affnity matrix得到conrrespondence flag（_affinity_to_correspondences()）
   >     *（矩阵相乘，作用相当于最近N点的加权平均，使用flagThreshold=0.9进行cut off）*

### SymmetricCorrespondenceFilter：通过双向确定Correspondence

1. _pushFilter
2. _pullFilter

## InlierDetector：内点检测

1. _smoothingWeights：_
2. ioProbability（inlier weights）：

## RigidTransformer：刚体变换，基于SVD分解

1. 设置输入：set_input：设置对应点的features和点的weight

2. 设置输出：set_output：设置变换后的feature

3. 设置参数：set_parameters，scaling：是否包含尺度变换

4. rigid变换：

   > 1. 计算两个点云的中心
   > 2. 计算协方差矩阵
   > 3. 计算抗对称矩阵
   > 4. 使用抗对称矩阵构建delta
   > 5. 计算Q
   >6. 通过求Q的最大特征值的特征向量来计算旋转四元数（SVD分解）。
   >7. 构造旋转矩阵
   >8. 估计尺度
   >9. 计算平移量
   >10. 计算整个旋转矩阵
   >11. 应用变换

## RigidRegistration：刚体配准

1. 设置输入：输入特征点对Features、Flags；

2. 设置参数：

   > symmetric：是否双向定点对
   > numNeighbours：进行领域搜索时的领域点数
   > flagThreshold：确定点对关系时的阈值（用于false matching reduction）
   > equalizePushPull
   > kappaa
   > inlierUseOrientation
   > numIterations
   > useScaling
   > 
3. updata（执行函数，ICP配准）
   > 1. 寻找点对：SymmetricCorrespondenceFilter或CorrespondenceFilter
   > 2. Inlier点滤波：inlierDetector
   > 3. 刚体变换：rigidTransformer
   > 4. 循环3-5。

## ViscoElasticTransformer：粘弹性变换

1. 设定输入：set_input，对应点Features，weights、Flags、浮动图像的Faces

2. 设定输出：set_output，浮动图像变换后的特征

3. 设定参数：

   > 1. numNeighbours：领域点个数设定
   >    sigma
   > 2. viscousIterations：粘性形变迭代次数
   > 3. elasticIterations：弹性形变迭代次数

4. 执行变换：updata
   > 1. _update_neighbours：使用flann更新，邻域点情况
   > 2. _update_smoothing_weights：根据邻域点情况确定邻域点的权重
   > 3. _update_viscously：粘性变换
   > 4. _update_elastically：弹性变换
   > 5. _update_outlier_transformation：对outlier点进行变换，基于扩散过程
   > 6. _apply_transformation
7. 返回形变场：get_transformation

## NonrigidRegistration：非刚性配准
1. CorrespondenceFilter/SymmetricCorrespondenceFilter 寻找点对

2. InlierDetector：排除离群点

3. ViscoElasticTransformer：粘弹变换

4. 迭代以上步骤

   

## ScaleShifter：

服务于PyramidNonrigidRegistration，尺度转换 

## PyramidNonrigidRegistration：多尺度非刚性配准
1. Downsampler：降采样floating
2. Downsampler：降采样Target
3. ScaleShifter：迁移floating上一级尺度的特征到当前尺度
4. NonrigidRegistration：nonrigid配准
5. 循环以上
