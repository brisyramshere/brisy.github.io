# Deep Latent Space Translation

Image Translation方法在很多领域大有用处。比如：

1. 图像去燥问题
2. 图像复原问题
3. 图像分割迁移问题
4. 医学图像：图像模态转换
5. 医学图像：金属去伪影

本文主要讨论CVPR2020上发表的一篇Oral文章，针对老照片的图像修复应用的一种新的Image Translation方法：

- paper:Old Photo Restoration via Deep Latent Space Translation
- code:[https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life)

![](../imgres/2020-11-22-10-48-42.png)

## 摘要

- 提出了一种基于深度学习的被严重损害的老照片的复原方法。
- 无监督方法，无需成对监督学习数据
- 训练两个VAE网络，分别在两个浅空间将老照片转换为干净的照片。
- 两个转换在浅空间形成闭环
- 对于老照片中的多种不同类型损毁：
  - 设计一个全局分支结合部分非局部块，以定位结构化缺损，如划痕和灰尘斑点。
  - 设计一个局部分支定位非结构化缺损，如噪声和模糊。
  - 两个分支在latent space进行融合
- 效果：**图像复原的观感远好于目前的SOTA以及现有的商业工具**

## 相关工作

- 单类型图像损伤的复原
  - 非结构化损伤（unstructed degradation）：噪声，模糊，色彩退化，低分辨率
  - 结构化损伤(structed degradation):空洞，划痕，灰尘斑点
- 混合类型图像损伤的复原
- 面部复原
- 老照片复原

|  非结构化损伤   | 结构化损伤  |
|  ------------  | ---------  |
| 噪声，模糊，色彩退化，低分辨率  | 空洞，划痕，灰尘斑点 |
|  nonlocal self-sumilarity;sparsity;local smooth | learning-based方法 |

## 方法

### 各种Domain和转换关系

下图为图像复原场景中涉及到的几种domain和之间的转换关系。

![](../imgres/2020-11-22-11-17-26.png)

>图注
>
>- 
<img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1">
:人工合成老照片图像
>- 
<img src="https://www.zhihu.com/equation?tex=y" alt="y" class="ee_img tr_noresize" eeimg="1">
:与
<img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1">
成对的修复clean的图像
>- 
<img src="https://www.zhihu.com/equation?tex=r" alt="r" class="ee_img tr_noresize" eeimg="1">
:真实老照片图像
>- 
<img src="https://www.zhihu.com/equation?tex=z_x" alt="z_x" class="ee_img tr_noresize" eeimg="1">
:合成老照片图像浅空间变量
>- 
<img src="https://www.zhihu.com/equation?tex=z_y" alt="z_y" class="ee_img tr_noresize" eeimg="1">
:clean图像浅空间变量
>- 
<img src="https://www.zhihu.com/equation?tex=z_r" alt="z_r" class="ee_img tr_noresize" eeimg="1">
:真实老图浅空间变量

该方法的关键在于浅空间学习（latent spacing learning）。涉及到两种技术：

1. 浅空间
<img src="https://www.zhihu.com/equation?tex=z_x" alt="z_x" class="ee_img tr_noresize" eeimg="1">
和
<img src="https://www.zhihu.com/equation?tex=z_r" alt="z_r" class="ee_img tr_noresize" eeimg="1">
的对齐（domain alignment）
2. 浅空间
<img src="https://www.zhihu.com/equation?tex=z_x" alt="z_x" class="ee_img tr_noresize" eeimg="1">
或
<img src="https://www.zhihu.com/equation?tex=z_y" alt="z_y" class="ee_img tr_noresize" eeimg="1">
到映射（domain mapping）

### 网络结构解析

下图为论文提出的网络结构：

![](../imgres/2020-11-22-11-24-46.png)

结构中涉及两个VAE网络：

