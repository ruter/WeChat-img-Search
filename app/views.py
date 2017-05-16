# -*- coding: utf-8 -*-

import hashlib
from flask import abort
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template

from . import app, collection
from . import receive


@app.errorhandler(404)
def not_found_error(error):
    return 404


@app.errorhandler(500)
def internal_error(error):
    return 500


@app.route('/', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # Verify
        try:
            signature = request.args['signature']
            timestamp = request.args['timestamp']
            nonce = request.args['nonce']
            echostr = request.args['echostr']

            temp_list = [app.config['TOKEN'], timestamp, nonce]
            temp_list.sort()

            sha1 = hashlib.sha1()
            map(sha1.update, temp_list)
            hash_code = sha1.hexdigest()

            if hash_code == signature:
                return echostr
            else:
                abort(404)
        except Exception as e:
            return e
    else:
        return 'hello, world'
