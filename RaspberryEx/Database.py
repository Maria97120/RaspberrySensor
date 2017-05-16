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
    
    def get_weather(self):
        TM_url = self.__url_dict["TM"]
        TMData = [-30,0]
        while (TMData[0] < -20 or TMData[0] > 35):
            TMData = json.loads(urllib2.urlopen(TM_url).read())
        self.__weather[0] = TMData[0]
        self.__weather[1] = TMData[1]

        rain_url = self.__url_dict["Rain"]
        self.__weather[2] = urllib2.urlopen(rain_url).read()

        mq_url = self.__url_dict["MQ"]
        self.__weather[3] = urllib2.urlopen(mq_url).read()
    
    @property
    def weather(self):
        self.get_weather()
        return self.__weather



class Database(object):
    def __init__(self):
        redisco.connection_setup(host = "localhost", port = 6379, db = 0)

    def use_database(self):
        weather_data = Weather.weather
        key = time.strftime('%Y-%m-%d %H',time.localtime(time.time()))
        weather_hash = Hash(key)
        weather_hash.hmset(
            { "temperature" : weather_data[0],
              "humidity"    : weather_data[1],
              "rain"        : weather_data[2],
              "mq"          : weather_data[3]
            }
        )
        return weather_hash.hgetall()


