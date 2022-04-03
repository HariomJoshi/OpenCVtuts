import cv2 as cv
from cv2 import waitKey
import numpy as np


# colors = [[143,113,136,179,243,255]]
colors = [[100,167,12,179,255,206]]
colorValues = [[222, 39, 225]]
myPoints = []  # [x, y, colorID]

def getContours(image):
    '''this function tells us where the tip is going by giving the X and Y coordinates of the tip every second'''

    contours, hirarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500:
            cv.drawContours(contourImage, cnt, -1, (255, 255, 0), 3)
            peri = cv.arcLength(cnt, True)
            corners = cv.approxPolyDP(cnt, 0.02*peri, True)
            # no_of_corners = len(corners)
            x,y,w,h = cv.boundingRect(corners)
    # we want to return just the tip of the thing we are using, so that we can draw from it
    return x+w//2,y


def getColor(image, mycolors, mycolorValues):
    '''this function tells us the color of the object, masks it and also returns the color id(by appending it in an array)
    and then appends it to another array named newPoints, and returns it'''

    imgHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in mycolors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv.circle(contourImage, (x, y), 5, mycolorValues[count], cv.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x, y, count])
        count += 1
        # cv.imshow("mask", mask)
        # if cv.waitKey(1) & 0xFF == ord('q'):
        #     break
    return newPoints


def drawOnCanvas(myPoints, mycolorValues):
    '''this function draws a circle at all the points passed to it in list -> myPoints , of color -> myColorValues
    respectively'''

    for points in myPoints:
        cv.circle(contourImage, (points[0], points[1]), 5, mycolorValues[points[2]], cv.FILLED)




frameHeight = 480
frameWidth = 640
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
cap.set(cv.CAP_PROP_BRIGHTNESS, 100)


while cap.isOpened():
    success, img = cap.read()
    contourImage = img.copy()
    newPoints = getColor(contourImage, colors, colorValues)
    if len(newPoints) != 0:
        for nPoint in newPoints:
            myPoints.append(nPoint)


    if len(myPoints) != 0:
        drawOnCanvas(myPoints, colorValues)
    
    img = cv.flip(img, 1)
    contourImage = cv.flip(contourImage, 1)

    cv.imshow("Camera", img)
    cv.imshow("Contours", contourImage)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    # elif cv.waitKey(1) & 0xFF == ord('e'):
        # code to erase here

