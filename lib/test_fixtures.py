from bookmark import Bookmark

import sys
import re
import tempfile
import types
import os

class Params(object):
    @classmethod
    def __setattribute__(self, *args, **kwargs):
        pass

class BookmarkParams(Params):
    tempfile = lambda x, o: tempfile.NamedTemporaryFile()
    filepath = lambda x, o: o.tempfile.name
    name = "bookmark"
    shortcut = "aa"
    project = lambda x, o: os.path.dirname(o.filepath)
    alias = "main"

class FullBookmarkParams(BookmarkParams):
    pass

class Fixture(object):
    def __init__(self, *args, **kwargs):
        self.params_object = self.params_klass()
        self.data = {}
        
        attributes = [attr for attr in self.params_klass.__dict__.iterkeys() if not re.match(r'^__.*__$', attr)]

        for attr in attributes:
            value = getattr(self.params_object, attr)

            if hasattr(value, "__call__"):
                value = value(self)

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


