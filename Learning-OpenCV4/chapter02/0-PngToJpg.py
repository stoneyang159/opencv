# Author : roczhang
# date :   2021/5/28

import cv2 as cv
import numpy

# 创建一个3*3的数组
img = numpy.zeros((3, 3), dtype=numpy.uint8)

# 将灰度图转换成RGB图
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

print(img.shape)

image = cv.imread('/data/file/img/dog.jpeg')

cv.imwrite('dog.jpg', image)