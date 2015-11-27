import os
import os.path
import json
import base64


VIMMARKS_PATH = os.path.expanduser('~/.vimmarks')

CACHE = {}

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

    if not os.path.exists(_path('global.json')):
        with open(_path('global.json'), 'w') as fh:
            fh.write(json.dumps({}))

    # TODO: build a CACHE['known_projects'] dict


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


def _save_project(data):
    filename = base64.b64encode(data['directory']) + ".json"
    _save("projects/" + filename, data)


def _load_project(filepath):
    filename = base64.b64encode(data['directory']) + ".json"
    return _load("projects/" + filename)


def _guess_project_directory(filepath):
    """
    Guess a project directory by looking for a source control directory (.git)
    or by looking to see if the project is parallel to other projects.
    """
    return os.path.dirname(filepath)


def _project_from_filepath(filepath):
    if CACHE.get('locked_project'):
        return CACHE['locked_project']

    while len(filedir.split('/')) > 1:
        if filedir in CACHE['known_projects']:
            return _load_project(filedir)

        filedir = os.path.abspath(os.path.join(filedir, "../"))

    # no project was found above this filepath. Go ahead and create one at the
    # most logical point we can think of
    project_directory = _guess_project_directory(filepath)
    project = create_project(project_directory)


def save_project_bookmark(filepath, mapping, line=False):
    """
    This will save a bookmark for the existing project and will return
    True/False if the project doesn't exist.
    """
    project = _project_from_filepath(filepath)
    project[mapping] = {
        'filepath': filepath,
        'line': line,
    }


def create_project(filepath):
    """
    Create a project in the current directory
    """
    current_dir = os.path.dirname(filepath)
    project = {
        'mappings': {},
        'directory': current_dir,
    }

    _save_project(project)
    CACHE['known_projects'][current_dir] = True
    return project


#def toggle_project_lock(filepath):
    #if CACHE.get('locked_project'):
        #del CACHE['locked_project']
        #return False
    #else:
        #CACHE['locked_project'] = project_for_filepath(filepath)['directory']
        #return True


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
