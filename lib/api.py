import os
import os.path
import json


VIMMARKS_PATH = os.path.expanduser('~/.vimmarks')


def _path(subpath):
    return os.path.join(VIMMARKS_PATH, subpath)


def _setup():
    """
    If the basic directory structure doesn't exist yet, create it so that
    subsequent calls can be successfully made without breaking things.
    """
    if not os.path.exists(VIMMARKS_PATH):
        os.makedirs(VIMMARKS_PATH)

    if not os.path.exists(_path('projects')):
        os.makedirs(_path('projects'))

    if not os.path.exists(_path('files')):
        os.makedirs(_path('files'))

    if not os.path.exists(_path('global.json')):
        with open(_path('global.json'), 'w') as fh:
            fh.write(json.dumps({}))


_setup()


def _load(filepath):
    try:
        with open(os.path.join(VIMMARKS_PATH, filepath), 'r') as fh:
            return json.loads(fh.read())
    except (IOError, ValueError) as e:
        print e
        return None


def _save(filepath, data):
    try:
        with open(os.path.join(VIMMARKS_PATH, filepath), 'w') as fh:
            fh.write(json.dumps(data))
    except (IOError, ValueError) as e:
        print e
        return None


def save_project_bookmark(filepath, mapping, line=False):
    """
    This will save a bookmark for the existing project and will return
    True/False if the project doesn't exist.
    """
    pass


def save_file_bookmarks(filepath):
    pass


def get_file_bookmarks(filepath):
    """
    Fetch bookmarks for an individual filepath. This is useful
    """
    pass


def get_global_bookmark(mapping):
    bookmarks = _load('global.json')
    return bookmarks.get(mapping, None)


def save_global_bookmark(filepath, mapping, line=False):
    """
    This will write a new bookmark, or overwrite an existing bookmark into the
    bookmark store for global bookmarks.
    """
    bookmarks = _load('global.json')
    bookmarks[mapping] = {
        'filepath': filepath,
        'line': line,
    }

    _save('global.json', bookmarks)
