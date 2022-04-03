import cv2
import numpy as np
import imutils

def empty(a):
    pass


path = 'res/car.jpg'
# created a window named TrackBar
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 240)  # declared size here
# we made 6 trackBars in order to balance the value to get the perfect mask
cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)  # empty() function runs, each time we alter TrackBar value
cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

# H -> Hue
# S -> Saturation
# v -> Value
url = "http://192.168.43.1:8080/video"
cap = cv2.VideoCapture(0)

# since the value will keep altering, so we have to use a while loop so that
# each time we alter the value in the TrackBar, the value reflects on screen
# and images as well
while True:

    success,img = cap.read()
    img = imutils.resize(img, width=640, height=480)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    # img = cv2.VideoCapture(0)
    # getTrackbarPos() returns the current position of the TrackBar
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    # converts the image into HSV image
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])  # array consisting of all the min values
    upper = np.array([h_max, s_max, v_max])  # array consisting of all the max values
    # now we are creating a mask, with the help of imgHSV and also its lower and upper bound, which are arrays
    mask = cv2.inRange(imgHSV, lower, upper)
    # now, by using this mask we can create a new image
    imgResult = cv2.bitwise_and(img, img, mask=mask)


    cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    # cv2.imshow("final image", imgResult)
    cv2.waitKey(1)
