import urllib2
import time
import random

#coding=utf8
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}

'''def extractSogou(query):
    url = 'http://www.sogou.com/web?ie=utf8&query='
    url += urllib2.quote(query)
    response = urllib2.urlopen(url,timeout=30)
    lines = response.read()
    query_path = "./Sogou/"+query+".html"
    write_file = open(query_path,'w')
    write_file.write(lines)'''


def extractSogou(query):
	url = 'http://www.sogou.com/web?ie=utf8&query='
	url += urllib2.quote(query)
	#url += "&ie=utf-8"
	req_timeout = 5
	req = urllib2.Request(url,None,header)
	resp = urllib2.urlopen(req,None,req_timeout)
	html = resp.read()
	#print html
	query_path = "./Sogou/"+query+".html"
	write_file = open(query_path,'w')
	write_file.write(html)


error_log = open('error_sogou.txt','w')
query_file = open("additional_query_file.txt","r")
queries = query_file.readlines()
count = 0
for query in queries:
	query = query.replace("\n","")
	try:
		extractSogou(query)
		random_time_s = random.randint(5,10)
		time.sleep(random_time_s)
		print query
		count +=1
		if count%10==9:
			count = 0
			random_time = random.randint(240,360)
			time.sleep(random_time)
			prnt("wait for "+str(random_time))
	except:
		error_log.write(query+" sogou\n")