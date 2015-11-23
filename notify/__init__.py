import cherrypy

class Notify(object):
    @cherrypy.expose
    def index(self):
        return "Hello, world!"