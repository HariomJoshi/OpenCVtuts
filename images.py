import cv2
import numpy as np


img = cv2.imread("res/image.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converts the image to grayscale
cv2.imshow("Gray image", imgGray)
# cv2.waitKey(0)

imgCanny = cv2.Canny(img, 200, 150)  # the parameters are thresholds
kernel = np.ones((5,5), np.uint8)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


imgBlur = cv2.GaussianBlur(img, (9,9), 0)  # adds blur, you can increase the magniture by increasing kernel(middle (9,9) pair)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("dilation image", imgDilation)
cv2.imshow("eroded image", imgEroded)
cv2.waitKey(0)