- VAE1可对
<img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1">
或
<img src="https://www.zhihu.com/equation?tex=r" alt="r" class="ee_img tr_noresize" eeimg="1">
进行重建
- VAE2可对
<img src="https://www.zhihu.com/equation?tex=y" alt="y" class="ee_img tr_noresize" eeimg="1">
进行重建
- VAE1和VAE2的潜变量通过一个Mapping模块
<img src="https://www.zhihu.com/equation?tex=T" alt="T" class="ee_img tr_noresize" eeimg="1">
实现转换
- 
<img src="https://www.zhihu.com/equation?tex=T" alt="T" class="ee_img tr_noresize" eeimg="1">
：可将
<img src="https://www.zhihu.com/equation?tex=z_X" alt="z_X" class="ee_img tr_noresize" eeimg="1">
和
<img src="https://www.zhihu.com/equation?tex=z_R" alt="z_R" class="ee_img tr_noresize" eeimg="1">
域内的变量迁移到
<img src="https://www.zhihu.com/equation?tex=z_Y" alt="z_Y" class="ee_img tr_noresize" eeimg="1">
域
- 图像复原流程：
<img src="https://www.zhihu.com/equation?tex=r" alt="r" class="ee_img tr_noresize" eeimg="1">
->
<img src="https://www.zhihu.com/equation?tex=z_R" alt="z_R" class="ee_img tr_noresize" eeimg="1">
->
<img src="https://www.zhihu.com/equation?tex=z_{R->Y}" alt="z_{R->Y}" class="ee_img tr_noresize" eeimg="1">
->
<img src="https://www.zhihu.com/equation?tex=r_{R->Y}" alt="r_{R->Y}" class="ee_img tr_noresize" eeimg="1">


### 两个VAE的训练和Loss

具体的，VAE1和和VAE2是单独训练的。

#### VAE重建任务Loss

VAE1由
<img src="https://www.zhihu.com/equation?tex=r" alt="r" class="ee_img tr_noresize" eeimg="1">
和
<img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1">
作为输入进行训练。目标是重建其自身图像。

对于作为重建任务的VAE1，对于输入图像为
<img src="https://www.zhihu.com/equation?tex=r" alt="r" class="ee_img tr_noresize" eeimg="1">
时，其训练Loss为：


<img src="https://www.zhihu.com/equation?tex=L_{VAE1}(r)=KL(E_{R,X}(z_r|r)||N(0,I))+\alpha E_{z_r\sim E_{R,X}(z_r|r)[||G_{R,X}(r_{R->R}|z_r)-r||_1]}+L_{VAE1,GAN}(r)" alt="L_{VAE1}(r)=KL(E_{R,X}(z_r|r)||N(0,I))+\alpha E_{z_r\sim E_{R,X}(z_r|r)[||G_{R,X}(r_{R->R}|z_r)-r||_1]}+L_{VAE1,GAN}(r)" class="ee_img tr_noresize" eeimg="1">


- 公式三项的优化目标分别是：
  1. latent分布服从高斯分布
  2. 重建Loss，要求latent学到有助于重建输入的特征
  3. 引入LSGAN，解决VAE的过平滑问题，保证重建图像的高真实度

同样的，使用
<img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1">
训练VAE1的Loss函数
<img src="https://www.zhihu.com/equation?tex=L_{VAE1}(x)" alt="L_{VAE1}(x)" class="ee_img tr_noresize" eeimg="1">
和上式$L_{VAE1}(r)类似。

VAE2由
<img src="https://www.zhihu.com/equation?tex=y" alt="y" class="ee_img tr_noresize" eeimg="1">
作为输入进行训练，目标是重建y本身。其训练的Loss函数
<img src="https://www.zhihu.com/equation?tex=L_{VAE2}(y)" alt="L_{VAE2}(y)" class="ee_img tr_noresize" eeimg="1">
形式上和$L_{VAE1}(r)同样没有区别。

#### latent gap reduction Loss


<img src="https://www.zhihu.com/equation?tex=R" alt="R" class="ee_img tr_noresize" eeimg="1">
和
<img src="https://www.zhihu.com/equation?tex=X" alt="X" class="ee_img tr_noresize" eeimg="1">
的浅空间的Domain alignment是非常重要的一步。本文使用对抗训练的思想实现。

为减少
<img src="https://www.zhihu.com/equation?tex=r" alt="r" class="ee_img tr_noresize" eeimg="1">
和
<img src="https://www.zhihu.com/equation?tex=x" alt="x" class="ee_img tr_noresize" eeimg="1">
两个latent domain的gap，引入第三个判别器{D_{r,x}}，并涉及latent对抗loss：


