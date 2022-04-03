import cv2
import numpy as np

# we are using a pre-defined cascade(xml file)
faceCascade = cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml")
img = cv2.imread('res/face.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
# here, faces is a list of rectangles bounding the objects detected
# above function detects objects of different input sizes in the input image and returns it as a list of rectangles

for (x, y, w, h) in faces:
    print(x, y, w, h)
    # cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    # drawing a circle when we detect a face
    cv2.circle(img, (x+w//2, y+h//2), 150, (255, 0, 0), 2)


cv2.imshow("Face Image", img)
cv2.waitKey(0)