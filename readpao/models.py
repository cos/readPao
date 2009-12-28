from storm.locals import *
import datetime

class ListItem(object):
    __storm_table__ = "list_items"
    id = Int(primary=True)
    list_name = RawStr()
    url = RawStr()
    content = RawStr()
    title = RawStr()
    date_added = DateTime()
    date_read = DateTime()
    time_to_read = Int()

    def __init__(self, list_name, url):
        self.list_name = list_name
        self.url = url
        self.content = "Empty content for now"
        self.title = "Page title"
        self.date_added = datetime.datetime.now()
        self.time_to_read = 0       

