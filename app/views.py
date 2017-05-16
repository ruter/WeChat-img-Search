# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for

from . import app, collection


@app.errorhandler(404)
def not_found_error(error):
    return 404


@app.errorhandler(500)
def internal_error(error):
    return 500


@app.route('/')
def index():
    return 'hello, world'
