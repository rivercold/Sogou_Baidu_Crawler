#Sogou_Baidu_Crawler

## Crawl sogou&baidu SERP based on queries and create tasks on CrowdBao

所有的代码的输入都是一个query 文件，包含一系列的query

其中百度的是使用request指令，模拟了浏览器的方式抓取。

文件输出路径：/Baidu/file.html or Sogou/file.html

输出为原始html页面，没有经过任何处理



##Filter Folder 中
baidu_filter.py
sogou_filter.py
都是采用了BeautifulSoup去掉无用标签
返回一个新的网页html文件


## CrowdBao Folder 中
生成id1***html1***id2****html2的文件格式
注意由于众包平台的规模限制问题（最多100个），所以我们这里是count 每100个 生成一个文件。