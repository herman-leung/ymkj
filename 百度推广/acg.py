# -*- coding: utf-8 -*-
# Author : YRH
# Data : 2020年12月1日
# Project : 爱采购商品价格
# Tool : PyCharm


# import subprocess
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import re
import json
import time
# subprocess.Popen([CLIENT_LOCATION])


class b2b(object):
    def __init__(self, name, max_page):
        self.name = name  # 搜索关键词
        self.url = "https://b2b.baidu.com/s?q={}&from=search".format(self.name)
        self.driver = webdriver.Chrome("F:\\ChromeGo\\ChromeGo\\Browser\\chromedriver.exe")
        #  "F:\\ChromeGo\\ChromeGo\\Browser\\chromedriver.exe"
        self.page_num = 1  # 统计页码
        self.max_page = max_page  # 最大页码
        self.data = []  # 数据暂存列表

    # 执行函数
    def run(self):
        self.driver.get(self.url)
        self.get_data()

    # 提取数据
    def get_data(self):
        print("正在抓取 "+self.name+" 页面第"+str(self.page_num)+"页")
        # 向下滚动31000像素
        js = "window.scrollBy(0, 1000)"
        # 设置滚动次数
        for i in range(5):
            self.driver.execute_script(js)  # 滚动页码
            sleep(2)

        page = self.driver.page_source  # 页码源码
        # print(page)
        soup = BeautifulSoup(page, "html.parser")
        div = soup.find("div", class_="product-list").find_all_next("div", class_="inline")
        for d in div:
            try:
                # 获取产品标题
                title = d.find("div", class_="p-card-img-layout").attrs["title"]
                # 利用正则获取商品价格，因为获取的数据需要编码转换，所以下面进行转换
                # price = re.findall(r'p-card-price.*?data-v-f9f0a31a="" title="(.*?)"', str(str(d).encode()), re.S)[0]
                # print('title=====',title)
                # price = bytes(price, encoding='utf-8')
                # price = eval(repr(price).replace("\\\\", "\\"))
                # price = str(price.decode("utf-8")).replace("\xa5", "")

                # 将数据追加到暂存的列表中
                # self.data.append({"title": title, "price": price})
                self.data.append({"title":title})
            except:
                pass
        # 调用换页函数
        self.next_page()

        # print(self.data)
    # 换页
    def next_page(self):
        print("第"+str(self.page_num)+"页爬取成功")
        try:
            # 进行判断，爬取到最后一页终止
            if self.page_num < self.max_page:
                self.page_num += 1
                self.driver.find_element_by_class_name("ivu-page-next").click()
                # self.driver.find_element_by_class_name("ivu-page-next ivu-page-custom-text").click()
                sleep(1)

                # 换页成功后调用解析数据函数
                self.get_data()
            else:
                self.save_data()
        except Exception as s:
            # 如果换页失败，可能是页面滑动没滑到最下面，所以可以到上面进行修改滑到次数
            print("爬取到第" + str(self.page_num) + "页后出错，错误信息为：\n" + str(s))
            self.save_data()

    # 数据保存
    def save_data(self):
        with open("data.json", "a", encoding="utf8") as fp:
            fp.write(json.dumps(self.data, ensure_ascii=False, indent=4))
        print("数据保存成功")
        self.driver.close()


if __name__ == '__main__':
    # name = input("要爬取的关键词")
    name = "辛集市德泰机械科技有限公司"
    # max_page = eval(input("请输入爬取的最大页码"))
    max_page = 14
    b2b = b2b(name, max_page)
    b2b.run()
