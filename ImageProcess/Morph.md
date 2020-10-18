# 形态学

形态学注重的是在位置上的膨胀扩孔导致的灰度变化，不强调灰度上的纵向变化

## 二值图像形态学

* dilation：每一个为1的像素膨胀为SE那么大，盖章一样
* erotion：能够将SE匹配进去（SE和原图像素完全匹配）的像素才能被保留。
* open：比SE小的结构或尖角都会被抹除
* close：比SE小的空洞或凹陷会被填充
形态学的加速：大的SE分解成小的SE
* hit-and-miss：
在前景上hit，在背景上 miss
和前景match，和背景不match
可以求取：独立像素、端点、轮廓点
* pattern spectrum：不同尺寸大小的筛子（SE）筛谷物（图像物体）
测量物体不同尺寸的分布
DST distance size transformation：opening image-original image
* recursive dilation
* recursive erosion：计算距离函数
* Distance Transform 距离函数
* Skeleton 骨架 保留拓扑结构，距离边缘最远的点组成的 
* Shape Inspection：使用特定形状的SE进行opening筛选图中的特定结构

## 灰度图的形态学

* dilation：
用SE，盖章一样把SE和原图灰度相加，滑过之后取最大值；
白区被膨胀，整体变亮；
* erosion：
用SE，反方向盖章一样把原图减去SE，滑过之后取最小值；
白区被腐蚀，图像变暗；
* openning：
打掉了白色的尖锐部分（大小由SE尺寸决定）；
SE在原图从下往上fit图像的pattern
* closing：
填埋了暗色的狭小区域；
SE在原图从上往下fit图像的pattern

## 形态学重建（受约束的膨胀）

Marker M& Mask V：对M进行反复膨胀，使用V对其进行约束
M一旦超出V，就会被和V交集给抹掉

步骤：

* 1.open除噪，指定Marker
* 2.M进行膨胀，和V做交集
* 3.反复进行，知道M(t-1)=M(t)，停止

SE要足够小；打断一些链接；

## 灰度形态学重建

步骤

* 1.灰度图像的marker g上做灰度dilation
* 2.保证Marker没有超出灰度空间f的制约
* 3.重复1，2，直到稳定

OBR:open+reconstuction：去头皮

CBR:close+reconstruction：白质增强
