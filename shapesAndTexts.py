import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)  # function to check dimensions of image

img[:] = 255,0,0  # this will color the whole image
# img[100:200, 100:200] = 255,0,0  # this will color the specified segment
cv2.line(img, (0,0), (300, 300), (0,255,0), 3)
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)
# img.shape[1] gives us the width, and latter the height
cv2.rectangle(img, (0,0), (200, 300), (0, 255, 0), 3)
cv2.rectangle(img, (0,0), (img.shape[0],img.shape[1]), (0, 255, 0), 3)  # square surrounding the whole image

cv2.circle(img, (200, 200), 50, (0, 0, 255), 2)
# instead of width if you write cv2.FILLED so it will fill the complete shape
cv2.circle(img, (200, 400), 50, (0, 0, 255), cv2.FILLED)

cv2.putText(img, "OPEN CV HARIOM", (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 0 ,150), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)