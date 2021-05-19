# author: roczhang
# file: demo_4.py
# time: 2021/05/14
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/data/file/img/data/messi5.jpg')
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()

# 平移
img2 = cv.imread('/data/file/img/data/messi5.jpg', 0)
rows, cols, dim = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 旋转
img = cv.imread('/data/file/img/data/messi5.jpg', 0)
rows, cols = img.shape
M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('dst', dst)
cv.waitKey()
cv.destroyAllWindows()

# 仿射变换
img = cv.imread('/data/file/img/data/digits.png')
rows,cols,ch = img.shape
# 找到对应的三个点
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
# 获取变换矩阵
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')

# 透视变换
img = cv.imread('/data/file/img/data/sudoku.png')
rows,cols,ch = img.shape
# 在原图找四个点，这四个点对应处理后图像的四个角的点
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
# 根据这八个点，生成转换矩阵
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()