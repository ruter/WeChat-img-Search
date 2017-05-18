# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET


def parse_xml(data):
    if len(data) == 0:
        return None
    xml_data = ET.fromstring(data)
    msg_type = xml_data.find('MsgType').text
    if msg_type == 'text':
        return TextMessage(data)
    elif msg_type == 'image':
        return ImageMessage(data)


class Message(object):
    def __init__(self, xml_data):
        self.to_username = xml_data.find('ToUserName').text
        self.from_username = xml_data.find('FromUserName').text
        self.create_time = xml_data.find('CreateTime').text
        self.msg_type = xml_data.find('MsgType').text
        self.msg_id = xml_data.find('MsgId').text


class TextMessage(Message):
    def __init__(self, xml_data):
        Message.__init__(self, xml_data)
        self.content = xml_data.find('Content').text.encode('utf-8')


class ImageMessage(Message):
    def __init__(self, xml_data):
        Message.__init__(self, xml_data)
        self.pic_url = xml_data.find('PicUrl').text
        self.media_id = xml_data.find('MediaId').text