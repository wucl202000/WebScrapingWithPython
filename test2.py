#!/usr/bin/python
# Platform:            win7
# Python:              3.5
# Author:              wucl(wucl-20@163.com)
# Program:             test2
# History:             2016.7.25


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
cont = html.read()
soup = BeautifulSoup(cont, 'html.parser')
name_list = soup.find_all("span", {"class":{"green","red"}})
print(soup.findAll({'h1','h2','h3','h4','h5','h6'}))
print(soup.findAll(text="the prince"))
#for name in name_list:
 #   print(name.get_text())
