#coding=utf-8
import codecs


class Cache():
	def __init__(self):
	
		self.alldata = []
		self.read()
		
	def Get(self,type):
		#print type
		Str = ""
		for item in self.alldata:
			#print item[0]
			if item[0] == type:
				#print item[1]
				Str=Str+item[1]
		print self.alldata[0][1]
	def GetCatalog(self):
		Str = ""
		name = self.alldata[0][1]
		type = self.alldata[0][2]
		for item in self.alldata:
			if item[1]!=name:
				Str=Str+name+":"+item[1]+type+":"+item[2]+"\r\n"
		return self.alldata[1][1]+self.alldata[1][2]
		
	def read(self):
		f = codecs.open('doc/Catalog.csv','r','gbk')
		s = f.readlines()
		f.close()
		for line in s:
			
			lines = line.split(',')
			lines[0] = lines[0].encode('gbk')
			lines[1] = lines[1].encode('gbk')
			lines[2] = lines[2].replace("\r\n","")
			lines[2] = lines[2].encode('gbk')
			self.alldata.append(lines)
		#print self.alldata
		