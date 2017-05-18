import redisco
from redisco.containers import Hash

import urllib2
import time
import json

class Weather(object):
    def __init__(self):
        self.__weather = [0,0,0,0]
        self.__url_dict = {
            "TM"   : "http://192.168.0.108:8000/TM",
            "Rain" : "http://192.168.0.108:8000/Rain",
            "MQ"   : "http://192.168.0.108:8000/MQ-2"
        }
    
    def set_weather(self):
        TM_url = self.__url_dict["TM"]
        TMData = [-30,0]
        while (int(TMData[0]) < -20 or int(TMData[0]) > 35):
            TMData = json.loads(urllib2.urlopen(TM_url).read())
        self.__weather[0] = TMData[0]
        self.__weather[1] = TMData[1]

        rain_url = self.__url_dict["Rain"]
        self.__weather[2] = urllib2.urlopen(rain_url).read()

        mq_url = self.__url_dict["MQ"]
        self.__weather[3] = urllib2.urlopen(mq_url).read()
    
    def get_weather(self):
        self.set_weather()
        return self.__weather

class Visitors(object):
    def __init__(self):
        self.__visitors = 0
        self.__url = "http://192.168.0.108:8000/RPI"
    
    def set_visitors(self):
        self.__visitors = urllib2.urlopen(self.__url).read()

    def get_visitors(self):
        self.set_visitors()
        return self.__visitors

class Database(object):
    def __init__(self):
        redisco.connection_setup(host = "localhost", port = 6379, db = 0)

    def weather(self):
        weather_data = Weather().get_weather()
        weather_key = 'weather.' + time.strftime('%Y-%m-%d %H',time.localtime(time.time()))
        weather_hash = Hash(weather_key)
        weather_hash.hmset(
            { "temperature" : weather_data[0],
              "humidity"    : weather_data[1],
              "rain"        : weather_data[2],
              "mq"          : weather_data[3]
            }
        )

    def visitors(self, visitors = 0):
        visitors_key  = 'rpi.' + time.strftime('%Y-%m-%d %H',time.localtime(time.time()))
        visitors_hash = Hash(visitors_key)
        visitors_hash.hset (visitors_key , visitors) 
    
    def run(self):
        current_time = time.localtime(time.time())
        visitors_perhor = 0
        self.weather()
        while time.localtime(time.time())[3] == current_time[3]:
            visitors_persec = Visitors().get_visitors()
            visitors_perhor = int(visitors_perhor) + int(visitors_persec)
        self.visitors(str(visitors_perhor))



