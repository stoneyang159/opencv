# Author : roczhang
# date :   2021/5/28
import cv2
import cv2 as cv
import numpy

# 创建一个3*3的数组
img = numpy.zeros((3, 3), dtype=numpy.uint8)

# 将灰度图转换成RGB图
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

print(img.shape)

image = cv.imread('/data/file/img/dog.jpeg')

cv.imwrite('img/dog.jpg', image)

# 创建一个随机的字节数组，把他转换成灰度图和BGR图
import os
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
flatNumpyArray.shape  # Out[15]: (120000,)

grayImage = flatNumpyArray.reshape(300, 400)
cv.imwrite('img/RandomGray2.png', grayImage)

bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv.imwrite('img/RandomColor.png', bgrImage)

# 获取图像的数据
# 第10行第10列的bgr值
image[10, 10, 0]
print(image.shape)
print(image.size)
print(image.dtype)

# 从摄像头获取视频的帧
# 有时，您甚至可能会遇到acamera，它在开始生成具有稳定维度的好帧之前，
# 会生成一些具有不稳定维度的坏帧。如果你担心防止这种怪癖，
# 你可能需要在捕获会话开始时阅读并忽略一些帧
cameraCapture = cv.VideoCapture(0)
fps = 30
# 这个方法可能会返回错误的值
size = (int(cameraCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv.VideoWriter('MyOutputVid.avi', cv.VideoWriter_fourcc('I', '4', '2', '0'),
                             fps, size)

success, frame = cameraCapture.read()
NumFramesRemaining = 10 * fps - 1  # 10 seconds of frames
while success and NumFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    NumFramesRemaining -= 1


# show image
img = cv.imread('img/dog.jpg')
cv.imshow('my image', img)
cv.waitKey()
cv.destroyAllWindows()