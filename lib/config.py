import vim
import utils
import sys

class ConfigMetaclass(type):

    variable_namespace = "VimMark"

    @classmethod
    def to_vim_varname(self, varname):
        return "".join(piece.capitalize() for piece in varname.split("_"))

    def __getattr__(cls, name):
        varname = cls.to_vim_varname(name)

        value = vim.eval("g:%s%s" % (cls.variable_namespace, name))

        if name.endswith("int"):
            return int(value)
        if name.endswith("float"):
            return float(value)

        return value 


class Config(object):
    '''
    Return configuration from either vim or from defaults, if vim is not present
    '''
    __metaclass__ = ConfigMetaclass

sys.modules[__name__] = Config
