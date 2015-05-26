import os
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


def extract_class(div, class_str, soup):
	try:
		a  = soup.find_all(div, class_= class_str)
		for item in a:
			item.extract()
	except:
		print "None"



path = "../Baidu/"
count = 0


for f in os.listdir(path):
	count += 1
	if f == ".DS_Store":
		continue

	html = open(path+f,"r").read()
	soup = BeautifulSoup(html)
	write_file = open("./Baidu/"+f,"w")
	# result logo 
	#result_logo = soup.find("a",id="result_logo")
	#result_logo.extract()
	extract_id("a","result_logo",soup)
	# baidu numbers
	extract_class("div","nums",soup)
	# input baidu 
	extract_id("input","su",soup)
	#
	clear_id("div","s_tab",soup)
	extract_id("div","u",soup)
	extract_class("i","c-icon c-icon-bear-circle c-gap-right-small res-queryext-pos",soup)
	# feedback
	extract_class("a","feedback",soup)
	# baidu bear png
	extract_class("i","c-icon c-icon-bear-pn",soup)
	extract_class("i","c-icon c-icon-bear-p",soup)
	#
	extract_class("div","cr-offset",soup)

	write_file.write(str(soup))
