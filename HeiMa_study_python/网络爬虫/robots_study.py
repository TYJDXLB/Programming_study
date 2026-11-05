# 网络机器人（爬虫）：按照预设规则自动抓取网络数据的程序或脚本
# robots协议:爬虫协议，是指网站根目录下的一份文本文件robots.txt，用于告诉爬虫哪些页面可以抓取，哪些不能。
# 可通过：网址/robots.txt查看
""" robots.txt示例：
(以下为通用规则，针对所有爬虫)
User-agent(用户代理，通过该请求头确认爬虫类型): *  ( * 表示所有爬虫)
Disallow(禁止访问的资源): /admin/
allow(允许访问的资源): /public/
sitemap(站点地图，帮助爬虫获取网站内容): https://www.example.com/sitemap.xml
crawl-delay(爬取时间间隔，控制爬虫访问网站的速度): 10

(以下为针对特定爬虫的规则)
user-agent: Googlebot (谷歌爬虫)
Disallow: / ( / 表示禁止访问所有资源)
"""

# # 数据分析  (从原始HTML文件中提取数据)
# # lxml库：是一个高性能的HTML/XML文档的解析库，支持基于Xpath语法来解析和获取网页数据（使用：地址 -m pip install lxml 安装）
# from lxml import html
# # 打开html文件
# with open("./网络爬虫/testweb.html", "r", encoding="utf-8") as f:
#     html_test = f.read()
#     # 解析html使其转换成一个文档对象，html.fromstring方法可以将html对象转化为代码文本文件
#     document = html.fromstring(html_test)
#     # 通过Xpath进行解析(用列表接收数据).xpath代码没有提示不必在意
#     thead_list = document.xpath("//table/thead/tr/td/text()")
#     print(thead_list)

#     tbody_list = document.xpath("//table/tbody/tr")
#     for tr in tbody_list:
#         t_list = tr.xpath("./td/text()")
#         print(t_list)

"""Xpath语法
/                   从根节点出发选择节点
//                  从任意位置选择节点
.                   从当前节点出发
[n]                 选择第n个元素，索引从1开始
[last()]            选择最后一个元素
[@atter]            选择有该属性的元素
[@atter='value']    选择有该属性的元素
*                   匹配任何元素
@*                  匹配任何元素的任何属性
text()              获取文本内容
"""

# # CSV(Comma-Separated Values，逗号分隔值)文件：是一种简单通用文本文件格式，用于储存表格数据
# # 新建CSV文件时记得保存时编码选系统编码(ANSI)
# # 直接写CSV文件
# with open("./网络爬虫/CSV_data/csv_zhijie.csv", "w", encoding="utf-8") as f:
#     f.write("name,age,gender,hobby\n")
#     f.write('A,14,boy,"JavaScript,football"\n') # 用双引号引起来可以放到一个单元格内
#     f.write("B,15,girl,C++\n")
# # 读取用for循环遍历就行

# # 用CSV标准库进行操作
# import csv
# # newline=""  # 写入csv文件时，windows系统会自动在每行后面加上一个空行，使用newline=""可以避免这个问题
# with open("./网络爬虫/CSV_data/csv_ku.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"]) # csv.DictWriter(文件, fieldnames=["表头"])
#     writer.writeheader() # 写入表头，由于实例化对象的时候已经传入因此现在不用再传入
#     writer.writerow({"姓名": "小王", "年龄": 14, "性别": "男", "爱好": "JavaScript,football"}) # 写入一行数据
#     writer.writerows([
#         {"姓名": "小李", "年龄": 15, "性别": "女", "爱好": "C++"},
#         {"姓名": "小张", "年龄": 16, "性别": "男", "爱好": "Python"}]) # 写入多行数据，用[]括起来
# 读取
# with open("./网络爬虫/CSV_data/csv_ku.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f) # csv.DictReader(文件)
#     for row in reader:
#         print(row) # 读取出来的每一行都是一个字典，key为表头，value为对应的值



# # test1 获取TIOBE网站排行榜单 步骤：1. 查看robots.txt文件，获取爬取规则。2. 安装request第三方库（用pip安装）用于发送请求。3. 编写代码，访问网站，爬取数据
# import requests
# from lxml import html


# # 定义url
# target_url = "https://www.tiobe.com/tiobe-index/"

# # 发送请求，获取数据 (在浏览器地址栏发起的所有请求都是get请求)
# response= requests.get(target_url)

# # 数据解析（只要榜单） response.text将返回的请求转化为text文本
# document = html.fromstring(response.text)
# # 解析表头
# th_list = document.xpath("/html/body/section/div/article/table[1]/thead/tr/th/text()") # 直接在网页中选中该元素右键点复制xpath路径即可
# print(th_list)
# # 解析表格数据
# tb_list = document.xpath("//*[@id='top20']/tbody/tr")
# for tr in tb_list:
#     tr_list = tr.xpath("./td/text()")
#     print(tr_list)


# test2 爬取高分电影榜单(Top100)数据，并保存到CSV文件中