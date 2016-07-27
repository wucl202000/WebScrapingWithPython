# -*- coding:utf-8 -*-
# Platform:               win7
# Python:                 3.5
# Author:                 wucl(wucl-20@163.com)
# Program:                test
# History:                2016.7.27


from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)

dictReader = csv.DictReader(dataFile)
for row in dictReader:
    print(row)


csvReader = csv.reader(dataFile)
for row in csvReader:
    print(row)