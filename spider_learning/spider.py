from bs4 import BeautifulSoup #网页解析， 获取数据
import re   #正则表达式进行文字匹配
import urllib.request,urllib.error  #制定url，获取网页数据
import xlwt #进行excel操作
import sqlite3


def main():
    #爬取网页
    baseurl = 'https://movie.douban.com/top250?start='
    dataList = getData(baseurl)
    #保存数据
    savePath="豆瓣电影top250.xls"
    saveData(dataList,savePath)



    # askURL("https://movie.douban.com/top250?start=")


# 以这个表达式为例：a. * b，它将会匹配最长的以a开始，以b结束的字符串。如果用它来搜索aabab的话，它会匹配整个字符串aabab。这被称为贪婪匹配。
findLink  = re.compile(r'<a href="(.*?)">')  #compile创建正则表达式对象，表示规则（字符串的模式）
# 影片图片的地址
findImgSrc  = re.compile(r'<img .*src="(.*?)"',re.S)  # re.S 忽略换行符 让换行符包含在字符中
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findJudje = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页
def getData(baseurl):
    dataList=[]

    for i in range(0,10):       #调用获取页面信息的函数
        url = baseurl + str(i*25)
        html = askURL(url)      #保存获取到的网页源码

         #2. 逐一解析数据
        soup = BeautifulSoup(html,"html.parser")  #解析，形成属性文档的对象
        # for i in soup.select(".item"):
        #     print(i)

        for item in soup.find_all('div',class_='item'):  #查找符合要求的字符串，形成列表
            # print(item)  #测试查看电音的item全部信息
            data = [] #保存一部电影的全部信息
            item = str(item)

            # link:影片详情的链接
            link = re.findall(findLink,item)[0]  #re库用来查找，通过正则表达式查找指定得字符串
            data.append(link) #添加链接


            imgSrc = re.findall(findImgSrc,item)[0] #
            data.append(imgSrc)  # 添加图片


            titles = re.findall(findTitle,item)      #片名可能只有一个中文名，没有外文名
            if(len(titles) == 2):
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/","")   # 去掉无关的符号
                data.append(otitle) # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')   #外国名字 可能为空  需要留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)                          #添加评分

            judgeNum = re.findall(findJudje,item)[0]
            data.append(judgeNum)                       # 添加评价人数

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")  #去掉句号
                data.append(inq)                        # 添加概述
            else:
                data.append(" ")


            bd = re.findall(findBd, item)
            if len(bd) != 0:
                bd = bd[0]
                bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) # 去掉br
                bd = re.sub('/'," ",bd) #替换杠号/
                data.append(bd.strip()) #去掉前后空格后加入列表
            else:
                data.append(" ")

            dataList.append(data)  #把处理好的一部电影信息放入dataList
    return dataList


#得到指定url的网页内容
def askURL(url):
    #用户代理：表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件内容）
    #头部head  默契浏览器头部信息，向豆瓣服务器发送消息
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    request = urllib.request.Request(url=url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        # hasattr(e,'code') 判断e这个对象是否包含code这个属性
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

def saveData(dataList,savePath):
    book = xlwt.Workbook(encoding = "utf-8",style_compression=0) #style_compression 样式压缩效果
    sheet = book.add_sheet("豆瓣电影榜单Top250",cell_overwrite_ok=True)  #cell_overwrite_ok 是否覆盖
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")          #列
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("正在写入。。。第%d条"% (i+1))

        data = dataList[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])   # 写入数据



    book.save(savePath)  #保存文档

if __name__ == '__main__':
    main()
    print("爬取完毕！")