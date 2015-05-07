

import json
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

def sortkey(thing):
    country = thing[1]
    return country

csorted = sorted(intl_data, key = sortkey, reverse = True)

totalothers = 0
for jobs in csorted[0:10]:
    print('%s,%s' % (jobs[0], jobs[1]) )

for jobs in csorted[11:]:
    totalothers += jobs[1]


print('Others,' , totalothers)
