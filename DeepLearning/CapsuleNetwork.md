# 胶囊网络（Capsule Network）

## 背景：为什么会有胶囊网络？

### CNN中没有可用的空间信息

虽然随着卷积网络的层数的加深，网络可以学到更为全局的上下文信息，然后利用这些信息进行预测。

但实际上，因为卷积的是局部连接和参数共享的，不像类似于图结构，并没有考虑不通过特征之间的相互关联和相互位置关系，CNN中其实没有可用的空间信息。

![](https://raw.githubusercontent.com/brisyramshere/PicturesBed/master/20201011173706.png)

### 池化操作导致信息严重丢失

