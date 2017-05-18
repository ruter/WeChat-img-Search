# -*- coding: utf-8 -*-

import time


class Message(object):
    def __init__(self):
        pass

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
        xml_form = """
        <xml>
          <ToUserName><![CDATA[{to_username}]]></ToUserName>
          <FromUserName><![CDATA[{from_username}]]></FromUserName>
          <CreateTime>{create_time}</CreateTime>
          <MsgType><![CDATA[text]]></MsgType>
          <Content><![CDATA[{content}]]></Content>
        </xml>
        """
        return xml_form.format(**self.__dict)


class ImageMessage(Message):
    def __init__(self, to_username, from_username, media_id):
        self.__dict = dict()
        self.__dict['to_username'] = to_username
        self.__dict['from_username'] = from_username
        self.__dict['create_time'] = int(time.time())
        self.__dict['media_id'] = media_id

    def send(self):
        xml_form = """
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
        return xml_form.format(**self.__dict)


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
        xml_form = """
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
        return xml_form.format(**self.__dict)
