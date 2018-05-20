# coding=utf-8
from utils import *
import colorama

colorama.init()

try:
    raise Exception('q')
except Exception:
    pass

print pretty_last_exception()
