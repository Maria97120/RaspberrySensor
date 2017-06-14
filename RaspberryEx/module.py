# -*- coding:utf-8 -*-#
import os.path
import tornado.web
import json
import time
import datetime

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
		db = Database("10.203.87.18",6379,0)
		current_time = time.strftime('%Y-%m-%d %H',time.localtime(time.time()))
		week1 = datetime.datetime.now()
		week = week1.weekday()
		t = int (db.get_data("weather." + current_time, "rain"))
		mon = 0
		tue = 0
		wed = 0
		thu = 0
		fri = 0
		sat = 0
		sun = 0
		if(week == 0):
			mon = t
		elif(week ==1):
			tue = t
		elif(week ==2):
			wed = t
		elif(week ==3):
			thu = t
		elif(week ==4):
			fri =t
		elif(week ==5):
			sat = t
		elif(week == 6):
			sun = t
		
		self.render('bar.html',Mon=mon,Tue=tue,Wed=wed,Thu=thu,Fri=fri,Sat=sat,Sun=sun )
		
class lineHandler(tornado.web.RequestHandler):
	def get(self):
		db = Database("10.203.87.18",6379,0)
                current_time = time.strftime('%Y-%m-%d ',time.localtime(time.time()))
		tem_key = []
		hum_key = []
		tem = []
		hum = []
		i=0
		while(i<24):
			if(i<10):
				tem_key.append("weather."+current_time+'0'+str(i))
				hum_key.append("weather."+current_time+'0'+str(i))
			else:
				tem_key.append("weather."+current_time+str(i))
                                hum_key.append("weather."+current_time+str(i))
			i=i+1
		
		i=0
		while(i<24):
			tem.append(int (db.get_data(tem_key[i], "temperature")))
			hum.append(int (db.get_data(hum_key[i], "humidity")))
			i=i+1
		current_time = time.strftime('%Y-%m-%d %H',time.localtime(time.time()))
		fog  = int (db.get_data("weather." + current_time, "mq"))
		if(fog ==0):
			fog = "No fog"
		elif (fog == 1):
			fog = "Has fog"
		else:
			fog = "Error fog"

		self.render('line.html',fog=fog,tem0=tem[0],tem1=tem[1],tem2=tem[2],tem3=tem[3],tem4=tem[4],tem5=tem[5],tem6=tem[6],tem7=tem[7],tem8=tem[8],tem9=tem[9],tem10=tem[10],tem11=tem[11],tem12=tem[12],tem13=tem[13],tem14=tem[14],tem15=tem[15],tem16=tem[16],tem17=tem[17],tem18=tem[18],tem19=tem[19],tem20=tem[20],tem21=tem[21],tem22=tem[22],tem23=tem[23],hum0=hum[0],hum1=hum[1],hum2=hum[2],hum3=hum[3],hum4=hum[4],hum5=hum[5],hum6=hum[6],hum7=hum[7],hum8=hum[8],hum9=hum[9],hum10=hum[10],hum11=hum[11],hum12=hum[12],hum13=hum[13],hum14=hum[14],hum15=hum[15],hum16=hum[16],hum17=hum[17],hum18=hum[18],hum19=hum[19],hum20=hum[20],hum21=hum[21],hum22=hum[22],hum23=hum[23])
		
class linepeopleHandler(tornado.web.RequestHandler):
	def get(self):
		db = Database("10.203.87.18",6379,0)
                current_time = time.strftime('%Y-%m-%d ',time.localtime(time.time()))
		people_key = []
		people = []
		i=0
		while(i<24):
			if(i<10):
				people_key.append("rpi."+current_time+'0'+str(i))
			else:
				people_key.append("rpi."+current_time+str(i))
			i=i+1
		i=0
		while(i<24):
			people.append(int(db.get_data(people_key[i], "visitors flowrate")))
			i=i+1
		self.render('line_people.html',peo0=people[0],peo1=people[1],peo2=people[2],peo3=people[3],peo4=people[4],peo5=people[5],peo6=people[6],peo7=people[7],peo8=people[8],peo9=people[9],peo10=people[10],peo11=people[11],peo12=people[12],peo13=people[13],peo14=people[14],peo15=people[15],peo16=people[16],peo17=people[17],peo18=people[18],peo19=people[19],peo20=people[20],peo21=people[21],peo22=people[22],peo23=people[23])
		
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
