# -*- coding: utf-8 -*-
#
# plugin.video.netflix documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 26 16:27:25 2017.
from __future__ import absolute_import, division, unicode_literals


import os
import sys
import sphinx_rtd_theme

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
ROOT_PATH = os.path.dirname(os.path.dirname(BASE_PATH)) + os.path.sep

sys.path.insert(0, BASE_PATH)
sys.path.insert(0, ROOT_PATH)
sys.path.insert(0, ROOT_PATH + 'resources' + os.path.sep)
sys.path.insert(0, ROOT_PATH + 'resources' + os.path.sep + 'lib' + os.path.sep)

from setup import get_addon_data

ADDON_DATA = get_addon_data()

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'm2r']

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = ADDON_DATA.get('id', '')
copyright = u'2017, ' + ADDON_DATA.get('author', '')
author = ADDON_DATA.get('author', '')

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ADDON_DATA.get('version', '')
# The full version, including alpha/beta/rc tags.
release = ADDON_DATA.get('version', '')

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../resources/icon.png']
html_logo = '_static/icon.png'