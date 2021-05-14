# author: roczhang
# file: basic.py
# time: 2021/04/19

import numpy as np
import cv2 as cv
img = cv.imread("/data/file/img/dog.jpg")
px = img[100, 100]
print(px)


