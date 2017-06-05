# -*- coding: utf-8 -*-
import module

handlers = [
    (r'/test', module.test),
    (r'/', module.IndexHandler),
    (r'/bar.html',module.barHandler),
    (r'/line.html',module.lineHandler),
    (r'/line_people.html',module.linepeopleHandler),
    (r'/TM', module.TMHandler),
    (r'/Rain',module.RainHandler),
    (r'/RPI',module.RPIHandler),
    (r'/MQ-2',module.MQHandler),
    (r'/DB',module.DBHandler)

]
