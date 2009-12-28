import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
from readpao.index_controller import IndexController
from readpao.api_controller import APIController
from storm.locals import *

def initialize(thread_index):
    cherrypy.thread_data.templates = TemplateLookup(directories=["views"])
    database = create_database("mysql://readpao:paoread123@localhost:/readpao")
    store = Store(database)
    cherrypy.thread_data.db_store = store

cherrypy.engine.subscribe("start_thread", initialize)
                        
cherrypy.config.update("readpao.config.global.conf")
readpaoroot = IndexController()
readpaoroot.api = APIController()
cherrypy.tree.mount(readpaoroot, "/", "readpao.config.conf")

cherrypy.server.quickstart()
cherrypy.engine.start()

