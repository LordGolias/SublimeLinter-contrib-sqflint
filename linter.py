#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by LordGolias
# Copyright (c) 2017 LordGolias
#
# License: BSD-3-Clause
#

"""This module exports the Sqflint plugin class."""

from SublimeLinter.lint import PythonLinter


class Sqflint(PythonLinter):
    """Provides an interface to sqflint."""

    defaults = {'selector': 'source.sqf'}
    cmd = 'sqflint@python'
    regex = r'\[(?P<line>\d+),(?P<column>\d+)\]:(?:(?P<error>error)|(?P<warning>warning|info)):(?P<message>.*\r?)'
