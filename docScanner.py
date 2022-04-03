import cv2 as cv
import imutils
import numpy as np

def getContours(img):
    x,y,w,h = 0,0,0, 0
    contour = np.array([[0,0],[0,0], [0,0], [0,0]], np.int32)
    maxarea = 0
    contours, heirarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area> 5000:
            # cv.drawContours(contourImage, cnt, -1, (255, 255, 0), 3)
            peri = cv.arcLength(cnt, True)
            contoursList = cv.approxPolyDP(cnt, 0.02*peri, True)
            # x, y, w, h = cv.boundingRect(contoursList)
            if area>maxarea and len(contoursList) == 4:
                contour = contoursList
                maxarea = area

    return contour
    # return [[x,y], [x+w, y], [x, y+h], [x+h, y+w]]


def reorder(myPoints):
    myPoints = myPoints.reshape(4,2)
    myPointsNew = np.zeros((4,1,2), np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew



def cropImage(img):
    lower = np.array([76, 14, 150])
    upper = np.array([126, 255, 255])
    imgBlur = cv.GaussianBlur(img, (5,5), 0)
    imgCanny = cv.Canny(imgBlur, 200, 150)
    kernel = np.ones((5,5), np.uint8)
    imgDilate = cv.dilate(imgCanny, kernel, iterations=2)
    imgErode = cv.erode(imgDilate, kernel, iterations=1)
    # imgHSV = cv.cvtColor(imgBlur, cv.COLOR_BGR2HSV)
    # mask = cv.inRange(imgHSV, lower, upper)
    cv.imshow("imgErode", imgErode)
    cv.waitKey(1)
    cnt = getContours(imgErode)
    print(cnt.shape)
    # cv.rectangle(contourImage, corners[0], corners[3], (0, 0, 255), 3)
    width, height = 250, 350

    pts1 = np.float32(reorder(cnt))  # the points we want to crop
    pts2 = np.float32([[0,0],[width,0],[0, height], [width, height]])  # dimensions of the output window
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv.warpPerspective(img, matrix, (width, height))
    return imgOutputqqq


url = "http://192.168.43.1:8080/video"
cap = cv.VideoCapture(url)

while True:
    success, img = cap.read()
    img = imutils.resize(img, width=640, height=480)
    img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    contourImage = img.copy()
    imgOutput = cropImage(img)
    cv.imshow("Phone cam vid", img)
    cv.imshow("ImgOutput", imgOutput)
    # cv.imshow("Contours", contourImage)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


