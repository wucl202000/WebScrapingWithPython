# -*- coding: utf-8 -*-
# Platform:               win7
# Python:                 3.5
# Author:                 wucl(wucl-20@163.com)
# Program:                test
# History:                2016.7.26


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime, re, random, json


random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    soup = BeautifulSoup(html.read(), 'html.parser')
    return soup.find("div", {'id':'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
#    print("History url is " + historyUrl)
    html = urlopen(historyUrl)
    soup = BeautifulSoup(html.read(), 'html.parser')
    ipAddresses = soup.findAll("a", {"class":"mw-userlink mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks("/wiki/Python_(programming_language)")

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code')

while len(links) > 0:
    for link in links:
 #       print("---------------------------------------------------------------------")
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            print(historyIP + "  is from " + getCountry(historyIP))

    newLink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLink)