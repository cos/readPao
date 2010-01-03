import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
from readpao.index_controller import IndexController
from readpao.api_controller import APIController
from storm.locals import *
import settings

def initialize(thread_index):
    cherrypy.thread_data.templates = TemplateLookup(directories=["views"], output_encoding='utf-8')
    print "Initialized template lookup for thread "+str(thread_index)

def initialize_database():
    database = database = create_database("mysql://"+settings.db_user+":"+settings.db_password+"@localhost:/"+settings.db_database)
    store = Store(database)
    cherrypy.request.dbstore = store
    print "Initialized db store for request"

def cleanup_database():
    cherrypy.request.dbstore.close()
    print "Closed db store connection"

cherrypy.engine.subscribe("start_thread", initialize)
cherrypy.tools.dbstore = cherrypy.Tool('before_handler', initialize_database)
cherrypy.tools.dbstore_cleanup = cherrypy.Tool('on_end_request', cleanup_database)
                        
cherrypy.config.update("readpao.config.global.conf")
readpaoroot = IndexController()
readpaoroot.api = APIController()
cherrypy.tree.mount(readpaoroot, "/", "readpao.config.conf")

cherrypy.engine.start()

