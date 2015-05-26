import re
import random
import os
#coding=utf-8
baidu_path = "./Baidu/"
sogou_path = "./Sogou/"

for i in range(4,11):

	normal = open("normal-sample"+str(i)+".txt","w")
	query_file = open("query_id"+str(i)+".txt","w")
	count = 0
	for p_file in os.listdir(baidu_path):
		if p_file==".DS_Store":
			continue
			
		baidu_file = baidu_path + p_file
		sogou_file = sogou_path + p_file
		#try:
		baidu_lines = open(baidu_file,"r").read()
		sogou_lines = open(sogou_file,"r").read()
		#print baidu_lines
		count += 1
		if count <=(i-4)*100:
		    continue
		elif count > (i-3)*100:
			break
		else:
			baidu = baidu_lines.rstrip().lstrip().replace("\n","").replace("\r","").replace("***","")
			baidu_id = "b"+str(count)
			sogou = sogou_lines.rstrip().lstrip().replace("\n","").replace("\r","").replace("***","")
			sogou_id = "s"+str(count)
			ran = random.randint(1,4)
			if ran%2==0:
				string = baidu_id + "***"+ baidu+ "***"+ sogou_id + "***" + sogou+"\n"
				query_file.write(p_file + "\t" + str(count) + "\tbaidu_sogou"+"\n")
			else:
				string = sogou_id + "***"+ sogou+ "***"+ baidu_id + "***" + baidu+"\n"
				query_file.write(p_file + "\t" + str(count) + "\tsogou_baidu"+"\n")
			#print string
			normal.write(string)
			print count
		#except:
		#	print(p_file)

#re_script = re.compile(r'(?<=<script).*?(?=</script>)')


#b =  sogou_lines.replace("\n","")
#str1 = a + "***" + b

#normal = open("normal-sample.txt","w")
#normal.write(str1+"\n")

