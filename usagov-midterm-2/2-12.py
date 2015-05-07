import json
import requests
import os
## for subsequent exercises
## copy this data-loading snippet
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy...")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']

def cleanmoney(val):
    x = val.replace('$', '').replace(',', '')
    return float(x)

def findspread(job):
    x = cleanmoney(job['SalaryMax']) - cleanmoney(job['SalaryMin'])
    return x

spreadlist = []
for z in jobs:
    if cleanmoney(z['SalaryMax']) < 100000:
        x = findspread(z)
        title = z['JobTitle']
        min = cleanmoney(z['SalaryMin'])
        max = cleanmoney(z['SalaryMax'])
        spreadlist.append([title, x, min, max])
sortedlist = sorted(spreadlist)
#print(sortedlist)
def spreadsort(thing):
    spread = thing[1]
    return spread     

ssorted = sorted(sortedlist, key = spreadsort, reverse = True)

for d in ssorted[0:1]:
    print('%s, %s, %s' % (d[0],d[2],d[3]))