<img src="https://www.zhihu.com/equation?tex=L_{VAE1,GAN}^{latent}(r,x)=E_{x\sim X}[D_{R,X}(E_{R,X}(x))^2]+E_{r \sim R}[1-D_{R,X}(E_{R,X}(R))^2]" alt="L_{VAE1,GAN}^{latent}(r,x)=E_{x\sim X}[D_{R,X}(E_{R,X}(x))^2]+E_{r \sim R}[1-D_{R,X}(E_{R,X}(R))^2]" class="ee_img tr_noresize" eeimg="1">


至此，可以得到VAE1的总Loss公式如下：


<img src="https://www.zhihu.com/equation?tex=\underset{E_{R,X},G_{R,X},D_{R,X}}{min}\underset{D_{R,X}}{max}L_{VAE1}(r)+L_{VAE1}(x)+L_{VAE1,GAN}^{latent}(r,x)" alt="\underset{E_{R,X},G_{R,X},D_{R,X}}{min}\underset{D_{R,X}}{max}L_{VAE1}(r)+L_{VAE1}(x)+L_{VAE1,GAN}^{latent}(r,x)" class="ee_img tr_noresize" eeimg="1">


### Restoration through latent mapping

浅空间进行映射的三个好处：

1. 当
<img src="https://www.zhihu.com/equation?tex=R" alt="R" class="ee_img tr_noresize" eeimg="1">
和
<img src="https://www.zhihu.com/equation?tex=X" alt="X" class="ee_img tr_noresize" eeimg="1">
对齐到同一latent space，从
<img src="https://www.zhihu.com/equation?tex=Z_x" alt="Z_x" class="ee_img tr_noresize" eeimg="1">
到
<img src="https://www.zhihu.com/equation?tex=Z_y" alt="Z_y" class="ee_img tr_noresize" eeimg="1">
的映射同样适用于从
<img src="https://www.zhihu.com/equation?tex=Z_r" alt="Z_r" class="ee_img tr_noresize" eeimg="1">
到
<img src="https://www.zhihu.com/equation?tex=Z_y" alt="Z_y" class="ee_img tr_noresize" eeimg="1">

2. 浅空间编码特征维度低，相比于高维图像空间更易学习
3. 因为两个VAE是单独训练的，因此两条线路的图像的重建并不会受到各自的影响。
<img src="https://www.zhihu.com/equation?tex=G_y" alt="G_y" class="ee_img tr_noresize" eeimg="1">
总是能得到一个干净的图像

训练Mapping模块时，会固定两个VAE的参数，Loss函数由三部分组成：


<img src="https://www.zhihu.com/equation?tex=L_T(x,y)=\lambda_1L_{T,l_1}+L_{T,GAN}+\lambda_2L_{FM}" alt="L_T(x,y)=\lambda_1L_{T,l_1}+L_{T,GAN}+\lambda_2L_{FM}" class="ee_img tr_noresize" eeimg="1">


- 
<img src="https://www.zhihu.com/equation?tex=L_{T,l_1}=E||T(z_x)-z_y||_1" alt="L_{T,l_1}=E||T(z_x)-z_y||_1" class="ee_img tr_noresize" eeimg="1">
, 为x的潜变量转换到
<img src="https://www.zhihu.com/equation?tex=Z_Y" alt="Z_Y" class="ee_img tr_noresize" eeimg="1">
后与
<img src="https://www.zhihu.com/equation?tex=z_y" alt="z_y" class="ee_img tr_noresize" eeimg="1">
的1范式距离
- 
<img src="https://www.zhihu.com/equation?tex=L_{T,GAN}" alt="L_{T,GAN}" class="ee_img tr_noresize" eeimg="1">
：对抗Loss，引入LSGAN，使
<img src="https://www.zhihu.com/equation?tex=x_{X->Y}" alt="x_{X->Y}" class="ee_img tr_noresize" eeimg="1">
看上去更真实
- 
<img src="https://www.zhihu.com/equation?tex=L_{FM}" alt="L_{FM}" class="ee_img tr_noresize" eeimg="1">
：feature matching Loss，也就是perception loss，即要求不仅判别器输出要接近，判别器输出前几层的feature map也要相近

