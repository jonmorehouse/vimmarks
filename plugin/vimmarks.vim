if exists("g:vimmarks_loaded") && !exists("g:vimmarks_debug") || &cp
  finish
endif
let g:vimmarks_loaded = 1

if !has("python")
  echo "vimmarks.vim requires Python support."
  finish
endif

python <<EOF
import sys
import vim
from os.path import abspath, join

base_path = abspath(join(vim.eval("expand('<sfile>:p:h')"), "../lib"))
sys.path.insert(0, base_path)

import vimmarks

if vim.eval('g:vimmarks_debug'):
  import imp
  imp.reload(vimmarks)
  imp.reload(vimmarks.api)

vimmarks.setup_vimmarks()
EOF

command! VimmarksCreateProject :python vimmarks.create_project()
command! VimmarksLockProject :python vimmarks.lock_project()
