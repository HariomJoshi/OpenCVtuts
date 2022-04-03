import cv2
import numpy as np

def getContours(img):
    Contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # contours will be saved in contours, so we have to loop through it
    for cnt in Contours:
        area = cv2.contourArea(cnt)  # function to find area of between the contours
        print(area)
        # it is good to give an area threshold so that it may not detect noises
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # draws all the contours detected in imgContour
            peri = cv2.arcLength(cnt, True)  # gives us the arc length/ perimeter
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)  # you may vary 0.02 according to your need
            # 0.02*peri is the tolerance parameter
            # approx will give us a list of corners


            # true denotes that the shape is closed
            # above function works of Douglas-Peuker algorithm

            print(len(approx))
            objCorner = len(approx)

            # if we were to draw a bounding box around the object, the x, y, width, height would be
            x, y, w, h = cv2.boundingRect(approx)
            if objCorner == 3:
                objectType = "Triangle"

            elif objCorner == 4:
                aspectRatio = w/float(h)
                # we can have a deviation of 0.05 in the aspect ration
                if aspectRatio > 0.95 and aspectRatio< 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"

            elif objCorner>4:
                objectType = "Circle"

            else:objectType = "Not Defined"
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255, 0), 2)

            cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)



path = 'res/shapes.png'
img = cv2.imread(path)
imgContour = np.zeros_like(img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50,50)
getContours(imgCanny)  # defined above

cv2.imshow("Original", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Contour", imgContour)
cv2.waitKey(0)
