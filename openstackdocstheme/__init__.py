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
import string
import subprocess

_giturl = 'https://git.openstack.org/cgit/{}/tree/doc/source'
_html_context_data = None


def _get_other_versions(app):
    if not app.config.html_theme_options.get('show_other_versions', False):
        return []

    git_cmd = ["git", "tag", "--sort=v:refname", "--merged"]
    try:
        raw_version_list = subprocess.Popen(
            git_cmd, stdout=subprocess.PIPE).communicate()[0]
        raw_version_list = raw_version_list.decode("utf-8")
    except UnicodeDecodeError:
        app.warn('Cannot decode the list based on utf-8 encoding. '
                 'Not setting "other_versions".')
        raw_version_list = u''
    except OSError:
        app.warn('Cannot get tags from git repository, or no merged tags. '
                 'Not setting "other_versions".')
        raw_version_list = u''

    # grab last five that start with a number and reverse the order
    _tags = [t.strip("'") for t in raw_version_list.split('\n')]
    other_versions = [
        t for t in _tags if t and t[0] in string.digits
        # Don't show alpha, beta or release candidate tags
        and 'rc' not in t and 'a' not in t and 'b' not in t
    ][:-5:-1]
    return other_versions


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
        try:
            _html_context_data['gitsha'] = subprocess.check_output(
                ['git', 'rev-parse', 'HEAD'],
            ).decode('utf-8').strip()
        except Exception:
            app.warn('Cannot get gitsha from git repository.')
            _html_context_data['gitsha'] = 'unknown'

        repo_name = app.config.repository_name
        if repo_name:
            _html_context_data['giturl'] = _giturl.format(repo_name)
        bug_project = app.config.bug_project
        if bug_project:
            _html_context_data['bug_project'] = bug_project
        if bug_project and bug_project.isdigit():
            _html_context_data['use_storyboard'] = True
        bug_tag = app.config.bug_tag
        if bug_tag:
            _html_context_data['bug_tag'] = bug_tag

    context.update(_html_context_data)
    context['other_versions'] = _get_other_versions(app)


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
    return {
        'parallel_read_safe': True,
    }
