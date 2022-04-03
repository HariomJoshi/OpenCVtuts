import cv2
import numpy as np
img = cv2.imread("res/image.png")
# horizontal stack
hor = np.hstack((img, img,img, img))
#vertical stack
ver = np.vstack((hor, hor,hor, hor))
# it won't work if both the images have differnt number of channels
cv2.imshow("Horizontal stack", hor)
cv2.imshow("Vertical stack", ver)
cv2.waitKey(0)

