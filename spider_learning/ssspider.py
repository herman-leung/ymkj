

import urllib.request,urllib.error
from bs4 import BeautifulSoup
def main():
    #首先我们需要有一个目标网页地址：这里用豆瓣电影top250榜单
    baseUrl = "http://movie.douban.com/top250?start="
    askUrl(baseUrl)
    #获取数据
    data = getData(baseUrl)

    askUrl("https://movie.douban.com/top250?start=")

    #保存网页数据
    # savePath = "豆瓣top.xls"
    # saveData(savePath)

def getData(baseurl):
    dataList = []

    for i in range(0,1):
        url = baseurl + str(i*25)
        html = askUrl(url)

    # 开始逐一解析 获取到的网页  html
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_ = "item"):  #查找符合的内容
            print(item)




    return dataList

#   得到一个指定url的网页内容
def askUrl(url):
    #head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    request = urllib.request.Request(url = url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e,"reason")
    return html


def saveData(savepath):
    pass

if __name__ == '__main__':
    main()