#coding=utf-8
import codecs


class Cache():
	def __init__(self):
	
		self.alldata = []
		self.read()
		
	def Get(self,type):
		#print type
		for item in self.alldata:
			#print item[0]
			if item[0] == type:
				print item[2]
	def GetCatalog():
		return self.alldata
		
	def read(self):
		f = codecs.open('doc/Catalog.csv','r','gbk')
		s = f.readlines()
		f.close()
		for line in s:
			
			lines = line.encode('gbk').split(',')
			lines[2] = lines[2].replace("\r\n","")
			self.alldata.append(lines)
			
		