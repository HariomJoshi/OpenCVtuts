import cv2 as cv
import numpy as np

circle = True



def mouse_click(event,x,y,flags,param):
    radius = cv.getTrackbarPos("Radius", "Trackbar")
    width = cv.getTrackbarPos("Width", "Trackbar")
    red = cv.getTrackbarPos("RED", "Color Palette")
    green = cv.getTrackbarPos("GREEN", "Color Palette")
    blue = cv.getTrackbarPos("BLUE", "Color Palette")
    drawing = True
    if event == cv.EVENT_LBUTTONDBLCLK:

        if circle == True:
            cv.circle(img,(x,y),radius,(blue,green,red),width)
        else:
            cv.rectangle(img,(x-25, y-25), (x+25, y+25), (blue,green,red), width)

    # elif event == cv.EVENT_LBUTTONDOWN:
    #     cv.rectangle(img, (x, y), (x+20, y+20), (255, 0, 255), cv.FILLED)
    #
    # elif event == cv.EVENT_LBUTTONUP:
    #     cv.circle(img, (x,y), 20, (255, 255, 0), cv.FILLED)
    elif event == cv.EVENT_RBUTTONDOWN:
        drawing = True

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img, (x, y), radius, (blue,green,red), cv.FILLED)

def empty(a):
    pass
cv.namedWindow("Trackbar")
cv.createTrackbar("Radius", "Trackbar", 100, 500, empty)
cv.createTrackbar("Width", "Trackbar", 0, 50, empty)
cv.namedWindow("Color Palette")
cv.createTrackbar("RED", "Color Palette", 0, 255, empty)
cv.createTrackbar("GREEN", "Color Palette", 0, 255, empty)
cv.createTrackbar("BLUE", "Color Palette", 0, 255, empty)


img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
# insert the mouseCallBack function in the image, so wherever an event occurs on the image, the following function executes
cv.setMouseCallback('image', mouse_click)


while True:
    cv.imshow('image', img)
    k =cv.waitKey(1) & 0xFF
    if k == ord('c'):
        circle =not circle
    elif k == ord('q'):
        break

cv.destroyAllWindows()

