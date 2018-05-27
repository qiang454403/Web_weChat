#coding=utf-8
from cache import Cache
class CacheMgr():
	def __init__(self):
		self.dic = Cache()
	def Get(typeStr):
		print typeStr
		if typeStr=="@目录":
			logdata =  self.dic.GetCatalog()
			str = ""
			for iter in logdata:
				str = +"名称:"+iter[1]+"编号:"+iter[2]+"\r\n"
			return str
		return "指令无效"
		
