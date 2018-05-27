# -*- coding: utf-8 -*-# filename: handle.py
import hashlib
import reply
import receive
import web
from cacheMgr import CacheMgr

class Handle(object):
	def POST(self):
		try:
			webData = web.data()
			print "Handle Post webdata is ",webData
   #后台打日志
			recMsg = receive.parse_xml(webData)
			if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
				print "发送的消息是：",recMsg.Content
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				textmgr = CacheMgr()
				content =textmgr.Get(recMsg.Content)
				print content
				replyMsg = reply.TextMsg(toUser, fromUser, content)
				return replyMsg.send()
			else:
				print "暂且不处理"
				return "success"
		except Exception,Argment:
				return Argment