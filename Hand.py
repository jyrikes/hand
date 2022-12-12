import Servo as servo
import math
import numpy as np
from time import sleep
def angulos(vetor1, vetor2,op):
  if op ==1:
    a = np.array(vetor1)
    b = np.array(vetor2)
    c = np.hypot(vetor1[0],vetor1[1])
    d = np.hypot(vetor2[0],vetor2[1])
    
    pro = np.cross(a,b)
    tan = (pro/(c*d))
    tan = np.abs(tan)
    #print(tan)
    return(np.degrees(np.arcsin(tan)))
  else:
    a = np.array(vetor1)
    b = np.array(vetor2)
    c = np.hypot(vetor1[0],vetor1[1])
    d = np.hypot(vetor2[0],vetor2[1])
    
    pro = np.cross(a,b)
    tan = (pro/(c*d))
    tan = np.abs(tan)
    #print(tan)
    return(np.degrees(np.arccos(tan)))

class Hand():
  def __init__(self,placa,polegar,indicador,medio,anelar, minino):
    self.polegar = polegar
    self.indicador = indicador
    self.medio= medio
    self.anelar = anelar
    self.minimo = minino
    self.placa = placa
    
    self.motorPolegar = servo.servo(polegar,placa)
    self.motorIndicador = servo.servo(indicador,placa)
    self.motorMedio = servo.servo(medio,placa)
    self.motorAnelar = servo.servo(anelar,placa)
    self.motorMinimo = servo.servo(minino,placa)
    
    self.motorPolegar.move(0)
    self.motorIndicador.move(0)
    self.motorMedio.move(0)
    self.motorAnelar.move(0)
    self.motorMinimo.move(0)
    
  def moveHand(self,pos1, pos2 , pos3, pos4, pos5):
    self.motorPolegar.move(pos1)
   
    self.motorIndicador.move(pos2)

    self.motorMedio.move(pos3)
   
    self.motorAnelar.move(pos4)
    self.motorMinimo.move(pos5)

    
  def move(self,lmList):
    pos1 = self.disPolegar(lmList,0,2,4)
    pos2 = self.anguloInverso(lmList,0,5,8)
    pos3 = self.anguloNormal(lmList,0,9,12)
    pos4 = self.anguloInverso(lmList,0,13,16)
    pos5 = self.anguloInverso(lmList,0,17,20)
    self.moveHand(pos1,pos2,pos3,pos4,pos5)
    
  def calcularDistancia(self,lmList,pontoA,pontoB):
        x1, y1 = lmList[pontoA][1], lmList[pontoA][2]
        x2, y2 = lmList[pontoB][1], lmList[pontoB][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        #colocando na tela 
        
      #  cv2.circle(img, (x1, y1),5, (255, 0, 255), cv2.FILLED)
       # cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
       # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
      #  cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return(int((length/180)*100))
  def disPolegar(self,lmList,pontoA1,pontoB1,pontoB2):
        vetor1 = []
        vetor2 = []
        
        x11, y11 = lmList[pontoA1][1], lmList[pontoA1][2]
        x21, y21 = lmList[pontoB1][1], lmList[pontoB1][2]
        
        x12, y12 =lmList[pontoB1][1], lmList[pontoB1][2]
        x22, y22 =lmList[pontoB2][1], lmList[pontoB2][2]
        
        
        #cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        vetor1.append(x21 - x11)
        vetor1.append(y21 - y11)
        vetor2.append(x22 - x12)
        vetor2.append(y22 - y12)
        
        #colocando na tela 
        
      #  cv2.circle(img, (x1, y1),5, (255, 0, 255), cv2.FILLED)
       # cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
       # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
      #  cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        #length = math.hypot(x2 - x1, y2 - y1)
         
        angulo = angulos(vetor1,vetor2,0)
        
        if angulo == None:
          angulo = 0
       
        elif angulo <= 10 :
          angulo = 0
        elif angulo > 5 and angulo <=10:
          angulo = angulo
        elif angulo >10 and angulo <= 15:
          angulo = angulo + 5
        elif angulo >15 and angulo <= 20:
          angulo = angulo +5
        elif angulo >20 and angulo <= 25:
          angulo = angulo + 5
        elif angulo > 25 and angulo <=30:
          angulo = angulo + 5
        elif angulo >30 and angulo <=35:
          angulo = angulo + 5
        elif angulo >35 and angulo <=40:
          angulo = angulo + 5
        elif angulo > 40 and angulo <=45:
          angulo = angulo + 5
        elif angulo > 45 and angulo <= 50:
          angulo = angulo + 10
        elif angulo > 50 and angulo <= 55:
          angulo = angulo + 10
        elif angulo > 55 and angulo <= 60:
          angulo = angulo + 10
        elif angulo > 60 :
          angulo = angulo + 10
   
        
        

         
        
          
        angulo = np.abs(angulo)
          
         
        
        return(int(angulo))
          
  def anguloNormal(self,lmList,pontoA1,pontoB1,pontoB2):
        vetor1 = []
        vetor2 = []
        
        x11, y11 = lmList[pontoA1][1], lmList[pontoA1][2]
        x21, y21 = lmList[pontoB1][1], lmList[pontoB1][2]
        
        x12, y12 =lmList[pontoB1][1], lmList[pontoB1][2]
        x22, y22 =lmList[pontoB2][1], lmList[pontoB2][2]
        
        
        #cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        vetor1.append(x21 - x11)
        vetor1.append(y21 - y11)
        vetor2.append(x22 - x12)
        vetor2.append(y22 - y12)
        
        #colocando na tela 
        
      #  cv2.circle(img, (x1, y1),5, (255, 0, 255), cv2.FILLED)
       # cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
       # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
      #  cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        #length = math.hypot(x2 - x1, y2 - y1)
         
        angulo = angulos(vetor1,vetor2,0)
        
        if angulo == None:
          angulo = 0
       
        elif angulo <= 15 :
          angulo = 0
        elif angulo > 15 and angulo <=20:
          angulo = angulo
        elif angulo >20 and angulo <= 25:
          angulo = 45
        elif angulo >25 and angulo <= 30:
          angulo = angulo +55
        elif angulo >30 and angulo <= 35:
          angulo = angulo + 60
        elif angulo > 35 and angulo <=40:
          angulo = angulo + 75
        elif angulo >40 and angulo <=45:
          angulo = angulo + 90
        elif angulo >45 and angulo <=50:
          angulo = angulo + 105
        elif angulo > 50 and angulo <=55:
          angulo = angulo + 110
        elif angulo > 55 and angulo <= 60:
          angulo = angulo + 120
        elif angulo > 60:
          angulo = 180
   
        
        
          

          
        angulo = np.abs(angulo)
        
         
        
        return(int(angulo))
      
  
      
  def anguloInverso(self,lmList,pontoA1,pontoB1,pontoB2):
        vetor1 = []
        vetor2 = []
        
        x11, y11 = lmList[pontoA1][1], lmList[pontoA1][2]
        x21, y21 = lmList[pontoB1][1], lmList[pontoB1][2]
        
        x12, y12 =lmList[pontoB1][1], lmList[pontoB1][2]
        x22, y22 =lmList[pontoB2][1], lmList[pontoB2][2]
        
        
        #cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        vetor1.append(x21 - x11)
        vetor1.append(y21 - y11)
        vetor2.append(x22 - x12)
        vetor2.append(y22 - y12)
        
        #colocando na tela 
        
      #  cv2.circle(img, (x1, y1),5, (255, 0, 255), cv2.FILLED)
       # cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
       # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
      #  cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        #length = math.hypot(x2 - x1, y2 - y1)
         
        angulo = angulos(vetor1,vetor2,1) 
   
        if angulo == None:
          angulo = 0
       
        elif angulo <= 15 :
          angulo = 0
        elif angulo > 15 and angulo <=20:
          angulo = angulo
        elif angulo >20 and angulo <= 25:
          angulo = 45
        elif angulo >25 and angulo <= 30:
          angulo = angulo +55
        elif angulo >30 and angulo <= 35:
          angulo = angulo + 60
        elif angulo > 35 and angulo <=40:
          angulo = angulo + 75
        elif angulo >40 and angulo <=45:
          angulo = angulo + 90
        elif angulo >45 and angulo <=50:
          angulo = angulo + 105
        elif angulo > 50 and angulo <=55:
          angulo = angulo + 110
        elif angulo > 55 and angulo <= 60:
          angulo = angulo + 120
        elif angulo > 60:
          angulo = 180
        

       
          
        angulo = np.abs(angulo)
          
          
        print(int(angulo))
        
        return(int(angulo))
    