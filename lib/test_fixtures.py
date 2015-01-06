from bookmark import Bookmark

import sys
import re
import tempfile
import types
import os
import uuid

class Params(object):
    @classmethod
    def __setattribute__(self, *args, **kwargs):
        print "hi"
        pass

    @classmethod
    def memoized_lambda(cls, eval_string):
        uid = str(uuid.uuid1())

        def __(cls, uid, eval_string):
            if not hasattr(cls, uid):
                setattr(cls, uid, eval(eval_string))
            return getattr(cls, uid)

        _ = lambda x: __(cls, uid, eval_string)
        return _

class BookmarkParams(Params):
    name = "bookmark"
    shortcut = "aa"
    alias = "main"

    def __init__(self):
        self.tempfile = tempfile.NamedTemporaryFile()
        self.filepath = self.tempfile.name
        self.project = os.path.dirname(self.filepath)

class Fixture(object):
    def __init__(self, *args, **kwargs):
        self.params_object = self.params_klass()
        self.data = {}
        
        all_attributes = self.params_klass.__dict__.keys() + self.params_object.__dict__.keys()
        attributes = [attr for attr in all_attributes if not re.match(r'^__.*__$', attr)]

        for attr in attributes:
            value = getattr(self.params_object, attr)

            if hasattr(value, "__call__"):
                value = value()

            self.data[attr] = value
            setattr(self, attr, value)

for params_klass in [BookmarkParams,]:
    klass_name = params_klass.__name__.replace("Params", "")
    fixture_klass_name = params_klass.__name__.replace("Params", "Fixture")

    klass = locals().get(klass_name)
    fixture_klass = type(fixture_klass_name, (Fixture,), {})
    # NOTE klass is unneeded for now, potentially switch to use introspection and "hot swap" the class for the fixture
    setattr(fixture_klass, "klass", klass)
    setattr(fixture_klass, "params_klass", params_klass)

    # NOTE export the created class into this current module namespace
    setattr(sys.modules[__name__], fixture_klass_name, fixture_klass)


