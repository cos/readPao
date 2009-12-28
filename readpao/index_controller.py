import cherrypy

class IndexController(object):

    @cherrypy.expose
    def index(self):
        return cherrypy.thread_data.templates.get_template("index.html").render(title="ReadPao - Take-out reading")

