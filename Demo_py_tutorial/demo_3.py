# author: roczhang
# file: demo_3.py
# time: 2021/05/14
from timeit import timeit

import cv2 as cv
import numpy as np

img1 = cv.imread('/data/file/img/data/messi5.jpg')
e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t = (e1 - e2) / cv.getTickFrequency()
print(t)

cv.useOptimized()
