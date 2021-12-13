# -*- coding:utf-8 -*-
# @File : 2_视频分割.py
import cv2

cap = cv2.VideoCapture(r"无价之姐~让我乘风破浪~~~.flv")
num = 1
while True:
    # 逐帧读取视频  按顺序保存到本地文件夹
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"./pictures/img_{num}.jpg", frame)  # 保存一帧帧的图片
        print(f'========== 已成功保存第{num}张图片 ==========')
        num += 1
    else:
        break
cap.release()  # 释放资源
