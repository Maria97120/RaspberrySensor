import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO

class RPIData():
        def __init__(self):
               # GPIO.setwarning(False)
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(12,GPIO.IN)
        def RPIvalue(self):
                i=0
                while(1):
                        if GPIO.input(12) == True:
                                print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' Waring:Someone is Closing!'
                                i=i+1
                                time.sleep(2.5)
                        else:
                               break;
                               # print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' Not anybody!'
                        #time.sleep(2.5)
                return i

