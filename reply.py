# -*- coding: utf-8 -*-# filename: reply.py
import time
import sys 

class Msg(object):
	def __init__(self):
		pass
	def send(self):
		return "success"
class TextMsg(Msg):
	def __init__(self, toUserName, fromUserName, content):
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['Content'] = content
	def send(self):
		#XmlForm = """
		#<xml>
		#<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		#<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		#<CreateTime>{CreateTime}</CreateTime>
		#<MsgType><![CDATA[text]]></MsgType>
		#<Content><![CDATA[{Content}]]></Content>
		#</xml>
		#"""
		XmlForm = "<xml>"
		XmlForm=XmlForm+"<ToUserName><![CDATA["+self.__dict['ToUserName']+"]]></ToUserName>"
		XmlForm=XmlForm+"<FromUserName><![CDATA["+self.__dict['FromUserName']+"]]></FromUserName>"
		XmlForm=XmlForm+"<CreateTime>"+"111111111"+"</CreateTime>"
		XmlForm=XmlForm+"<MsgType><![CDATA[text]]></MsgType><Content><![CDATA["
		XmlForm = XmlForm+self.__dict['Content']+"]]></Content></xml>"
		return XmlForm#.format(**self.__dict)
class ImageMsg(Msg):
	def __init__(self, toUserName, fromUserName, mediaId):
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['MediaId'] = mediaId
	def send(self):
		XmlForm = """
		<xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		<CreateTime>{CreateTime}</CreateTime>
		<MsgType><![CDATA[image]]></MsgType>
		<Image>
		<MediaId><![CDATA[{MediaId}]]></MediaId>
		</Image>
		</xml>
		"""
		return XmlForm.format(**self.__dict)