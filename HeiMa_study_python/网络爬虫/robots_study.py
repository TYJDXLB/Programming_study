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

# # 正则表达式（Regular Expression）是一种由特定语法规则构成的文本模式，用来描述字符串中符合特定规则的字符序列。
# import re


# s1 = "18809091231是我的手机号，另一个手机号为18800001266，QQ号为：17799899你记住了吗？"
# s2 = "我的手机号是18809091231，另一个手机号为18800001266，QQ号为：17799899你记住了吗？"
# # r"1[3-9]\d{9}" 中的r表示使字符串中的符号表示其本身含义不然\会对后面的字符进行转义；1[3-9]\d{9}表示：这串数字要以1开头，第二位数要在3-9之间，后面有9个数字
# result_1 = re.match(r"1[3-9]\d{9}", s1) # match从字符串的开头匹配（返回Match对象）
# # result_1 = re.match(r"1[3-9]\d{9}", s2) # 会报错，因为match只能从开头匹配，开头不对就报错了
# print(result_1.group()) # .group()获取匹配的结果
# print(result_1.span()) # .span()获取匹配的索引
# print(result_1.start()) # .start()获取开始的索引
# print(result_1.end()) # .end()获取结束的索引
# result_2 = re.search(r"1[3-9]\d{9}", s2) # search从任意位置开始，搜索第一个选项（返回Match对象）
# print(result_2.group())
# result_3 = re.findall(r"1[3-9]\d{9}", s1) # findall从任意位置开始，搜索所有匹配的选项（返回list）
# print(result_3)
# re.sub(正则表达式, 替换成什么, 原始文本, count=替换次数(等于零默认全部替换)) 用正则表达式子取代：字符串.replace(旧的, 新的)
"""正则表达式语法:
普通字符    字母，数字，汉字及大部分字符直接匹配
.           匹配任意一个字符(除\n)
\d          匹配数字0-9
\D          匹配非数字
\w          匹配单词字符如：a-z,A-Z,0-9,_,其他语言字符
\W          匹配非单词字符
[aeiou]     匹配其中的任何单个字符
[^aeiou]    求反^,匹配不在其中的任何单个字符
[0-5]       表示范围
*           前面的字符出现任意次(0次或者无数次)
+           前面的字符至少出现1次
?           前面的字符至多出现1次
{m}         前面的字符至出现m次
{m,}        前面的字符至少出现m次
{m,n}       前面的字符出现m-n次
|           或，匹配左右任意一个表达式
()          分组，将括号里的多个字符视为一个单元
^           匹配字符串开头
$           匹配字符串结尾
如果只想匹配a-z,A-Z,0-9,_这些内容，可以在最后加一个, re.ASCII
"""


















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