import sys
import tempfile
import os

try:
    import vim
except ImportError:
    vim = False

# NOTE initialize vimmock class
class MockMetaclass(type):
    def __getattr__(cls, *args, **kwargs):
        return 

class VimMock(object):
    __metaclass__ = MockMetaclass

if not vim:
    sys.modules["vim"] = VimMock


# NOTE vimmarks file for test
import config
config.store_file = tempfile.NamedTemporaryFile()
config.store_filepath = config.store_file.name
