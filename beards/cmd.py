# coding=utf-8
from utils import *
import colorama

colorama.init()
#
# try:
#     raise Exception('q')
# except Exception:
#
#     print pretty_last_exception()


from werkzeug import script


# actions go here
def action_foo(name=""):
    """action foo does foo"""
    pass


def action_bar(id=0, title="default title"):
    """action bar does bar"""
    pass


if __name__ == '__main__':
    script.run()
