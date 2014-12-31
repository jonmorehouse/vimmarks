from bookmark import Bookmark

import sys
import re
import tempfile

class Params(object):

    @classmethod
    def __setattribute__(self, *args, **kwargs):
        print "made it here"

class BookmarkParams(Params):
    filepath = lambda x: tempfile.tempfile()

class Fixture(object):
    def __init__(self):
        pass

for params_klass in [BookmarkParams,]:
    klass_name = params_klass.__name__.replace("Params", "")
    fixture_klass_name = params_klass.__name__.replace("Params", "Fixture")

    klass = locals().get(klass_name)
    fixture_klass = type(fixture_klass_name, (Fixture,), {})
    setattr(fixture_klass, "klass", klass)
    setattr(fixture_klass, "params", params_klass)

    # NOTE export the created class
    setattr(sys.modules[__name__], fixture_klass_name, fixture_klass)


