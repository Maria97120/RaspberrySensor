# -*- coding:utf-8 -*-
import os.path
import tornado.web
import json

import TMSensorData

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
        self.write("当前温度:" + str(TMvalue[0]) + "\n\r" + "当前湿度:" + str(TMvalue[1]))
        
