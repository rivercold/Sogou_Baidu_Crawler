#Sogou_Baidu_Crawler

## Crawl sogou&baidu SERP based on queries and create tasks on CrowdBao

所有的代码的输入都是一个query 文件，包含一系列的query

其中百度的是使用request指令，模拟了浏览器的方式抓取。

文件输出路径：/Baidu/file.html or Sogou/file.html

输出为原始html页面，没有经过任何处理