# -*- coding: utf-8 -*-
#
# openstackdocstheme documentation build configuration file

import openstackdocstheme
from openstackdocstheme.version import version_info

# Release name for PDF documents
latex_custom_template = r"""
\usepackage{""" + openstackdocstheme.get_pdf_theme_path() + """}
\\newcommand{\openstacklogo}{""" + openstackdocstheme.get_openstack_logo_path() + """}
"""

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['openstackdocstheme']

# openstackdocstheme options
repository_name = 'openstack/openstackdocstheme'
bug_project = 'openstack-doc-tools'
bug_tag = 'openstackdocstheme'

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# "project" contains the name of the book, such as
# 'security guide' or 'network guide'
# It's used by the "log-a-bug" button on each page
# and should ultimately be set automatically by the build process
project = u'OpenStack Documentation Theme'
copyright = u'2015-2017, OpenStack Contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = version_info.release_string()
# The short X.Y version.
version = version_info.version_string()

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'openstackdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

# To use the API Reference sidebar dropdown menu,
# uncomment the html_theme_options parameter.  The theme
# variable, sidebar_dropdown, should be set to `api_ref`.
# Otherwise, the list of links for the User and Ops docs
# appear in the sidebar dropdown menu.
html_theme_options = {'show_other_versions': True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static/css']


# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    #Default figure align
    'figure_align': 'H',

    # Not to generate blank page after chapter
    'classoptions': ',openany',
    # Additional stuff for the LaTeX preamble.
    'preamble': latex_custom_template,
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'os-doc-demo.tex', u'os-doc-demo Documentation',
   u'OpenStack Contributors', 'manual'),
]
