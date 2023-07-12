import cv2
import mediapipe as mp
import math
import numpy as np


video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape 
    pontos = []
    if handsPoints:
        for points in handsPoints:
            print(points)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w),int(cord.y * h)
                #cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                pontos.append((cx, cy))

        x1, y1 = pontos[4][0], pontos[4][1]
        x2, y2 = pontos[8][0], pontos[8][1]
        
        cx, cy = (x1+x2) // 2, (y1 + y2) // 2
        
       
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
