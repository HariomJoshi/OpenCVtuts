import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
i = 0
while True:
    sucess, img = cap.read()
    cv.putText(img, f"{i}", (10, 70), cv.FONT_HERSHEY_COMPLEX, 1, (255, 5, 234))
    i = i+1
    cv.rectangle(img, (3,3), (630, 475), (234, 45, 54), 2)

    cv.imshow("Video", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break       
