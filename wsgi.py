#!/usr/bin/env python

import cherrypy
from notify import Notify 


app = cherrypy.tree.mount(Notify(), '/')

if __name__=='__main__':
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        })

    # Run the application using CherryPy's HTTP Web Server
    cherrypy.quickstart(Notify())
