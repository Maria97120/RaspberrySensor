# -*- coding:utf-8 -*-#
import os.path
import tornado.web
import json
import time

import TMSensorData
import RainSensorData
import RPISensorData
import MQSensorData
import Database

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('index.html')

class test(tornado.web.RequestHandler):
    def get(self):
        self.write("hello test")

class TMHandler(tornado.web.RequestHandler):
    '''temperature and moistrue'''   
    def get(self):
        TMvalue = TMSensorData.TMData().TMvalue()
        #self.write("当前温度:" + str(TMvalue[0]) + "\n\r" + "当前湿度:" + str(TMvalue[1]))
        json_TMvalue = json.dumps(TMvalue)
        self.write(json_TMvalue)

class RainHandler(tornado.web.RequestHandler):
    '''Raindrops module MH-RD '''
    def get(self):
        rain=RainSensorData.RainData().Rainvalue()
        #if rain[0]==1:
            #self.write("raining now "+"\n\r"+str(rain[1]))
        #else:
            #self.write("no raining "+"\n\r"+str(rain[1]))
        #json_Rainvalue = json.dumps(str(rain[1]))
        self.write(str(rain[1]))


class RPIHandler(tornado.web.RequestHandler):
    ''' �流量 '''
    def get(self):
        people=RPISensorData.RPIData().RPIvalue()
        people=people-2
        time_key=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        people_dict = {time_key:str(people)}
        json_RPIvalue = json.dumps(people_dict)
        self.write(json_RPIvalue)

class MQHandler(tornado.web.RequestHandler):
    '''MQ-2'''
    def get(self):
        MQ=MQSensorData.MQData().MQvalue()
        #if MQ==1:
            #self.write("has MQ")
        #else:
            #self.write("no MQ")
        #json_MQvalue = json.dumps(str(MQ))
        self.write(str(MQ))

class DBHandler(tornado.web.RequestHandler):
    '''Database'''
    def get(self):
        database = Database.Database()
        self.write(database.use_database())
