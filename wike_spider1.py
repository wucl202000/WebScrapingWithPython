# -*- coding:utf-8 -*-
# Platform:              win7
# Python:                3.5
# Author:                wucl(wucl-20@163.com)
# Program:               Spider on Wiki
# History:               2016.7.26


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    soup = BeautifulSoup(html.read(), 'html.parser')
    try:
        print(soup.h1.get_text())
        print(soup.find(id='mw-content-text').findAll("p")[0])
        print(soup.find(id='ca-edit').find('span').find('a')['href'])
    except AttributeError:
        print("Attribute Error, Don't worry!!")
    for link in soup.findAll("a", href=re.compile(r"^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            if link['href'] not in pages:
                newPage = link['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")