# author: roczhang
# file: demo_7.py
# time: 2021/05/15
# 边缘检测
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/data/file/img/data/messi5.jpg',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()