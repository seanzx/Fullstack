import sys
reload(sys)
sys.setdefaultencoding("utf8")

import urllib
import urllib2
import json

tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie&source=index'

request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = json.loads(response.read())
tags = result['tags']
for item in tags:
	print item
