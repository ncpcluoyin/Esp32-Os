# Esp32 Os

## 适用于Esp系列以及可以安装micropython的开发板的操作系统

这是第一个稳定版本v0.1，预计在2020年5月份发布0.2
如要获取最新的开发进度可以使用unstable分支中提供的系统

#### 安装教程

1.  克隆本系统到本地，默认克隆分支为稳定版
2.  复制main.py,start.py,lib.py等后缀名为.py的文件至micropython开发板的文件系统中，切记不要删除文件系统中自带的boot.py
3.  上电后可以在串口中进行交互，命令和linux相似，不过运行python程序要用"run [filename]"来执行

#### 使用说明

1.  本系统基于gpl 3.0协议进行开源，如要用于商业用途必须联系作者：罗印 邮箱:912271673@qq.com
2.  本系统不定期更新到github
3.  本系统制作团队为syrathon，我问的官网是www.syrathon.com,论坛bbs.syrathon.com

#### 此版本特性