import Servo as servo
import math
import numpy as np
def angulos(vetor1, vetor2):
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
    pos1 = self.calcularDistanciaPolegar(lmList,0,2,4)
    pos2 = self.calcularDistancia(lmList,0,8)
    pos3 = self.calcularDistancia(lmList,0,12)
    pos4 = self.calcularDistancia(lmList,0,16)
    pos5 = self.calcularDistancia(lmList,0,20)
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
  def calcularDistanciaPolegar(self,lmList,pontoA1,pontoB1,pontoB2):
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
         
        angulo = angulos(vetor1,vetor2)
   
        
        

        if angulo == None:
          angulo = 0
        if angulo > 50:
          angulo = 50
        if angulo < 15:
          angulo = 0
          
        angulo = np.abs(angulo)
          
          
        print(int(angulo))
        
        return(int(angulo))
    