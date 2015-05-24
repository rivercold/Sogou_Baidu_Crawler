import os
#coding=utf8

from bs4 import BeautifulSoup
import re

def extract_id(div, id_str, soup):
	try:
		a  = soup.find(div, id= id_str)
		a.extract()
	except:
		print "None"

def clear_id(div, id_str, soup):
	try:
		a  = soup.find(div, id= id_str)
		a.clear()
	except:
		print "None"

def clear_class(div, class_str, soup):
	try:
		a  = soup.find(div, class_= class_str)
		a.clear()
	except:
		print "None"
def extract_class(div, class_str, soup):
	try:
		a  = soup.find_all(div, class_= class_str)
		for item in a:
			item.extract()
	except:
		print "None"



path = "../Sogou/"
count = 0


for f in os.listdir(path):
	count += 1
	if count>330:
		break
	html = open(path+f,"r").read()
	soup = BeautifulSoup(html)
	write_file = open("./Sogou_filter/"+f,"w")
	
	extract_class("h2","tgad-title",soup)
	clear_class("ul","searchnav",soup)
	extract_class("a","logo",soup)
	extract_class("input","sbtn1",soup)
	extract_id("div","s_footer",soup)
	extract_id("div","right",soup)
	write_file.write(str(soup))
