import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from pyfirmata import Arduino,SERVO
import time
import Servo
import Hand as h
import sys
import time

from pymata4 import pymata4


################################
wCam, hCam = 1200, 1080
################################

# Definindo parametros do video e a fonte
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


#Iniciando a detecção com 0.8 de precisão
pTime = 0
detector = htm.handDetector(detectionCon=0.8)

IP_ADDRESS = "10.0.0.117"
IP_PORT = 3030

#board = Arduino("COM3")
board = pymata4.Pymata4(ip_address=IP_ADDRESS, ip_port=IP_PORT)
print("Conectando")
hand = h.Hand(board,0,2,4,5,16)

      

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
      try:
        hand.move(lmList)
      except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)
        
       
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    cv2.imshow("Img", img)
    cv2.waitKey(1)