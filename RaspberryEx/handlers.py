# -*- coding: utf-8 -*-
import module

handlers = [
    (r'/test', module.test),
    (r'/', module.IndexHandler),
    (r'/TM', module.TMHandler),
    (r'/Rain',module.RainHandler),
    (r'/RPI',module.RPIHandler),
    (r'/MQ-2',module.MQHandler)	

]
