# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2012, Wolf Vollprecht <w.vollprecht@gmail.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE
import sys
import optparse

import locale
import os
from locale import gettext as _
locale.textdomain('uberwriter')

from gi.repository import Gtk # pylint: disable=E0611

from . import UberwriterWindow
from uberwriter_lib import AppWindow

from uberwriter_lib import set_up_logging, get_version

def parse_options():
    """Support for command line options"""
    parser = optparse.OptionParser(version="%%prog %s" % get_version())
    parser.add_option(
        "-v", "--verbose", action="count", dest="verbose",
        help=_("Show debug messages (-vv debugs uberwriter_lib also)"))
    parser.add_option(
        "-e", "--experimental-features", help="Use experimental features",
        action='store_true'
        )
    (options, args) = parser.parse_args()

    set_up_logging(options)

    # print args

    return options, args

def main():
    'constructor for your class instances'
    (options, args) = parse_options()
    
    # TODO: all the parsing is unused. 
    # We want to allow multiple windows

    # Run the application.
    app = AppWindow.Application()
    
    if args:
        for arg in args:
            pass 
    else:
        pass
    if options.experimental_features:
        window.use_experimental_features(True)
        
    app.run(sys.argv)
    
