import sys
try:
    import vim
except ImportError:
    vim = False

class MockMetaclass(type):
    def __getattr__(cls, *args, **kwargs):
        return 

class VimMock(object):
    __metaclass__ = MockMetaclass

if not vim:
    sys.modules["vim"] = VimMock

