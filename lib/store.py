import sys
import json
import os
import logging

import config

class Store(dict):

    def __init__(self, filepath):
        self.filepath = filepath
        self.load()

    def load(self):
        '''
        Load vimmarks file into current object, create if it doesn't already exist
        '''
        if not os.path.isfile(self.filepath): return

        with open(self.filepath, "r") as fr:
            try:
                json_dict = json.loads(fr.read())
            except ValueError:
                logging.error("Invalid Json File")
            else:
                self.update(json_dict)
            
    def save(self):
        with open(self.filepath, "w") as fw:
            fw.write(json.dumps(self))

store = Store(config.store_filepath)
