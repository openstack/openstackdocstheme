# -*- coding: utf-8 -*-
# Copyright (C) 2020 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# openstackdocstheme documentation build configuration file

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['openstackdocstheme']

# openstackdocstheme options
openstackdocs_repo_name = 'openstack/openstackdocstheme'
openstackdocs_bug_project = 'openstack-doc-tools'
openstackdocs_bug_tag = 'openstackdocstheme'
openstackdocs_pdf_link = True

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'2015-2018, OpenStack Contributors'

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
html_theme_options = {
    'show_other_versions': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static/css']


# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'doc-openstackdocstheme.tex',
   u'OpenStack Docs Theme Documentation',
   u'OpenStack Contributors', 'manual'),
]
