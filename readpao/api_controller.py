import cherrypy
from readpao.models import ListItem

class APIController(object):
    
    @cherrypy.expose
    def save(self, list=None, url=None):
        new_item = ListItem(list, url)
        # TODO: Here we add any other attributes
        store = cherrypy.thread_data.db_store
        store.add(new_item)
        store.commit()
        return cherrypy.thread_data.templates.get_template("api_save_response.js").render(list_item=new_item) 
