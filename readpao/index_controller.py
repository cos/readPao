import cherrypy

class IndexController(object):

    @cherrypy.expose
    def index(self):
        return cherrypy.thread_data.templates.get_template("index.html").render(title="ReadPao - Take-out reading")

    @cherrypy.expose
    def secretAlfa(self):
	return cherrypy.thread_data.templates.get_template("secret-alfa.html").render(title="ReadPao - Take-out reading - the secret is not out!")

