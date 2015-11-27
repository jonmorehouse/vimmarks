# Vimmarks
> A plugin for bookmarking and navigating between files using vim.

## Overview

`Vimmarks` is a vim plugin for managing persistent bookmarks. It allows you to save and open bookmarks for many different projects and files on your computer all with just a few mappings.

By default, `Vimmarks` relies on the `m`, `M`, `f`, and `F` keys for mappings in normal mode. This is configurable so as to avoid conflicting with other mappings you may have in your editor.

`Vimmarks` is great for users who find themselves hanging out in `vim` while working on different projects, or simply don't want to have to constantly switch from their terminal to their editor to find files or directories.

## Global Bookmarks

Global bookmarks are useful for quickly opening projects, config files, directories or specific folders within `vim`.

Global bookmarks act similarly to the builtin `vim` bookmarking system. For instance, to bookmark the current file as `a`, you can enter `Ma`. By default, `vimmarks` saves new bookmarks by capitalizing the first letter (`M`).

Navigating back to the bookmark is as simple as pressing `ma` in normal mode.

## Project Bookmarks

Projects are workspaces which have their own bookmarks. For instance, lets say you have a few projects and you want to bookmark the README for each project. `Vimmarks` has the concept of projects so you can have bookmarks that make sense btu that change for each project.

Bookmarks work similarly to **global bookmarks** but use the `f` character for mapping (this is also configurable). For instance to bookmark your README to `a`, you could simple open the file and type `fa` in normal mode. This will 

Vimmarks intelligently tries to create projects based upon git repositories. When you create a project bookmark, it will attempt to find the project that corresponds to the current path by walking parent directories until it finds a `.git` folder. This is also configurable, as sometimes you may have multiple projects inside of a single repository. 

```vim
:NewProject 
:LockProject
```

When you switch directories, `vimmarks` will silently pick up changes and namespace your bookmarks automatically. You can also temporarily "stop" this auto-switching running `:LockProject`.


