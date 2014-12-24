import sys
import tempfile
import os
import logging

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

# NOTE replace the builtin vim module
sys.modules["vim"] = VimMock
logging.warning("vim module mocked out. Make sure you aren't seeing this inside of vim")

# NOTE vimmarks file for test
import config
config.store_file = tempfile.NamedTemporaryFile()
config.store_filepath = config.store_file.name

