# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'project-template'
copyright = '2019, Miro Adamy'
author = 'Miro Adamy'
release = '0.9.0'
version = '0.8'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']




# == NDD DOCKER SPHINX - OVERRIDE ============================================

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    # 'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',

#    'sphinx-prompt',

    'sphinxcontrib.actdiag',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.excel_table',
  # 'sphinxcontrib.googleanalytics',
  # 'sphinxcontrib.googlechart',
  # 'sphinxcontrib.googlemaps',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.packetdiag',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.seqdiag',
]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# If true, 'todo' and 'todoList' produce output, else they produce nothing.
todo_include_todos = True

# -- Markdown ----------------------------------------------------------------
# http://www.sphinx-doc.org/en/stable/usage/markdown.html

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

# -- Pseudo extensions -------------------------------------------------------

# Uncomment to enable Git parsing
# TODO: extract in a Sphinx plugin
#
# Must be defined somewhere
# html_context = {}
#
# import os.path
# source_directory = os.path.dirname(os.path.realpath(__file__))
# python_directory = os.path.join(source_directory, '_python')
# exec(open(os.path.join(python_directory, 'sphinx-git.py'), 'rb').read())

# -- Generator properties ----------------------------------------------------

# The Docker tag of the image that generated this project
ddidier_sphinxdoc_image_tag = '43af7d1cd588bb8b39bd0dafe2cfa2ccf710e6705b864785d8a8b4669e3432b0'
# The Git tag of the image that generated this project
# This is the most recent tag if the image is 'latest'
# Hopefully it will be (manually) updated while releasing...
ddidier_sphinxdoc_git_tag = '2.2.1-1'
