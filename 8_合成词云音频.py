# -*- coding:utf-8 -*-
# @File : 8_合成词云音频.py

import moviepy.editor as mpy

# 读取词云视频
my_clip = mpy.VideoFileClip('./result.mp4')
# 截取背景音乐 从 无价之姐~让我乘风破浪~~~.mp3 截取3～30秒的音频
audio_background = mpy.AudioFileClip('./无价之姐~让我乘风破浪~~~.mp3').subclip(3, 30)
audio_background.write_audiofile('./song.mp3')
# 视频中插入音频
final_clip = my_clip.set_audio(audio_background)
# 保存为最终的视频   动听的音乐！漂亮小姐姐词云跳舞视频！
final_clip.write_videofile('./final_video.mp4')
