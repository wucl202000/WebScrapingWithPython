# -*- coding:utf-8 -*-
# Platform:              win7
# Python:                3.5
# Author:                wucl(wucl-20@163.com)
# Program:               test
# History:               2016.7.26


import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
soup = BeautifulSoup(html.read(), 'html.parser')
table = soup.findAll('table', {'class':'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('csvFiles.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
