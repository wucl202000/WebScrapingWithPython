# -*- coding: utf-8 -*-
# Platform:              win7
# Python:                3.5
# Author:                wucl(wucl-20@163.com)
# Program:               test
# History:               2016.7.26


import json
from urllib.request import urlopen


def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code')

print(getCountry("112.136.72.222"))