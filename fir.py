"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys
import time

from pymata4 import pymata4

"""
This program tests an ESP-8266 using StandardFirmataWiFi.
It will toggle the on-board LED 4 times.

Change the IP address and IP port to match that in the
StandardFirmataWiFi config file.
"""

# some globals

IP_ADDRESS = "10.0.0.117"
IP_PORT = 3030

def servo(my_board, pin,angulo):
    """
    Set a pin to servo mode and then adjust
    its position.
    :param my_board: pymata4
    :param pin: pin to be controlled
    """

    # set the pin mode
    my_board.set_pin_mode_servo(pin)

    # set the servo to 0 degrees
    my_board.servo_write(pin, angulo)




board = pymata4.Pymata4(ip_address=IP_ADDRESS, ip_port=IP_PORT)
while True:
    try:
        print("Conect")
        angulo = int(input("Digite o angulo : "))
        servo(board, 5,angulo)
        servo(board, 16,angulo)
        servo(board, 4,angulo) # vai de 180 a 0
        servo(board, 0,angulo)
        servo(board, 2,angulo)

    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)