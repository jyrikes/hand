from pyfirmata import Arduino,SERVO
import time
import sys
from pymata4 import pymata4

class servo():
    def __init__(self,pin,board):
        self.board = board
        self.pin = pin
        #board.digital[pin].mode = SERVO
        board.set_pin_mode_servo(self.pin)

    def move(self,angle):
        #self.board.digital[self.pin].write(angle)
        self.board.servo_write(self.pin, angle)



