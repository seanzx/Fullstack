import sys
reload(sys)
sys.setdefaultencoding("utf8")

import urllib
import urllib2
import json
# from bs4 import BeautifulSoup


# get
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'

request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()
print result

'''
# post
url = 'http://shuju.wdzj.com/plat-info-target.html'
data = urllib.urlencode({'type':1, 'target1':2, 'target2':0, 'wdzjPlatId':59})
request = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(request, data)
result = response.read();
print result
for key, value in json.loads(result).items():
	print key, value
'''