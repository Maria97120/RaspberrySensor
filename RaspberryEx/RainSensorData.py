import RPi.GPIO as GPIO
import os.path
import time
import smbus


class RainData():
        def __init__(self):
                #GPIO.setwarning(False)
                channel=16
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(channel,GPIO.IN)
        def Rainvalue(self):
		channel=16
		RainValue=0
                if GPIO.input(channel) == GPIO.LOW:
                        i=1
			address = 0x48
			A0 = 0x40
			A1 = 0x41
			A2 = 0x42
			A3 = 0x43
			bus = smbus.SMBus(1)


		        bus.write_byte(address,A0)
         		value = bus.read_byte(address)
         		print("AOUT:%f  ",value)

			if(value>165):
				RainValue=0
			elif(value>150 and value<=165):
				RainValue=1
			elif(value>140 and value<=150):
				RainValue=2
			elif(value>130 and value<=140):
				RainValue=3
			elif(value>120 and value<=130):
				RainValue=4
			elif(value>110 and value<=120):
				RainValue=5
			elif(value>100 and value<=110):
				RainValue=6
			elif(value<=100):
				RainValue=7

                elif GPIO.input(channel) == GPIO.HIGH:
                        i=0
			RainValue=0

                return i,RainValue

