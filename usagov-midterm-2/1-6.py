#with itemgetter:

import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def sortkey(thing):
    country = thing[1]
    return country

csorted = sorted(intl_data, key = sortkey)        

def desc(thing):
    jobs = thing[1]
    return jobs

desclist = sorted(csorted, key = desc, reverse = True)

print(desclist[0:10]) 
 
totalothers = 0
for jobs in desclist:
    totalothers =+ jobs[1]
print(totalothers)
print("Others, x")