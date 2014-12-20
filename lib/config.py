import vim_api as vim

class ConfigMetaclass(type):

    default_values = {
        "": ""
    }

    def __getattr__(cls, *args, **kwargs):
        return cls.values.get(args[0])

class Config(object):
    '''
    Return configuration from either vim or from defaults, if vim is not present
    '''
    __metaclass__ = ConfigMetaclass

