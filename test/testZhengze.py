import re

## test RE
'''
.  表示任何单个字符 不包含换行符
[] 字符集，对单个字符给出取值范围  [abc]表示a或b或c  [a-z]表示a到z单个字符
[^ ]非字符集，对单个字符给出排除范围
*   前一个字符0次或者无数次扩展  abc* 表示 ab、abc、abcc、abcccc、等
+   前一个字符一次或无限次扩展   abc+ 表示 abc、abcc、abcccc、
?   前一个字符0次或1次扩展       abc？ 表示 ab、或者abc
|   左右表达式任何一个       abc|def 表示abc、def


{m} 前一个字符扩展几次  ab{2}c  表示abbc
{m，n} m至n次  ab{1,2}c 表示 abc、abbc

^ 匹配字符串开头  ^abc表示以abc开头
$ 匹配字符串结尾   abc$ 表示abc在字符串结尾

() 分组标记，内部只能使用|操作符  （abc)表示abc， （abc|def)表示abc、def

\d  数字，等价于[0-9]                     注意; \D 代表非数字字符
\w  单词字符， 等价于 [A-Za-z0-9]          注意: \W代表除了单词字符以外的字符
\s 空格字符 (包含换行符 Tab符)                   注:  \S代表除了空格字符以外的字符.



贪婪匹配和惰性匹配
    <.+>  会选中匹配下面一整行
    <span><b>This is a sample text</b></span>
    <.+?> 会选中匹配下面的标签
    <span><b> 和 </b></span>

ip地址测试
\b((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)\b
123
255.255.255.0
192.168.0.1
0.0.0.0
256.1.1.1
This is a string.
123.123.0
01.00.00.00





regex101com 测试样例


''<span><b>This is a sample text</b></span>''


#[A-Fa-f0-9]{6}\b
#00
#ffffff
#ffaaff
#00hh00
#aabbcc
#ffffffff





''use a used variable name is illegal.''
ac
abc
abbbbc
adc
abababac

an umbrella
a cat
a dog

tiger
aabbcc
dog
12345678
abc123456
ABCDEFG


re.search() 在一个字符中搜索匹配正则表达式的第一个位置 ，返回match对象
re.match() 从字符串的开始为只
'''

# 正则表达式： 字符串模式，（判断字符串是否符合一定的标准）

#1.创建模式对象
# pat = re.compile("AA")  #此处的AA是正则表达式，用来验证其他的字符串
# m = pat.search("AAAbbccaaAA").span()[1]  #search后面的字符串是被校验的内容
# print(m)
#2.没有模式对象
# m = re.search("AA","bbAA")
#
# print(m)  #只返回第一次出现的位置  span=（a，b） 左闭右开


# print(re.findall('[A-Z]','ASDaDFGAa')) #找到A-Z之间的大写字母
# print(re.findall('[A-Z]+','ASDaDFGAa')) #['ASD', 'DFGA']
# print(re.findall('[A-Z]','ASDaDFGAa')) #['A', 'S', 'D', 'D', 'F', 'G', 'A']

regex101.com
# sub

# 找到a用A来替换，在第三个字符串中查找
print(re.sub("a","A","ABCDabcdefg"))

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题

