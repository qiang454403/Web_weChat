# -*- coding: utf-8 -*-# filename: cacheMgr.py
from cache import Cache


class CacheMgr():
	def __init__(self):
		self.dic = Cache()
	def Get(self,typeStr):
		print typeStr
		if typeStr=="@ml":
			str = Cache()
			msg  = str.GetCatalog()
			return msg
		return "error"
	
