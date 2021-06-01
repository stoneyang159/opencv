import cv2
image = cv2.imread('/data/file/img/image_1.jpg')

image.shape

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img_gray.shape

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

thresh.shape
thresh

