# -*- coding:utf-8 -*-
# Platform:            win7
# Python:              3.5
# Author:              wucl(wucl-20@163.com)
# Program:             test download jpg via urlretrieve
# History:             2016.7.26


import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve


downloadDirectory = "downloaded/"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = 'http://' + source[4:]
    else:
        url = baseUrl + "/" + source
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www", "")
    path = path.replace(baseUrl, '')
    path = path.replace('/', '')
    path = downloadDirectory + path
    print(path)
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.mkdir(directory)
    return path

html =  urlopen("http://www.pythonscraping.com")
soup = BeautifulSoup(html.read(), 'html.parser')
downloadList = soup.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))