#coding=gbk
import codecs
f = codecs.open('doc/Item.csv','r','gbk')
s = f.readlines()
f.close()
for line in s:
    print line.encode('gbk')