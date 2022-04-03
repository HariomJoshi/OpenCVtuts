import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 300)
cap.set(10, 100)
while(True):

    _, img = cap.read()

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # defining the range of blue color in HSV
    blue_lower = np.array([90, 50, 70])
    blue_upper = np.array([128, 255, 255])

    mask = cv2.inRange(imgHSV, blue_lower, blue_upper)
    finalImg = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("MaskImage", mask)
    cv2.imshow("Image", img)
    cv2.imshow("ImgHSV", imgHSV)
    cv2.imshow("Final img", finalImg)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

# color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
#               'white': [[180, 18, 255], [0, 0, 231]],
#               'red1': [[180, 255, 255], [159, 50, 70]],
#               'red2': [[9, 255, 255], [0, 50, 70]],
#               'green': [[89, 255, 255], [36, 50, 70]],
#               'blue': [[128, 255, 255], [90, 50, 70]],
#               'yellow': [[35, 255, 255], [25, 50, 70]],
#               'purple': [[158, 255, 255], [129, 50, 70]],
#               'orange': [[24, 255, 255], [10, 50, 70]],
#               'gray': [[180, 18, 230], [0, 0, 40]]}

