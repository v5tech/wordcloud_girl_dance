# -*- coding:utf-8 -*-
# @File : 1_安装依赖.py
import os

libs = {"lxml", "requests", "pandas", "numpy", "you-get", "opencv-python", "pandas", "fake_useragent", "matplotlib",
        "moviepy", "wordcloud", "jieba", "baidu-aip"}
try:
    for lib in libs:
        os.system(f"pip3 install -i https://pypi.doubanio.com/simple/ {lib}")
        print(lib + "安装成功")
except:
    print("安装失败")
