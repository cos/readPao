import cherrypy

class APIController(object):
    
    @cherrypy.expose
    def save(self, list=None, url=None):
       return "Called save with list="+str(list)+" and url="+str(url) 
