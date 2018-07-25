# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 22:57:24 2018

@author: Cristina
"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes