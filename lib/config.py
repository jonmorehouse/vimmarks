import vim_api as vim

class Config(object):
    '''
    Return configuration from either vim or from defaults, if vim is not present
    '''
    class Meta(object):

        def __getattr__(self, *args, **kwargs):
            pass

