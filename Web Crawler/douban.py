#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import urllib
import urllib2
import json
from bs4 import BeautifulSoup


tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie&source=index'
# get request
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = json.loads(response.read())
tags = result['tags']
# movies list store all movies information
movies = []
start = 0;
# process all kind of movies
for tag in tags:
	while 1: 
		# get request to get all movies url
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&page_limit=20&page_start=' + str(start)
		request = urllib2.Request(url=url)
		response = urllib2.urlopen(request, timeout=20)
		result = response.read()
		result = json.loads(result)
		result = result['subjects']
		start += 20
		# loop until there is no movies
		if len(result) == 0:
			break
		# add all movies into list
		for item in result:
			movies.append(item)

# open a file to write in data
fw = open('movies.txt', 'w')
# movies information includes film director, screenwriter and actor
fw.write('Film' + '\t' + 'director' + '\t' + 'screenwriter' + '\t' + 'actor' + '\n')
# search all movies' details
for x in xrange(0,len(movies)):
	# get request to search details information
	url = movies[x]['url']
	request = urllib2.Request(url=url)
	response = urllib2.urlopen(request, timeout=20)
	result = response.read()
	html = BeautifulSoup(result)
	# try to search director, screenwriter and actor
	try:
		value = html.select('#info span.attrs')
	except Exception, e:
		# only write movies name if other information is not accessible
		fw.write(str(movies[x]['title']))
	else:
		movies[x]['director'] = value[0].get_text()
		movies[x]['screenwriter'] = value[1].get_text()
		movies[x]['actor'] = value[2].get_text()
		print str(movies[x]['title'] + '\t' +movies[x]['director'])
		fw.write(str(movies[x]['title'] + '\t' +movies[x]['director'] + '\t' +movies[x]['screenwriter'] + '\t' +movies[x]['actor']+'\n'))
	finally:
		pass
fw.close()