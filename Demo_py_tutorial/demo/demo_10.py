# Author : roczhang
# date :   2021/5/18
import cv2 as cv

im = cv.imread('/data/file/img/data/chessboard.png')
imgary = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgary, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)