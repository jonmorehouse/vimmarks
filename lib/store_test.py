import test_setup

import json

import config
import store

class TestStore(object):

    def test_store_save(self):
        store.store["bookmark"] = "bookmark_value"
        store.store.save()

        assert json.dumps({"bookmark": "bookmark_value"}) == config.store_file.read()

    def test_store_load(self):
        value_dict = {"bookmark": "bookmark_value"}
        config.store_file.write(json.dumps(value_dict))
        
        test_store = store.Store(config.store_filepath)
        assert test_store == value_dict
        
