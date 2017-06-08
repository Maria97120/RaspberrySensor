# -*- coding:utf-8 -*-#
import os.path
import tornado.web
import json
import time

import TMSensorData
import RainSensorData
import RPISensorData
import MQSensorData
from Database import Database

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class barHandler(tornado.web.RequestHandler):
	def get(self):
		mon = 3
		tue = 4
		wed = 3
		thu = 4
		fri = 3
		sat = 5
		sun = 2

		self.render('bar.html',Mon=mon,Tue=tue,Wed=wed,Thu=thu,Fri=fri,Sat=sat,Sun=sun )
		
class lineHandler(tornado.web.RequestHandler):
	def get(self):
		a=[]
		b=[]
		k=0
		i=2
		j=4
		while(k<24):
			a.append(i)
			k=k+1
			i=i+1
		k=0
		while(k<24):
			b.append(j)
			k=k+1
			j=j+1
		fog="has fog"
		self.render('line.html',fog=fog,tem0=a[0],tem1=a[1],tem2=a[2],tem3=a[3],tem4=a[4],tem5=a[5],tem6=a[6],tem7=a[7],tem8=a[8],tem9=a[9],tem10=a[10],tem11=a[11],tem12=a[12],tem13=a[13],tem14=a[14],tem15=a[15],tem16=a[16],tem17=a[17],tem18=a[18],tem19=a[19],tem20=a[20],tem21=a[21],tem22=a[22],tem23=a[23],hum0=b[0],hum1=b[1],hum2=b[2],hum3=b[3],hum4=b[4],hum5=b[5],hum6=b[6],hum7=b[7],hum8=b[8],hum9=b[9],hum10=b[10],hum11=b[11],hum12=b[12],hum13=b[13],hum14=b[14],hum15=b[15],hum16=b[16],hum17=b[17],hum18=b[18],hum19=b[19],hum20=b[20],hum21=b[21],hum22=b[22],hum23=b[23])
		
class linepeopleHandler(tornado.web.RequestHandler):
	def get(self):
		a=[]
		i=0
		while(i<24):
			a.append(i)
			i=i+1
		
		self.render('line_people.html',peo0=a[0],peo1=a[1],peo2=a[2],peo3=a[3],peo4=a[4],peo5=a[5],peo6=a[6],peo7=a[7],peo8=a[8],peo9=a[9],peo10=a[10],peo11=a[11],peo12=a[12],peo13=a[13],peo14=a[14],peo15=a[15],peo16=a[16],peo17=a[17],peo18=a[18],peo19=a[19],peo20=a[20],peo21=a[21],peo22=a[22],peo23=a[23])
		
class test(tornado.web.RequestHandler):
    def get(self):
	a=[1,2,3,4,5,6,7]
	json_a=json.dumps(a)
        self.write(json_a)

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
        #people=people-2
        #time_key=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #people_dict = {time_key:str(people)}
        #json_RPIvalue = json.dumps(people_dict)
        self.write(str(people))

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
        database = Database()
	while True:
            database.run()
