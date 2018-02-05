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

try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import os
import subprocess

import dulwich.repo
from sphinx.ext import extlinks
from sphinx.util import logging

_giturl = 'https://git.openstack.org/cgit/{}/tree/{}'
_html_context_data = None
logger = logging.getLogger(__name__)


def _get_other_versions(app):
    if not app.config.html_theme_options.get('show_other_versions', False):
        return []

    all_series = []
    try:
        repo = dulwich.repo.Repo.discover()
    except dulwich.repo.NotGitRepository:
        return []

    refs = repo.get_refs()
    for ref in refs.keys():
        ref = ref.decode('utf-8')
        if ref.startswith('refs/remotes/origin/stable'):
            series = ref.rpartition('/')[-1]
            all_series.append(series)
        elif ref.startswith('refs/tags/') and ref.endswith('-eol'):
            series = ref.rpartition('/')[-1][:-4]
            all_series.append(series)
    all_series.sort()

    # NOTE(dhellmann): Given when this feature was implemented, we
    # assume that the earliest version we can link to is for
    # mitaka. Projects that have older docs online can set the option
    # to indicate another start point. Projects that come later should
    # automatically include everything they actually have available
    # because the start point is not present in the list.
    earliest_desired = app.config.html_theme_options.get(
        'earliest_published_series', 'mitaka')
    if earliest_desired and earliest_desired in all_series:
        interesting_series = all_series[all_series.index(earliest_desired):]
    else:
        interesting_series = all_series

    # Reverse the list because we want the most recent to appear at
    # the top of the dropdown. The "latest" release is added to the
    # front of the list by the theme so we do not need to add it
    # here.
    interesting_series.reverse()
    return interesting_series


def _get_doc_path(app):
    # Handle 'doc/{docType}/source' paths
    doc_parts = os.path.abspath(app.srcdir).split(os.sep)[-3:]
    if doc_parts[0] == 'doc' and doc_parts[2] == 'source':
        return '/'.join(doc_parts)

    # Handle '{docType}/source' paths
    doc_parts = os.path.abspath(app.srcdir).split(os.sep)[-2:]
    if doc_parts[1] == 'source':
        return '/'.join(doc_parts)

    logger.info('Cannot identify project\'s root directory.')
    return


def builder_inited(app):
    theme_dir = os.path.join(os.path.dirname(__file__), 'theme')
    logger.info('Using openstackdocstheme Sphinx theme from %s' % theme_dir)
    setup_link_roles(app)


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
            logger.warning('Cannot get gitsha from git repository.')
            _html_context_data['gitsha'] = 'unknown'

        doc_path = _get_doc_path(app)
        repo_name = app.config.repository_name
        if repo_name and doc_path:
            _html_context_data['giturl'] = _giturl.format(repo_name, doc_path)
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


_SERIES = None


def get_series_name():
    "Return string name of release series, or 'latest'"
    global _SERIES
    if _SERIES is None:
        parser = configparser.ConfigParser()
        parser.read('.gitreview')
        try:
            branch = parser.get('gerrit', 'defaultbranch')
        except configparser.Error:
            _SERIES = 'latest'
        else:
            _SERIES = branch.rpartition('/')[-1]
    return _SERIES


def setup_link_roles(app):
    series = get_series_name()
    for project_name in app.config.openstack_projects:
        url = 'https://docs.openstack.org/{}/{}/%s'.format(
            project_name, series)
        role_name = '{}-doc'.format(project_name)
        logger.info('adding role %s to link to %s', role_name, url)
        app.add_role(role_name, extlinks.make_link_role(url, project_name))


def setup(app):
    logger.info('connecting events for openstackdocstheme')
    app.connect('builder-inited', builder_inited)
    app.connect('html-page-context', _html_page_context)
    app.add_config_value('repository_name', '', 'env')
    app.add_config_value('bug_project', '', 'env')
    app.add_config_value('bug_tag', '', 'env')
    app.add_config_value('openstack_projects', [], 'env')
    app.add_html_theme(
        'openstackdocs',
        os.path.abspath(os.path.dirname(__file__)) + '/theme/openstackdocs',
    )
    return {
        'parallel_read_safe': True,
    }
