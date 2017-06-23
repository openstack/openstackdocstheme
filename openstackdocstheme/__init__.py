# Copyright 2015 Rackspace US, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import subprocess

_giturl = 'https://git.openstack.org/cgit/{}/tree/doc/source'
_html_context_data = None


def builder_inited(app):
    theme_dir = os.path.join(os.path.dirname(__file__), 'theme')
    app.info('Using openstackdocstheme Sphinx theme from %s' % theme_dir)


def get_pkg_path():
    return os.path.abspath(os.path.dirname(__file__))


def get_html_theme_path():
    """Return the directory containing HTML theme for local builds."""
    return os.path.join(get_pkg_path(), 'theme')


def get_pdf_theme_path():
    """Return the directory containing PDF theme for local builds."""
    args = ['theme', 'openstackdocs_pdf', 'pdftheme']
    return os.path.join(get_pkg_path(), *args)


def get_openstack_logo_path():
    """Return the directory containing openstack logo for local builds."""
    args = ['theme', 'openstackdocs_pdf', 'openstack-logo-full.png']
    return os.path.join(get_pkg_path(), *args)


def _html_page_context(app, pagename, templatename, context, doctree):
    global _html_context_data
    if _html_context_data is None:
        _html_context_data = {}
        _html_context_data['gitsha'] = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'],
        ).decode('utf-8').strip()
        repo_name = app.config.repository_name
        if repo_name:
            _html_context_data['giturl'] = _giturl.format(repo_name)
        bug_project = app.config.bug_project
        if bug_project:
            _html_context_data['bug_project'] = bug_project
        bug_tag = app.config.bug_tag
        if bug_tag:
            _html_context_data['bug_tag'] = bug_tag
    context.update(_html_context_data)


def setup(app):
    app.info('connecting events for openstackdocstheme')
    app.connect('builder-inited', builder_inited)
    app.connect('html-page-context', _html_page_context)
    app.add_config_value('repository_name', '', 'env')
    app.add_config_value('bug_project', '', 'env')
    app.add_config_value('bug_tag', '', 'env')
    app.add_html_theme(
        'openstackdocs',
        os.path.abspath(os.path.dirname(__file__)) + '/theme/openstackdocs',
    )
