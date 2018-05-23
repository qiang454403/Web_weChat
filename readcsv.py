#coding=gbk
import codecs
f = codecs.open('doc/Item.csv','r','utf-8')
s = f.readlines()
f.close()
for line in s:
    print line.encode('gbk')