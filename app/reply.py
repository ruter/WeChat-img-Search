# -*- coding: utf-8 -*-

import time


class Message(object):
    def __init__(self):
        self.__dict = dict()

    def send(self):
        return 'success'


class TextMessage(Message):
    def __init__(self, to_username, from_username, content):
        self.__dict = dict()
        self.__dict['to_username'] = to_username
        self.__dict['from_username'] = from_username
        self.__dict['create_time'] = int(time.time())
        self.__dict['content'] = content

    def send(self):
        xml_form = u"""
        <xml>
          <ToUserName><![CDATA[{to_username}]]></ToUserName>
          <FromUserName><![CDATA[{from_username}]]></FromUserName>
          <CreateTime>{create_time}</CreateTime>
          <MsgType><![CDATA[text]]></MsgType>
          <Content><![CDATA[{content}]]></Content>
        </xml>
        """
        detail = self.__dict
        return xml_form.format(**detail)


class ImageMessage(Message):
    def __init__(self, to_username, from_username, media_id):
        self.__dict = dict()
        self.__dict['to_username'] = to_username
        self.__dict['from_username'] = from_username
        self.__dict['create_time'] = int(time.time())
        self.__dict['media_id'] = media_id

    def send(self):
        xml_form = u"""
        <xml>
          <ToUserName><![CDATA[{to_username}]]></ToUserName>
          <FromUserName><![CDATA[{from_username}]]></FromUserName>
          <CreateTime>{create_time}</CreateTime>
          <MsgType><![CDATA[image]]></MsgType>
          <Image>
            <MediaId><![CDATA[{media_id}]]></MediaId>
          </Image>
        </xml>
        """
        detail = self.__dict
        return xml_form.format(**detail)


class NewsMessage(Message):
    def __init__(self, to_username, from_username, title, description, pic_url, url):
        self.__dict = dict()
        self.__dict['to_username'] = to_username
        self.__dict['from_username'] = from_username
        self.__dict['create_time'] = int(time.time())
        self.__dict['title'] = title
        self.__dict['description'] = description
        self.__dict['pic_url'] = pic_url
        self.__dict['url'] = url

    def send(self):
        xml_form = u"""
        <xml>
          <ToUserName><![CDATA[{to_username}]]></ToUserName>
          <FromUserName><![CDATA[{from_username}]]></FromUserName>
          <CreateTime>{create_time}</CreateTime>
          <MsgType><![CDATA[news]]></MsgType>
          <ArticleCount>1</ArticleCount>
          <Articles>
            <item>
              <Title><![CDATA[{title}]]></Title> 
              <Description><![CDATA[{description}]]></Description>
              <PicUrl><![CDATA[{pic_url}]]></PicUrl>
              <Url><![CDATA[{url}]]></Url>
            </item>
          </Articles>
        </xml>
        """
        detail = self.__dict
        return xml_form.format(**detail)
