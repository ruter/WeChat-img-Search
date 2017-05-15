# -*- coding: utf-8 -*-

import sys

import pymongo
from flask import Flask


# Fix messy code
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

client = pymongo.MongoClient(app.config['DB_URI'])
db = client[app.config['DB_NAME']]
collection = db[app.config['DB_COLLECTION']]


from app import views
