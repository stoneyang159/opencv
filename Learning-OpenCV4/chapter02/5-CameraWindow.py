# Author : roczhang
# date :   2021/5/29
import cv2 as cv

clicked = False

# 鼠标点击会触发函数
def onMouse(event, x, y, flags, param):
    global clicked
    # 触发
    if event == cv.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv.VideoCapture(0)
# 这里的名字一定要和后面的对上，不然会出现几个窗口
cv.namedWindow('MyWindows')
cv.setMouseCallback('MyWindows', onMouse)

print('Showing camera feed. Click window or press any key to stop.')
success, frame = cameraCapture.read()
while cv.waitKey(1) == -1 and not clicked:
    if frame is not None:
        cv.imshow('MyWindows', frame)
    success, frame = cameraCapture.read()
cv.destroyWindow('MyWindows')
cv.destroyAllWindows()