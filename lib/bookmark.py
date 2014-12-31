from store import store

import uuid
import json

class Bookmark(object):
    '''
    Responsible for managing state of the bookmark
    '''
    required_attrs = [
        "filepath",
        "shortcut",
        "alias",
        "project",
    ]

    optional_attrs = ["cursor"]



    @classmethod
    def create(cls, *args, **kwargs):
        '''
        Create a new bookmark and persist it to the store
        '''
        obj = cls()

        missing = [key for key in cls.required_attrs if not key in kwargs]
        if missing:
            raise Exception("Missing required parameters: %s" % ",".join(missing))
            return

        for attribute in cls.required_attrs + cls.optional_attrs:
            if kwargs.get(attribute):
                setattr(obj, kwargs.get(attribute))

        obj.save()
        return obj

    def __init__(self):
        self.id = uuid.uuid.v1()

    def save(self, **kwargs):
        store["bookmarks"][self.id] = json.dumps(self.__dict__)


