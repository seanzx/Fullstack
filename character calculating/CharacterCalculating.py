# coding:utf8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

fr = open('Harry Potter and The Chamber of Secrets.txt', 'r')
character = []
stat = {}
for line in fr:
	line = line.strip()

	if len(line) == 0:
		continue
	
	for x in xrange(0,len(line)):
		if not (line[x] <= 'z' and line[x] >= 'a' or line[x] <='Z' and line[x] >= 'A'):
	 		continue
	 	if not line[x] in character:
	 		character.append(line[x])

	 	if not stat.has_key(line[x]):
	 		stat[line[x]] = 0
	 	stat[line[x]] += 1

fw = open('result.json', 'w')
fw.write(json.dumps(stat))
fw.close()

stat = sorted(stat.iteritems(), key = lambda d:d[1], reverse=True)
print '*'*20
for x in xrange(0,52):
	print stat[x][0], stat[x][1]
fw = open('result.csv', 'w')
for item in stat:
	fw.write(item[0] + ',' + str(item[1]) + '\n')
fw.close()
fr.close()
