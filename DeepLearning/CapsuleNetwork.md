# 胶囊网络（Capsule Network）

将神经元替换为胶囊，就是胶囊网络。

## 背景：为什么会有胶囊网络？

### CNN中没有可用的空间信息

虽然随着卷积网络的层数的加深，网络可以学到更为全局的上下文信息，然后利用这些信息进行预测。

但实际上，因为卷积的是局部连接和参数共享的，不像类似于图结构，并没有考虑不通过特征之间的相互关联和相互位置关系，CNN中其实没有可用的空间信息。

如下图：
- CNN因为识别到人脸中包含的特征，认为这个一张正确的人脸。
- CNN不会识别这些特征之间的相互关系。没有学习到一种正确的特征间相位置对关系（特征的姿态信息）。

![20201011173706](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011173706.png)

![20201011200124](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011200124.png)

### 池化操作导致信息严重丢失

如最大池化，只保留最为活跃的神经元，传递到下一层，导致有价值的空间信息丢失。

Hinton提出“routing-by-agreement”的过程。较底层的特征将只被传递到与匹配的高层。

如：眼睛、嘴巴等底层特征，将被传递到“面部”的高层特征；手指、手掌等低层特征，被传递到“手”的高层特征。

## 胶囊网络的原理

### 核心思想：逆渲染（Inverse rendering）

1. 渲染：渲染来自于计算机图形学。渲染过程中我们需要提供几何信息，如告诉计算机在何处绘制对象，比如对象的比例、角度、空间信息等。

2. 逆渲染：根据图像（渲染结果）反推出物体的信息，包括空间几何信息。

胶囊网络需学会如何反向渲染图像————通过官差图像，预测图像的实例参数。

### 特征的向量编码形式
胶囊网络同事对空间信息和物体存在概率进行编码，编码在Capsule向量中。

Capsule向量：
>1. 向量的模表示特征存在的概率；
>2. 向量的方向表示特征的姿态信息；
>3. 移动特征会改变Capsule向量，不影响特征存在概率。

![20201011201630](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011201630.png)
<center>
胶囊网络分类人脸
</center>

### 胶囊内的操作

传统神经网络：加权求和+非线性激活

胶囊网络：
1. 输入向量 x 权重矩阵：编码了低级特征和高级特征的空间关系
2. 加权输入向量：权重决定当前胶囊将其输出到哪个更高级的胶囊。通过动态路由实现。 
3. 加权后求和
4. 非线性激活，使用squash函数：将向量进行压缩使其长度在0-1之间，方向保持不变。

![20201011204006](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011204006.png)

![20201011203934](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011203934.png)

### 胶囊之间的动态路由

- 路由（routing）：底层胶囊将输入向量传递到高层胶囊的过程。
- 高层胶囊和底层胶囊的权重通过动态路由（dynamic routing）获得。

![20201011205110](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011205110.png)
<center>动态路由示意图</center>

## 实例：CapsNet

### 整体结构

![20201011205307](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011205307.png)

### 重构解码结构

![20201011205320](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011205320.png)

### 损失函数

1. margin loss
2. reconstruction loss

## 胶囊网络存在的问题

目前只在mnist上表现出好的性能。

**胶囊脱落**问题。

