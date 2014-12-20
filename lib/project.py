import utils

class Project(object):

    def __init__(self, filepath):

        self.basepath = utils.get_basepath(filepath)
        self.store_filepath = utils.get_store_filepath(self.basepath)



