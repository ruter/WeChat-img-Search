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
                    to_username = recv_msg.from_username
                    from_username = recv_msg.to_username
                    content = recv_msg.content.strip()
                    if content.find('#') == 0:
                        detail = handler.get_detail(content)
                        reply_msg = reply.NewsMessage(to_username, from_username, detail['title'],
                                                      detail['description'], detail['pic_url'], detail['url'])
                        return reply_msg.send()
                    elif content in app.config['MENU_KEYS']:
                        help_msg = u'使用图片搜索服务，只需要发送「# + 关键词」就可以GET到图片啦(ゝ∀･)b\n\n支持多个关键词搜索，只需要用空格分隔即可，如:\n\n#美食 水果'
                        reply_msg = reply.TextMessage(to_username, from_username, help_msg)
                        return reply_msg.send()
                    else:
                        menu_msg = u'回复以下任一关键词可以获得帮助信息哦(〃∀〃)\n\n「菜单」「帮助」「说明」「使用」「menu」「help」'
                        reply_msg = reply.TextMessage(to_username, from_username, menu_msg)
                        return reply_msg.send()

                if recv_msg.msg_type == 'image':
                    pass
                else:
                    return reply.Message().send()
        except Exception as e:
            return e


@app.route('/images/<res_key>', methods=['GET'])
def images(res_key):
    res = collection.find_one({'resKey': res_key})
    if res:
        return render_template('index.html', res=res['resVal']['hits'])
    else:
        return render_template('empty.html')
