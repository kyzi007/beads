# -*- coding:utf-8 -*-
import json

import yaml
from tabulate import tabulate
import traceback
import pprint
import sys

from pygments import highlight, lexers, formatters
from colorama import Back, Fore, Style


def pretty_table(data, headers=None):
    if isinstance(data, dict):
        data = data.values()
    return highlight(tabulate(data, tablefmt='pipe', headers=headers), lexers.CssLexer(), formatters.TerminalFormatter())


def pretty_yaml(data):
    if not isinstance(data, basestring):
        data = yaml.dump(data)
    return highlight(data, lexers.YamlLexer(), formatters.TerminalFormatter())


def pretty_json(data):
    if not isinstance(data, basestring):
        data = json.dumps(data, indent=1)
    return highlight(data, lexers.JsonLexer(), formatters.TerminalFormatter())


def pretty_obj(data):
    data = pprint.pformat(data, 1)
    return highlight(data, lexers.PythonLexer(), formatters.TerminalFormatter())


def pretty_last_exception():
    data = traceback.format_exc().replace('\\n', '\n').replace("\\'", '"').replace("'", '')
    return highlight(data, lexers.XtlangLexer(), formatters.TerminalFormatter())


def find_lexers(data):
    for l in lexers._iter_lexerclasses():
        print l
        print highlight(data, l(), formatters.TerminalFormatter())
