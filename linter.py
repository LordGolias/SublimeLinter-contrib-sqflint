#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jorge Cardoso Leitão
# Copyright (c) 2017 Jorge Cardoso Leitão
#
# License: MIT
#

"""This module exports the Sqflint plugin class."""

from SublimeLinter.lint import PythonLinter, util


class Sqflint(PythonLinter):
    """Provides an interface to sqflint."""

    syntax = 'sqf'
    cmd = 'sqflint@python3'
    regex = '\[(?P<line>\d+),(?P<column>\d+)\]:(?:(?P<error>error)|(?P<warning>warning|info)):(?P<message>.*\r?)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
    module = 'sqflint'
    check_version = False
