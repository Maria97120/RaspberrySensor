import RPi.GPIO as GPIO
import os.path
import time

class MQData():
        def __init__(self):
                #GPIO.setwarning(False)
                channel=18
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(channel,GPIO.IN)
        def MQvalue(self):
                if GPIO.input(18) == GPIO.HIGH:
                        i=0
                elif GPIO.input(18) == GPIO.LOW:
                        i=1

                return i
