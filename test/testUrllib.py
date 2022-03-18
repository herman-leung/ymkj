import urllib.request
# 获取一个get请求
'''
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8解码
'''
#获取一个post请求
#httpbin.org
import urllib.parse
'''
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding ='utf-8') #以utf-8的方式封装，parse是解析器。
response = urllib.request.urlopen("http://httpbin.org/post",data = data)
print(response.read().decode('utf-8'))
'''




'''
# 超时处理
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e,",time out!")

'''

# 响应头的问题：
'''
response = urllib.request.urlopen("http://baidu.com", timeout=1)
print(response.status)  #418  状态码，我是一个茶壶  # 状态码为200 是正常访问的
print(response.getheader("Server"))
print(response.getheaders())
'''


#伪装成浏览器

'''
url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({'name':'lh'}),encoding='utf-8')
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"
}
req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
'''


url = "https://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
