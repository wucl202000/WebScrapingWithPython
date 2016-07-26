# -*- coding:utf-8 -*-
# Platfrom:              win7
# Python:                3.5
# Author:                wucl(wucl-20@163.com)
# Program:               test3
# History:               2016.7.26


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.19lou.com/?from=hangzhou")
soup = BeautifulSoup(html.read(), 'html.parser')

#for child in soup.find("table", {"id":"giftList"}).children:
#    print(child.find("td"))

#for sibling in soup.find("table", {"id":"giftList"}).tr.next_siblings:
#    print(sibling) #.find("span").get_text())
#print(soup.tbody)
#for table in soup.findAll('table').findAll('img'):
#    print(table)
#    print('*'*100)
for i in soup.findAll('li'):
    cont = i.find("a")
    try:
        print(cont['title'], cont['href'])
    except:
        pass
 #   print(i.attrs)
#    print(i.parent.previous_sibling.get_text())

#print(soup.find("img", {"src":re.compile(r"../img/gifts/img\d.jpg")})) #.parent.previous_sibling.get_text())
#print(soup.findAll(lambda tag: len(tag.attrs) == 2))