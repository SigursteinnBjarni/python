#!/bin/python

import requests
import json
import operator
import sys
r = requests.get('http://apis.is/petrol')
data = json.loads(r.text)

prices = {}
#price, name, station
for station in data['results']:
    mystation = station['name']
    myprice = station['bensin95']
    name = station['company']
    location = name + " " + mystation
    prices[location] = myprice

sorted_prices = sorted(prices.items(), key=operator.itemgetter(1))
count = 10 

for place, price in sorted_prices:
    print("{0}\t{1}".format(place.encode("utf-8"),price))
