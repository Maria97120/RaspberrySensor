#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from RaspberryEx import app
import RaspberryEx.handlers as handlers

import os.path
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)



if __name__ == '__main__':
    tornado.options.parse_command_line()

    parameters_dict = {
        "test"   : handlers.handlers[0],
        "sensors": handlers.handlers[1:6],
        "TM"     : handlers.handlers[2],
        "Rain"   : handlers.handlers[3],
        "RPI"    : handlers.handlers[4],
        "MQ-2"   : handlers.handlers[5],
        "DB"     : handlers.handlers[6]
    }

    parameters_list = [parameter for parameter in sys.argv[1:] if parameter in parameters_dict]
    handlers_list = []
    for parameter in parameters_list:
        handlers_list.append(parameters_dict[parameter])

    if not handlers_list:
        handlers_list = handlers.handlers

    app = tornado.web.Application(
        handlers = handlers_list,
        #template_path=os.path.join(os.path.dirname(__file__), "templates")
        debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
