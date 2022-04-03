import cv2

img = cv2.imread("res/image.png")
cv2.imshow("output", img)
cv2.waitKey(0)

cap = cv2.VideoCapture("res/video.mp4")

while True:
    success, img = cap.read()
    # success is a boolean variable which tells us whether the capture of video into picture is successful or not
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# how to use a webcam is similar to playing video
cap = cv2.VideoCapture(0)
# id for length id 3
cap.set(3, 640)
# id for width is 4
cap.set(4, 480)
# id for brightness is 10
cap.set(10, 100)

while True:
    success, img = cap.read()
    # success is a boolean variable which tells us whether the capture of video into picture is successful or not
    cv2.imshow("video",img)
    # the following line makes the function quit on pressing q button on keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


