import cv2 as cv
import mediapipe as mp
import time   # to check the frame rate

cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
# we dont need to pass anything here because, everything is already according to us, if we want
# so we can change several properties by passing it as an argument, as we will do later

mpDraw = mp.solutions.drawing_utils  # this will help us drawing landmarks and also line between them


pTime = 0
cTime = 0


while True:
    sucess, img = cap.read()

    # since hand class only uses RGB image so we have to convert our image to RGB from BGR before passing it to hand class
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # now we just need to extract the required data from results
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handlms, mphands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime -pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)),(10, 70), cv.FONT_HERSHEY_SIMPLEX, 3,(255, 255, 0), 2 )


    cv.imshow("Camera", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

