import numpy as np
import cv2 as cv
img = cv.imread('/data/file/img/dog.jpg', 0)
cv.imshow('image', img)
k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('/data/file/img/dog2.jpg', img)
    cv.destroyAllWindows()