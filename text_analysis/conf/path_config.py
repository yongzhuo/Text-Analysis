# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2019/11/18 23:59
# @author  : Mo
# @function: path of text-analysis


import sys
import os
path_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path_root)

# path of basic
path_log_dir = os.path.join(path_root, "logs")

ta = 0

