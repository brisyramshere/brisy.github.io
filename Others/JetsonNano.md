# 介绍
jetson nano的入门使用教程笔记

# 内容
## 查看系统类型：
`uname -a`
`uname --help` 查看指令帮助
## 将cuda相关目录添加到环境变量PATH
在~/.bashrc文件末尾添加：
查看cuda环境变量配置情况：nvcc -V
## 设置apt-get的sources源
>1. 使用tsinghua的源替换/ect/apt/sources.list
>2. `sudo apt-get update`
## 设置pip的sources源
`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
## 设置默认python版本
用户级修改，只在当前用户有效：
在~/.bashrc文件中添加alias python='/usr/bin/python3.6'
## 安装中文输入法ibus
参考网址：https://blog.csdn.net/Discoverhfub/article/details/79719208
## 配置远程桌面
参考网址：http://www.waveshare.net/study/article-894-1.html
>1. 使用VNC（windows通过VNC Viewer连接）
>2. 使用xrdp（windows通过远程桌面连接）
## 连接摄像头
>1. 摄像头型号：IMX219
>2. 查看设备连接状态：ls /dev/vid*
>3. 启动摄像头：`gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=3820, height=2464, framerate=21/1, format=NV12' ! nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=616' ! nvvidconv ! nvegltransform ! nveglglessink -e`
## 安装pytorch 1.4.0
注意安装aarch框架
参考网址：https://www.cnblogs.com/cloudrivers/p/12233545.html
## git配置ssh key
>1. git配置public key
>2. 生成本地密钥：`ssh-keygen -t rsa -b 2048 -C "your email addr"`
>3. 复制生成的密钥'~/.ssh/id_rsa.pub'到github的 Setting->SSH and GPG keys->New SSH Key
git clone代码
## 尝试jetson-inference项目(NVIDIA官方)
>1. 安装依赖
>2. git clone下载源码
>更换模型和pytorch的安装源(原源需要翻墙)
>`sed -in-place -e 's@https://nvidia.box.com/shared/static@https://bbs.gpuworld.cn/mirror@g' tools/download-models.sh`
>`sed -in-place -e 's@https://nvidia.box.com/shared/static@https://bbs.gpuworld.cn/mirror@g' tools/install-pytorch.sh`
>3. 编译源码：
>参考网址：https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md
## 利用pytorch运行人脸检测算法

## 利用tensorRT加速算法推理
 
