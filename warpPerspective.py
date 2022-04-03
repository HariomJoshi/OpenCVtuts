import cv2
import numpy as np

img = cv2.imread("res/card_image.jpg")


width, height = 250, 350
# if you want to get the coordinates, open image with paint and moove cursor around
pts1 = np.float32([[407, 80], [667, 130], [595, 549], [313, 488]])
# now we have to define which point we are referring to, which is the first and which is the last
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey()
