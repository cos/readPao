import cherrypy
from readpao.models import ListItem
from readpao.content_grabber import *
import re
import math

class APIController(object):
    
    @cherrypy.expose
    def save(self, list=None, url=None, rand=None):
        # TODO: Validate list, url. Check if they are not None and if they don't already exist.
        new_item = ListItem(list, url)
        link,link_title,link_content,soup = myGrabContent(url)
        #link_content = re.sub("[\s]+"," ", link_content)
        soup_content = u''.join(soup.findAll(text=True))
        soup_content = re.sub("\\s[^\\s]{1,2}\\s"," ",soup_content)
        soup_content = re.sub("[\\s]+", " ", soup_content)
        new_item.content = link_content
        new_item.title = link_title
        new_item.time_to_read = round(len(soup_content.split(" "))/200.0)
        # TODO: Here we add any other attributes
        store = cherrypy.request.dbstore
        store.add(new_item)
        store.commit()
        return cherrypy.thread_data.templates.get_template("api_save_response.js").render(list_item=new_item) 
