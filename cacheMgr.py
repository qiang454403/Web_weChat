# -*- coding: utf-8 -*-# filename: cacheMgr.py
from cache import Cache
import sys\


class CacheMgr():
	def __init__(self):
		self.dic = Cache()
	def Get(self,typeStr):
		print typeStr
		if typeStr=="@ml":
			str = Cache()
			msg  = str.GetCatalog()
			print (msg.decode('utf-8').encode(sys.getfilesystemencoding()))
			return msg
		return "error"
	
