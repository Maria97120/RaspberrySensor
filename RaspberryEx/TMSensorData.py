import RPi.GPIO as GPIO
import time



class TMData(object):
    data = []
    fdata = []
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        time.sleep(0.5)
    def TMvalue(self):
        j = 0
        self.data = []
        self.fdata = []
        channel = 7 #GPIO7
        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(0.02)
        GPIO.output(channel, GPIO.HIGH)
        GPIO.setup(channel, GPIO.IN)

        while GPIO.input(channel) == GPIO.LOW:
            continue

        while GPIO.input(channel) == GPIO.HIGH:
            continue
    
        while j < 41:
            k = 0
            while GPIO.input(channel) == GPIO.LOW:
                continue
            while GPIO.input(channel) == GPIO.HIGH:
                k += 1
                if k > 100:
                    break
            self.fdata.append(k)
            if k < 15:
                self.data.append(0)
            else:
                self.data.append(1)
            j += 1
        return self.DataDeal()


    def DataDeal(self):
        #print self.data
        #print self.fdata
        humidity_bit = self.data[0:8]
        humidity_point_bit = self.data[8:16]
        temperature_bit = self.data[16:24]
        temperature_point_bit = self.data[24:32]
        check_bit = self.data[32:40]

        humidity = 0
        humidity_point = 0
        temperature = 0
        temperature_point = 0
        check = 0
        for i in range(8):
            humidity += humidity_bit[i] * 2 ** (7-i)
            humidity_point += humidity_point_bit[i] * 2 ** (7-i)
            temperature += temperature_bit[i] * 2 ** (7-i)
            temperature_point += temperature_point_bit[i] * 2 ** (7-i)
            check += check_bit[i] * 2 ** (7-i)

        tmp = humidity + humidity_point + temperature + temperature_point
        if check == tmp:
            print "temperature :", temperature, "*C, humidity :", humidity, "%"
        else:
            print "wrong fix it"
            temperature, humidity = self.Datafix()
        GPIO.cleanup()
        return temperature,humidity




#if check == tmp:
#    print "temperature :", temperature, "*C, humidity :", humidity, "%"
#else:
#    print "wrong"
#    print "temperature :", temperature, "*C, humidity :", humidity, "% check :", check, ", tmp :", tmp

#GPIO.cleanup()

    def Datafix(self):
        humidity_bit = self.data[1:9]
        temperature_bit = self.data[17:25]
        humidity = 0
        humidity_point = 0
        temperature = 0
        temperature_point = 0
        check = 0
        for i in range(8):
            humidity += humidity_bit[i] * 2 ** (7-i)
            temperature += temperature_bit[i] * 2 ** (7-i)
        return temperature,humidity