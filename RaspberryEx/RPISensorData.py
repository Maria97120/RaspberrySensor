import RPi.GPIO as GPIO
import time

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)
def detct():
    while True:
        if GPIO.input(12) == True:
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' Waring:Someone is Closing!'
        else:
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+' Not anybody!'
        time.sleep(2.5)
time.sleep(3)
init()
detct()
GPIO.cleanup()
