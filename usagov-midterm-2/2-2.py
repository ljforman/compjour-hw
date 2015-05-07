import json
import os
import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
CODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
sdata = requests.get(CODES_URL).json()
mylist = []
for d in sdata:
        # we set NumberOfJobs to 1 because we don't need job listings, just
        # the TotalJobs
        atts = {'CountrySubdivision': d,  'NumberOfJobs': 1}
        resp = requests.get(BASE_USAJOBS_URL, params = atts)
        data = resp.json()
        # the 'TotalJobs' value is always a string, we want it as an
        # int
        jobcount = int(data['TotalJobs'])
        mylist.append([d, jobcount])

print(mylist)


# save the file on to your hard drive
os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/domestic-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()