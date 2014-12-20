import utils

class Project(object):
    cache = {}

    @classmethod
    def project(cls, filepath):
        basepath = utils.basepath_from_filepath(filepath)
        return cache.get(basepath, cls(basepath))

    def __init__(self, basepath):
        self.basepath = basepath
        self._load_bookmarks()

    def add_bookmark(self, filepath, cursor):

        pass

    def add_bookmark_with_cursor(self, filepath, cursor):

        pass

class GlobalProject():
    pass




