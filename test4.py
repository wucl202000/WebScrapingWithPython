# -*- coding: utf-8 -*-
# Platform:                win7
# Python:                  3.5
# Author:                  wucl(wucl-20@163.com)
# Program:                 test
# History:                 2016.7.26


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime, random


random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    soup = BeautifulSoup(html.read(), 'html.parser')
    return soup.find('div', {"id":"bodyContent"}).findAll("a", href=re.compile(r"^(/wiki/)((?!:).)*$"))

links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
    