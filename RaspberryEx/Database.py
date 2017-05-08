import redisco
from redisco.containers import Hash

import urllib2
import time
import json

class Database(object):
    def __init__(self):
        redisco.connection_setup(host = 'localhost', port = 6379, db = 0)
    def get_url_data(self,url):
        data = json.loads(urllib2.urlopen(url).read())
        return data
    def use_database(self):
        values = self.get_url_data("http://192.168.0.108:8000/TM")
        key = time.strftime('%Y-%m-%d %H:%M:%s',time.localtime(time.time()))
        TM_hash = Hash(key)
        TM_hash.hmset(
	    {'temperature' : str(values[0]), 'humidity' : str(values[1])}
        )
        return TM_hash.hgetall()


