import api

BANNED_GLOBAL_MAPPINGS = ('c', 'x', 'm', 'q')
BANNED_PROJECT_MAPPINGS = ()

try:
    import vim
except ImportError:
    import sys
    print "Please run this from within a vim python runtime, where the vim module is available"
    sys.exit(1)


def setup_vimmarks():
    """
    1. build mappings for writing/using project-specific bookmarks
    2. build mappings for global bookmarks
    """
    mappings = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                )

    def cb(prefix, mapping, callback):
        cmd = "map %s%s :python vimmarks.%s('%s')<CR>" % (prefix, mapping, callback, mapping)
        vim.command(cmd)

    for mapping in mappings:
        if mapping not in BANNED_GLOBAL_MAPPINGS:
            cb("m", mapping, "open_global_bookmark")
            cb("M", mapping, "save_global_bookmark")

        if mapping not in BANNED_PROJECT_MAPPINGS:
            cb('f', mapping, 'open_project_bookmark')
            cb('F', mapping, 'save_project_bookmark')


def create_project():
    api.create_project(vim.current.buffer.name)


def lock_project():
    pass


def save_project_bookmark(mapping):
    filepath = vim.current.buffer.name
    line, column = vim.current.window.cursor

    project = api.save_project_bookmark(mapping, filepath, line)


def open_project_bookmark(mapping):

    pass


def open_global_bookmark(mapping):
    bookmark = api.get_global_bookmark(mapping)
    if not bookmark:
        print "No global bookmark found for %s" % mapping
        return

    _open_bookmark(bookmark['filepath'], bookmark['line'])


def save_global_bookmark(mapping):
    filepath = vim.current.buffer.name
    line, column = vim.current.window.cursor

    api.save_global_bookmark(filepath, mapping, line=line)


def _open_bookmark(filepath, line=False):
    cmd = ":edit "
    if line:
        cmd += "+%d " % line
    cmd += "%s " % filepath

    vim.command(cmd)
