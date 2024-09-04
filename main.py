import cv2
import mediapipe as mp
import math
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

direcao = None

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
                cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                pontos.append((cx, cy))

            
        
        x1, y1 = pontos[4][0], pontos[4][1]
        x2, y2 = pontos[8][0], pontos[8][1]
        
        cx, cy = (x1+x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1,y1), 5, (255,0,0), cv2.FILLED)
        cv2.circle(img, (x2,y2), 5, (255,0,0), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)
        
        length = math.hypot(x2 - x1, y2 -y2)
        
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx,cy), 5, (0,255,0), cv2.FILLED)
        
        

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    
    
# pontos 4 ,8 