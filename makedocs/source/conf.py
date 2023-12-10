#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# lifelib documentation build configuration file, created by
# sphinx-quickstart on Sat Nov 11 16:48:39 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(here + "../.."))

# Insert project path in sys.path so that each directory under
# the path is interpreted as the top level package in the API reference.
sys.path.insert(0, os.path.abspath(here + "/../../lifelib/projects"))
sys.path.insert(0, os.path.abspath(here + "/../../lifelib/libraries"))
sys.path.insert(0, '')  # Add the current folder at front.

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'nbsphinx',
    'nbsphinx_link',
    'sphinx_gallery.gen_gallery',
    'sphinx_design',
    'myst_parser',
    'sphinxcontrib.mermaid'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'lifelib'
copyright = '2018-2023, lifelib Developers'
author = 'lifelib Developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import lifelib
version = lifelib.__version__
# The full version, including alpha/beta/rc tags.
release = lifelib.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    '_build',
    '**.ipynb_checkpoints',
    'generated_examples/*/*.py',
    'generated_examples/*/*.ipynb'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = "images/logo.png"

html_title = "lifelib " + version

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

# See below for options of bootstrap theme
# https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html
html_theme_options = {

    "header_links_before_dropdown": 8,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lifelib-dev/lifelib",
            "icon": "fab fa-github-square"
        }
    ],
    "external_links": [
        {"name": "Discussions", "url": "https://github.com/lifelib-dev/lifelib/discussions"}
    ],
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "lifelib-favicon-16x16.png",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "lifelib-favicon-32x32.png",
        },
        {
            "rel": "apple-touch-icon",
            "sizes": "180x180",
            "href": "lifelib-favicon-32x32.png",
        },
    ]

}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "index": None,
    "notebooks": None,
    "generated_examples/**": None
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'lifelibdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'lifelib.tex', 'lifelib Documentation',
     'lifelib Developers', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'lifelib', 'lifelib Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'lifelib', 'lifelib Documentation',
     author, 'lifelib', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Auto doc -----------------------------------------------
# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# https://stackoverflow.com/questions/20864406/remove-package-and-module-name-from-sphinx-function
add_module_names = False

# -- Options for Auto summary -------------------------------------------
autosummary_generate = True
# autoclass_content = 'class'
# autodoc_default_flags = [
#     'members', 'inherited_members',  # 'undoc-members',
#     'show-inheritance']
#     # , 'private-members', 'special-members']

autodoc_default_options = {
    # 'members': True,
    # 'member-order': 'bysource',
    # 'inherited_members': True,
    # 'show-inheritance': True
    # 'special-members': '__init__',
    # 'undoc-members': True,
    # 'exclude-members': '__weakref__'
}

autodoc_member_order = 'bysource'


# -- Options for Gallery -------------------------------------------
from sphinx_gallery.sorting import ExplicitOrder, FileNameSortKey
sphinx_gallery_conf = {
    # path to your examples scripts
    'ignore_pattern': '^(?!.*plot_)',
    'examples_dirs': '../../lifelib/projects',
    'subsection_order': ExplicitOrder(
        ['../../lifelib/projects/savings',
         '../../lifelib/projects/economic',
         '../../lifelib/projects/fastlife',
         '../../lifelib/projects/simplelife',
         '../../lifelib/projects/nestedlife',
         '../../lifelib/projects/ifrs17sim',
         '../../lifelib/projects/solvency2',
         '../../lifelib/projects/smithwilson']),
    # path where to save gallery generated examples
    'gallery_dirs': 'generated_examples',
    # Suppress warning:
    'backreferences_dir': None,
    'download_all_examples': False,
    # 'download_section_examples': False,
    'capture_repr': (),
    'within_subsection_order': FileNameSortKey
}

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# https://sphinx-panels.readthedocs.io/en/latest/
panels_add_bootstrap_css = False

# Hide download note and buttons from gallery pages.
# https://github.com/ryan-roemer/sphinx-bootstrap-theme

# Fix mermaid
nbsphinx_requirejs_path = ''

def setup(app):
    app.add_css_file("custom-style.css")
