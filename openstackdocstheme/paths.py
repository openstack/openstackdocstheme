# Copyright 2018 Red Hat, Inc.
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

import os.path


def get_pkg_path():
    return os.path.abspath(os.path.dirname(__file__))


def get_html_theme_path():
    """Return the directory containing HTML theme for local builds."""
    return os.path.join(get_pkg_path(), 'theme')


def get_pdf_theme_path(theme='openstackdocs'):
    """Return the directory containing PDF theme for local builds."""
    args = ['theme', theme + '_pdf', 'pdftheme']
    return os.path.join(get_pkg_path(), *args)


def get_theme_logo_path(theme='openstackdocs'):
    """Return the directory containing theme logo for local builds."""
    args = ['theme', theme + '_pdf', 'logo-full.png']
    return os.path.join(get_pkg_path(), *args)


# This function is for compatibility with previous releases.
def get_openstack_logo_path():
    """Return the directory containing OpenStack logo for local builds."""
    return get_theme_logo_path('openstackdocs')
