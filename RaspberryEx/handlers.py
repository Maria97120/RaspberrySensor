# -*- coding: utf-8 -*-
import module

handlers = [
    (r'/test', module.test),
    (r'/', module.IndexHandler),
    (r'/TM', module.TMHandler)

]
