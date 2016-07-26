# -*- coding:utf-8 -*-
# Platform:        win7
# Python:          3.5
# Author:          wucl(wucl-20@163.com)
# Program:         test
# History:         2016.7.26


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime, random, pymysql


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='scraping', charset='utf8')
cur = conn.cursor()

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute('insert into pages (title, content) values (\"%s\", \"%s\")', (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1').get_text()
    content = soup.find("div", {'id':'mw-content-text'}).find('p').get_text()
    store(title, content)
    return soup.find("div", {'id':'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:

    cur.close()
    conn.close()