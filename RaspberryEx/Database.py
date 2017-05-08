import redisco
from redisco.contianers import Hash

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
        #values = self.get_url_data(url)
        values = [10,11]
        key = time.strftime('%Y-%m-%d %H:%M:%s',time.localtime(time.time()))
        TM_hash = Hash(key)
        TM_hash.hmset(
            {'temperature' : str(values[0]), 'humidity' : str(values[1])}
        )
        return TM_hash.hgetall()


