

import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def sortkey(thing):
    country = thing[1]
    return country

csorted = sorted(intl_data, key = sortkey,  reverse = True)        

for d in csorted:
    if d[1] > 10:
        print('%s,%s' % (d[0],d[1]) ) 
   