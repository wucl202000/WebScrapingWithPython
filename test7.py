# -*- coding:utf-8 -*-
# Platform:            win7
# Python:              3.5
# Author:              wucl(wucl-20@163.com)
# Program:             test
# History:             2016.7.26


from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com").read()
soup = BeautifulSoup(html, 'html.parser')
imageLocation = soup.find("a", {"id":"logo"}).find("img")['src']
urlretrieve(imageLocation, 'logo.jpg')
