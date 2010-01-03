import cherrypy
from readpao.models import ListItem
import datetime

class IndexController(object):

    @cherrypy.expose
    def index(self):
        return cherrypy.thread_data.templates.get_template("secret-alfa.html").render(title="ReadPao - Take-out reading - the secret is not out!")

    @cherrypy.expose
    def secretAlfa(self):
	    return cherrypy.thread_data.templates.get_template("secret-alfa.html").render(title="ReadPao - Take-out reading - the secret is not out!")
    
    @cherrypy.expose
    def read(self, id):
        store = cherrypy.request.dbstore
        item = store.find(ListItem, ListItem.id == int(id)).one()
        return cherrypy.thread_data.templates.get_template("item.html").render(item=item)

    @cherrypy.expose
    def mark_read(self, id):
        store = cherrypy.request.dbstore
        item = store.find(ListItem, ListItem.id == int(id)).one()
        item.date_read = datetime.datetime.now()
        store.commit()
        raise cherrypy.HTTPRedirect("/"+str(item.list_name))

    @cherrypy.expose
    def default(*args, **kwargs):
        store = cherrypy.request.dbstore
        list_name = args[1]
        list_items = store.find(ListItem, ListItem.list_name==list_name, ListItem.date_read==None)
        list_items = list_items.order_by(ListItem.time_to_read)
        return cherrypy.thread_data.templates.get_template("list.html").render(list_items=list_items, list_name=list_name)
