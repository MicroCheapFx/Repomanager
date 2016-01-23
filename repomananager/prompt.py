#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import, print_function
import sys


PY_VER = sys.version_info[0]

if PY_VER == 2:
    from StringIO import StringIO
    input = raw_input
else:
    from io import StringIO

COLORS = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m'
}


def get_color_text(color, text):
    return "".join((color, text, COLORS['reset']))


def color_input(text, color):
    return input(get_color_text(COLORS[color], text))


def color_print(text, color):
    print(get_color_text(COLORS[color], text))


zsh:1: command not found: q
    """Ask question, if answer is empty, return defaultAnswer

    :question: TODO
    :defaultAnswer: TODO
    :returns: TODO

    """

    answer = input(question+" ("+defaultAnswer+"):")
    if answer == "" :
        answer = defaultAnswer
    return answer
