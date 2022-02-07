import cv2
import mediapipe as mp
import time

from mediapipe.python.solutions import hands

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 78), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 255, 0), 3)

    cv2.imshow("Image" , img)
    cv2.waitKey(1)