# -*- coding: utf-8 -*-

import hashlib
from flask import abort
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template

import receive
import reply
import handler
from . import app, collection


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
        try:
            new_data = request.data
            recv_msg = receive.parse_xml(new_data)
            if isinstance(recv_msg, receive.Message):

                if recv_msg.msg_type == 'text':
                    content = recv_msg.content
                    if content.strip().find('#') == 0:
                        to_username = recv_msg.from_username
                        from_username = recv_msg.to_username
                        detail = handler.get_detail(content)
                        if detail:
                            reply_msg = reply.NewsMessage(to_username, from_username, **detail)
                            return reply_msg.send()
                        else:
                            no_images_msg = u'ヾ(°д°)ノ゛系统表示找不到匹配关键词的图片，换个姿势再来一次吧！'
                            reply_msg = reply.TextMessage(to_username, from_username, no_images_msg)
                            return reply_msg.send()
                    else:
                        return reply.Message().send()

                if recv_msg.msg_type == 'image':
                    pass
                else:
                    return reply.Message().send()
        except Exception as e:
            return e
