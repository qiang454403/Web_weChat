#coding=utf-8
from cache import Cache

class CacheMgr():
	def __init__(self):
		self.dic = Cache()
	def Get(self,typeStr):
		print typeStr
		if typeStr=="@ml":
			str = Cache()
			return str.GetCatalog()
		return "指令无效"
		
