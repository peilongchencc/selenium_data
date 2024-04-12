#!/bin/bash

# 查看自己正在使用的shell解释器名称,这里是为了检查crontab运行的环境是否为 `/bin/bash`。
echo $SHELL

# 初始化conda环境
source /root/anaconda3/etc/profile.d/conda.sh

# 激活conda环境
conda activate langchain

# 切换路径
cd /data/selenium_data

# conda环境下运行python文件
python fetch_webpage_content_baidu.py