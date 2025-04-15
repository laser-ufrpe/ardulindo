#===========================================================
#                      BLUETOOTH CODE
#===========================================================
import time
from machine import Pin, ADC, PWM

import ble_repl
ble_repl.start()
#===========================================================
#                  ENVIROMENT VARIABLES
#===========================================================
isBlack = 1           # Tape color
maxSpeed = 700        # Max PWM Speed     (0-1023)
blackValue = 3500     # Set What is Black (0-4095) 

Motors = [2, 4, 0, 15]                # set motors pins
Sensor = [27, 26, 25, 33, 32, 35, 34] # sensor pins

Stop = [0,0,0,0]                     # stop direction
Front, Back = [0,1,0,1], [1,0,1,0]   # front and back directions
Right, Left = [1,0,0,0], [0,0,1,0]   # right and left directions
