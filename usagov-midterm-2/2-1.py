import requests
BASE_WORLDJOBS_URL = "https://data.usajobs.gov/api/jobs"
codes = requests.get("http://stash.compjour.org/data/usajobs/CountryCode.json").json()
thelist = []
for value in codes.items():
    atts = {'Country': value, 'NumberOfJobs': 1}
    resp = requests.get(BASE_WORLDJOBS_URL, params = atts)
    jobcount = int(resp.json()['TotalJobs'])
    print(thelist)
    thelist.append('Country', jobcount)

#import requests
#BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
#codes = requests.get("http://stash.compjour.org/data/usajobs/us-statecodes.json").json()
#thelist = []
#thelist.append(["State", "Job Count"])
#for name, ab in codes.items():
    #atts = {'CountrySubdivision': name, 'NumberOfJobs': 1}
    #resp = requests.get(BASE_USAJOBS_URL, params = atts)
    #jobcount = int(resp.json()['TotalJobs'])
    #print(name)
    #thelist.append(['US-' + ab , jobcount])