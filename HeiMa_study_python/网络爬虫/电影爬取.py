# 爬取豆瓣TOP250(https://movie.douban.com/top250)电影数据，并保存到CSV文件中（数据包括：电影名，年份，上映时间，类型，时长，评分，语言，导演，编剧，主演，简介）
# 步骤：1. 查看：网址/robots.txt文件，看抓取规则 2. 按F12查看页面结构，拆解具体操作步骤：a.获取电影列表；b.遍历列表获取每一部电影详细信息；c.将信息保存到CSV
# 由于豆瓣反爬太强爬取失败，更换为scrape center


import requests
import csv
from lxml import html


# 常量(一般全大写)
BC_URL = "https://ssr1.scrape.center"
# 模拟请求头，让网站返回信息（按F12在网络处获取）模拟真实请求防止某些网站反爬
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0"}
MOVIE_LIST_FILE = "./网络爬虫/CSV_data/电影数据.csv"


# 向电影详细信息页面发送请求，获得详细信息
def get_movie_info(url):
    # 发送请求
    movie_resp = requests.get(url, timeout=60, headers=HEADERS)
    print(f"发送请求{url}，获取电影详情中。。。")
    print(f"状态码：{movie_resp.status_code}；返回文本长度：{len(movie_resp.text)}") # 判断请求状况，如果文本长度为0则为爬取失败
    movie_doc = html.fromstring(movie_resp.text)
    # 解析数据  following-sibling::text()[1]后面第一个文本
    names = movie_doc.xpath("//*[@id='detail']/div[1]/div/div/div[1]/div/div[2]/a/h2/text()")
    dates = movie_doc.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[3]/span/text()')
    tags = movie_doc.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[1]/button/span/text()') # 如果想获得多个相同标签内容，就不用写索引了直接/text()
    cost_times = movie_doc.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[2]/span[3]/text()')
    scores = movie_doc.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[3]/p[1]/text()')
    directors = movie_doc.xpath('//*[@id="detail"]/div[2]/div/div/div/div/div/p/text()')
    discriptions = movie_doc.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[4]/p/text()')
    # print(names, dates, tags, cost_times, scores, directors, discriptions)
    # 定义字典用于储存数据
    movie_info_dic = {
        "电影名": names[0].strip() if names else '',
        "上映时间": dates[0].strip() if dates else '', 
        "类型": ", ".join(t.strip() for t in tags) if tags else '', # "".join()方法是用双引号里面的符号隔开几个字符
        "时长": cost_times[0].strip() if cost_times else '', 
        "评分": scores[0].strip() if scores else '', 
        "导演": directors[0].strip() if directors else '', 
        "简介": discriptions[0].strip() if discriptions else ''
        }
    return movie_info_dic

# 保存数据到CSV文件中
def save_all_movies(infos):
    with open(MOVIE_LIST_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名", "上映时间", "类型", "时长", "评分", "导演", "简介"])
        writer.writeheader()
        writer.writerows(infos)


# 主函数
def main():
    # 1.发送请求，解析数据获取电影列表
    response = requests.get(BC_URL, timeout=60, headers=HEADERS)  # timeout=60指超过60s则请求超时
    print(f"状态码：{response.status_code}；返回文本长度：{len(response.text)}") # 判断请求状况，如果文本长度为0则为爬取失败
    document = html.fromstring(response.text)
    movie_list = document.xpath("//*[@id='index']/div[1]/div[1]/div")

    # 2.遍历列表获取详细信息
        # 定义一个列表用于储存信息
    movie_infos = []
    for movie in movie_list:
        movie_url = movie.xpath("./div/div/div[2]/a/@href") # xpath返回的项目封装成一个列表，拼成一个完整的网址
        # 再向电影详细信息页面发送请求，获得详细信息
        if movie_url:
            movie_info_url = BC_URL + movie_url[0] # movie_url是一个只有一个数据的列表
            movie_infos.append(get_movie_info(movie_info_url))

    # 3. 将数据储存在CSV文件中
    print("以获取所有电影数据，保存数据到CSV文件中。。。")
    save_all_movies(movie_infos)

    # 4.数据处理





# 当该文件直接运行的时候执行主函数，当作为模块导入时不执行主函数
if __name__ == '__main__':
    main()