# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 19:00:59 2018

@author: Cristina
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a-prova-di-furto"