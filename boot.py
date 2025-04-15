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
#===========================================================
#                    SUPPORT FUNCTIONS
#===========================================================
def setPin(pin, val): Pin(pin, Pin.OUT).value(val)
def setPWM(pin, val, freq=1000): PWM(Pin(pin), freq=freq).duty(int(val*maxSpeed))

def getPin(pin): return Pin(pin, Pin.IN).value()
def getADC(pin): return ADC(Pin(pin, Pin.IN), atten=ADC.ATTN_11DB).read()
def inTape(pin): return isBlack ^ (getADC(pin)<blackValue)
#===========================================================
def getTest():
  print(f'{getSensor():07b}')
#===========================================================
#                   MOVIMENT FUNCTIONS
#===========================================================
def move(dir):
  for i in range(4):
    setPin(Motors[i], dir[i])

def setSpeed(left, right):
  setPWM(17, left)
  setPWM(16, right)

#===========================================================
def getSensor():
  sum = 0
  for pin in Sensor:
    sum = (sum<<1) + inTape(pin)
  return sum
