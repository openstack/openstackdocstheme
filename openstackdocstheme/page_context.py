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

import datetime
import os
import os.path
import subprocess
import time

import sphinx
from sphinx.util import logging

from . import version

LOG = logging.getLogger(__name__)

_timeint = int(os.environ.get('SOURCE_DATE_EPOCH', time.time()))
_default_last_updated = datetime.datetime.utcfromtimestamp(_timeint)


def _get_last_updated_file(src_file):
    if not os.path.exists(src_file):
        return None
    try:
        last_updated_t = (
            subprocess.check_output(
                [
                    'git',
                    'log',
                    '-n1',
                    '--format=%ad',
                    '--date=format:%Y-%m-%d %H:%M:%S',
                    '--',
                    src_file,
                ]
            )
            .decode('utf-8')
            .strip()
        )
    # NOTE: we catch any exception here (instead of
    # subprocess.CalledProcessError and OSError) because some projects (eg.
    # neutron) do import eventlet in docs/source/conf.py which will patch
    # the subprocess module and with that, the exception is not catched
    except Exception as err:
        LOG.info(
            '[openstackdocstheme] Could not get modification time of %s: %s',
            src_file,
            err,
        )
    else:
        if last_updated_t:
            try:
                return datetime.datetime.strptime(
                    last_updated_t, '%Y-%m-%d %H:%M:%S'
                )
            except ValueError:
                LOG.info(
                    '[openstackdocstheme] '
                    'Could not parse modification time of %s: %r',
                    src_file,
                    last_updated_t,
                )
    return None


def _get_last_updated(app, pagename):
    last_updated = None
    full_src_file = app.builder.env.doc2path(pagename)

    candidates = []

    # Strip the prefix from the filename so the git command recognizes
    # the file as part of the current repository.
    if sphinx.version_info >= (7, 0):
        src_file = str(full_src_file.relative_to(app.builder.env.srcdir))
    else:  # Sphinx < 7.0
        src_file = full_src_file[len(str(app.builder.env.srcdir)) :].lstrip(
            '/'
        )
    candidates.append(src_file)

    if not os.path.exists(src_file):
        # Some of the files are in doc/source and some are not. Some
        # of the ones that are not are symlinked. If we can't find the
        # file after stripping the full prefix, try looking for it in
        # doc/source explicitly.
        candidates.append(os.path.join('doc/source', src_file))

    for filename in candidates:
        last_updated = _get_last_updated_file(filename)
        if last_updated:
            LOG.debug(
                '[openstackdocstheme] Last updated for %s is %s',
                pagename,
                last_updated,
            )
            return last_updated

    if pagename not in ('genindex', 'search'):
        LOG.info(
            '[openstackdocstheme] could not determine last_updated for %r',
            pagename,
        )

    return _default_last_updated


def html_page_context(app, pagename, templatename, context, doctree):
    # Use the last modified date from git instead of applying a single
    # value to the entire site.
    context['last_updated'] = _get_last_updated(app, pagename)


def setup(app):
    LOG.info('[openstackdocstheme] connecting html-page-context event handler')
    app.connect('html-page-context', html_page_context)
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        'version': version.version_info.version_string(),
    }
