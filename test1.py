#!/usr/bin/python
# Platform:            win7
# Python:              3.5
# Author:              wucl(wucl-20@163.com)
# Program:             test1
# History:             2016.7.25


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.baidu.com")
cont = html.read()
soup = BeautifulSoup(cont, 'html.parser')
print(soup.title.get_text())
