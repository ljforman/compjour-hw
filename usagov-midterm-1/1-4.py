
#As a for loop
import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
names = ['California','New York','Florida','Maryland']
thedictionary = {}
for name in names:
    atts = {'CountrySubdivision': name, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    jobcount = resp.json()['TotalJobs']
    thedictionary[name] = int(jobcount)

print(thedictionary) 

