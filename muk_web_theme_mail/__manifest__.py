###################################################################################
#
#    Copyright (c) 2017-2019 MuK IT GmbH.
#
#    This file is part of MuK Backend Theme Mail 
#    (see https://mukit.at).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################
{
    "name": "MuK Backend Theme Mail", 
    "summary": "Backend Theme Mail",
    "version": "12.0.2.0.0",
    'category': 'Extra Tools',
    "license": "LGPL-3",
    "author": "MuK IT",
    "website": "http://www.mukit.at",
    'live_test_url': 'https://mukit.at/r/SgN',
    "contributors": [
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    "depends": [
        "mail",
        "muk_web_theme",
    ],
    "excludes": [
        "web_enterprise",
    ],
    "data": [
        "template/assets.xml",
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png',
    ],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'application': False,
    'installable': True,
    'auto_install': True,
}