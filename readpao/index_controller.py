import cherrypy
from readpao.models import ListItem

class IndexController(object):

    @cherrypy.expose
    def index(self):
        return cherrypy.thread_data.templates.get_template("index.html").render(title="ReadPao - Take-out reading")

    @cherrypy.expose
    def secretAlfa(self):
	    return cherrypy.thread_data.templates.get_template("secret-alfa.html").render(title="ReadPao - Take-out reading - the secret is not out!")

    @cherrypy.expose
    def default(*args, **kwargs):
        store = cherrypy.thread_data.db_store
        list_items = store.find(ListItem, ListItem.list_name==args[1])
        return cherrypy.thread_data.templates.get_template("list.html").render(list_items=list_items)

