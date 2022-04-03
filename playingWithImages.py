import cv2

img = cv2.imread("res/image.png")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))  # the width first and then the height
print(imgResize.shape)

# cosider image as a matrix/array of pixels
# below function is to crop an image
imgCropped = img[0:200, 0:200]  # the height first and then the width

cv2.imshow("Image", img)
# cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)