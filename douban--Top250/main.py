# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# import urllib.request
# import urllib.error
#
# def AskUrl(url):
#     # 代理,告诉服务器自己的相关信息,方便爬取信息
#     head={}
#     request = urllib.request.Request(url, headers=head)
#     html = ""
#     try:
#         response = urllib.request.urlopen(request)
#         html = response.read().decode("utf-8")
#         print(html)
#     except urllib.error.URLError as e:
#         if hasattr(e, "code"):
#             print(e.code)
#
#
#
#
# def main():
#     AskUrl("https://www.runoob.com/python/python-files-io.html")
#
# if __name__=='__main__':
#     main()
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import re
import urllib.request
import urllib.error
from bs4 import  BeautifulSoup
import xlwt


#得到一个指定的URL的网页的内容,并转化为html源码,原则上就是字符串
def askURL(url):
    # 用户代理
    head = {"User-Agent":"Mozilla"}

    # 对服务器提出请求
    request = urllib.request.Request(url, headers=head)
    html = ""

    try:
        # 根据请求获得响应
        respose = urllib.request.urlopen(request)
        html = respose.read().decode("utf-8")
    except urllib.error.URLError as e:
        if(hasattr(e, "code")):
            print(e.code)
        if(hasattr(e, "reason")):
            print(e.reason)

    return html

movie_link = re.compile(r'<a href="(.*?)">')
movie_name = re.compile(r'<span class="title">(.*)</span>')
movie_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
movie_judge_number = re.compile(r'<span>(\d*)人评价</span>')
movie_inq = re.compile(r'<span class="inq">(.*)</span>')

def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_ = "item"): #查找符合要求的字符串
            data = [] #data用来存储一部电影的所有信息
            item = str(item)

            # 电影链接
            mv_Link = re.findall(movie_link, item)[0]
            data.append(mv_Link)
            # 电影名称
            mv_name = re.findall(movie_name, item)[0]
            data.append(mv_name)
            # 电影评分
            mv_rating = re.findall(movie_rating, item)
            data.append(mv_rating)
            # 电影评分人数
            mv_judge_nr = re.findall(movie_judge_number,item)[0]
            data.append(mv_judge_nr)
            # 电影信息
            mv_inq = re.findall(movie_inq, item)
            if len(mv_inq) != 0:
                data.append(mv_inq[0])
            else: data.append("")
            datalist.append(data)
    #     逐一解析数据(获得html之后)

    print("Data is accessed successfully!")
    return datalist



# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.
# 文档搜索
# (1) find_all方法:返回的是list
# (2)正则表达式
def saveData(savePath, datalist):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("豆瓣电影Top250")
    col = ("电影链接","电影名称", "评分", "评价人数","相关信息")
    for i in range(0, len(col)):
        ws.write(0, i, col[i])

    for i in range(0, len(datalist)):
        item = datalist[i]
        for j in range(0, len(col)):
            ws.write(i + 1, j, item[j])

    wb.save(savePath)
    print("Data is saved successfully!")

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = []
    datalist = getData(baseurl)
    savePath = "data.xls"
    saveData(savePath, datalist)

if __name__ == '__main__':
    main()

