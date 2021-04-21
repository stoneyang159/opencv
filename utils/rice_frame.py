# author: roczhang
# file: rice_frame.py
# time: 2021/04/21

import cv2
import os
# file name
num = 1

while num < 7:
    # whole file name
    FileName = 'MVI_' + str(num)
    num += 1
    video_path = os.path.join("D:/fei/Grain_video_capture_images/CANON20210416Rice/", FileName+'.MOV')
    times = 0
    OutputDirName = 'D:/RocZhang/file/rice_frame/'+FileName+'/'
    if not os.path.exists(OutputDirName):
        os.makedirs(OutputDirName)
    camera = cv2.VideoCapture(video_path)
    # 获取总帧数 19657.0
    frames_num = camera.get(7)
    # 每十秒为一张新图，总时长为13：06， 所以提取78张图片。间隔252帧取一张图。
    # 提取视频的频率，每25帧提取一个
    frameFrequency = 252
    # frame = 19656
    # #设置要获取的帧号
    # camera.set(cv2.CAP_PROP_POS_FRAMES, frame)
    # res, image = camera.read()
    # cv2.imwrite(OutputDirName+str(frame)+"_param"+'.jpg', image)
    id = 1
    while True:
        times += 1
        if times >= frames_num:
            print('已经提取到最后一帧拉!')
            break
        if times % frameFrequency == 0:
            camera.set(cv2.CAP_PROP_POS_FRAMES, times)
            res, image = camera.read()
            cv2.imwrite(OutputDirName + str(id) + '.jpg', image)
            print(OutputDirName+str(id)+'.jpg')
            id += 1
    print("图片提取结束！")
    camera.release()

