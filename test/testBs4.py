#测试beatuifulsoup

'''
BeautifulSoup4 将复杂HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种

- Tag
- NavigableString
- BeautifulSoup
- Comment
'''

from bs4 import BeautifulSoup
file = open("./baidu.html","rb") # 不加rb 则报错  unicodeDecodeError ：‘gbk'错误
html = file.read()
bs = BeautifulSoup(html,"html.parser")  #"html.parser"解析器

'''
print("bs.a = \n\t",bs.a)

print("\n\nbs.head= \n\t",bs.head)
#
print("\n\nbs.head的类型是： \n\t",type(bs.head))   #<class 'bs4.element.Tag'>  Tag，标签及其内容
                                                    # 只能拿到它所找到的第一内容
#
print("\n\nbs.title = \n\t",bs.title)
print(bs.title.string) #提取title标签里的值
# print(type(bs.title.string))  #NavigableString
#
#
print(bs.a.attrs)  #标签里面的属性值  return一个字典
#
#
print(type(bs))  #<class 'bs4.BeautifulSoup'>  表示整个文档
#
 '''
# print(bs.name)   # document
#
#
# print(bs.attrs)   # 空字典，没有标签
# print(bs)  #打印整个文档
#
# print(bs.a.string)
# print(type(bs.a.string))  # Comment是一个兔鳄属的NavigableString 输出得内容不包含注释的


# --------------------------
'''文档的遍历'''
#
# print(bs.head.contents)     # head标签里的内容
# print(bs.head.contents[9].string) # 百度一下你就知道
#

# 更多内容 搜索文档

# 这里用一下for循环打印列表元素，方便查看
def myprint(t_list):
    for item in t_list:
        print(item)

'''文档的搜索： 根据特点，结构 关键字搜索'''
# (1) find_all() 查找所有

#字符串过滤 ：会查找与字符串（标签）完全匹配的内容
# t_list = bs.find_all("a")
#
# myprint(t_list)


import re
# # #正则表达式搜索：  使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))
# myprint(t_list)



#用方法来搜索  ： 传入一个函数（方法）， 根据函数的要求来搜素
#不好用  作为了解
def name_is_exists(tag):

    return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
# myprint(t_list)

# kwargs 参数
# t_list = bs.find_all(id="head")
# myprint(t_list)

# for t in t_list:
#     if t.has_attr("name"):
#         print(t.name)
# t_list = bs.find_all(class_=True)


# t_list = bs.find_all(href="http://news.baidu.com")
# myprint(t_list)



# text 参数
# t_list= bs.find_all(text="hao123")   #参数可以是列表

# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# myprint(t_list)
# t_list=bs.find_all(text=re.compile("\d"))  #应用正则表达式查找包含特定文本的内容 （标签里的字符串）
#




#limit参数  limit来限定查找到的个数
# t_list = bs.find_all("a",limit=3)
#
#
# for item in t_list:
#     print(item)
#


#css选择器
print(bs.select('title'))
t_list = bs.select('title')  #通过标签来查找
myprint(t_list)
t_list =bs.select(".mnav")  #通过类名来查找
myprint(t_list)
t_list = bs.select("#ul")    #通过id来查找
myprint(t_list)
t_list= bs.select("a[class = 'bri']")  #通过属性来查找
myprint(t_list)
t_list = bs.select("head>title") #通过子标签来查找
myprint(t_list)
t_list = bs.select(".mnav ~ .bri")  # 查找mnav这个类的名为bri类的兄弟标签
print(t_list[len(t_list)-1].get_text())

# print(t_list[0].get_text())


