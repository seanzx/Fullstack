# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host = '127.0.0.1', user = 'root', passwd = '', db = 'douban', port = 3306, charset = 'utf8')
db.autocommit(True)
cursor = db.cursor()
fw = open('douban_movie_clean.txt', 'r')

count = 0
# insert
for line in fw:
	count += 1
	print count
	if count == 1:
		continue
	print line
	line = line.strip().split('^')
	cursor.execute("insert into movie(title, url, rate, length, description) values(%s, %s, %s, %s, %s)", [line[1], line[2], line[4], line[-3], line[-1]])

# # select
# cursor.execute("select title, rate from movie where rate > 8")
# movies = cursor.fetchall()

# # delete
# cursor.execute("delete from movie where title = 'zxsean'")

fw.close()
cursor.close()
db.close()