# -*- coding: utf-8 -*-

import hashlib
import requests
import datetime

from . import app
from . import collection


def get_detail(content):
    res = get_resource(content)
    if res:
        keywords = get_keywords(content)
        hash_code = get_hash_code(keywords)
        return {
            'title': u'搜索关于{0}的图片'.format(u'、'.join(keywords)),
            'description': u'点击查看包含关键词「{0}」的图片(｡・`ω´・)'.format(u'、'.join(keywords)),
            'pic_url': res['resVal']['hits'][0]['webformatURL'],
            'url': app.config['SITE_URL'] + hash_code
        }
    else:
        return None


def get_resource(content):
    keywords = get_keywords(content)
    hash_code = get_hash_code(keywords)
    # Find resource in collection
    res = collection.find_one({'resKey': hash_code})
    if not res:
        res = request_resource(keywords, hash_code)
    return res


def request_resource(keywords, hash_code):
    req_url = '{0}?key={1}&q={2}&lang=zh'.format(
        app.config['PIXABAY_URL'],
        app.config['PIXABAY_KEY'],
        '+'.join(keywords)
    )
    response = requests.get(req_url)
    res = response.json()
    if res['totalHits'] > 0:
        res = collection.insert_one({'resKey': hash_code, 'resVal': res, 'createAt': datetime.datetime.utcnow()})
        return res
    else:
        return None


def get_keywords(content):
    keywords = content.strip().lstrip('#').split()
    keywords.sort()
    return keywords


def get_hash_code(keywords):
    sha1 = hashlib.sha1()
    map(sha1.update, keywords)
    hash_code = sha1.hexdigest()
    return hash_code
