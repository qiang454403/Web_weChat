#coding=utf-8
from cacheMgr import CacheMgr

#dic = Cache()
#str = dic.GetCatalog()
#con = dic.GetCatalog()
textmgr = CacheMgr()
content =textmgr.Get("@ml")
print content