import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
states = ['Alaska', 'Hawaii']
for state in states:
    atts = {"CountrySubdivision": state, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    print("%s has %s job listings." % (state, data['TotalJobs']))

sum_jobs = 130+182
print("Together, they have %s job listings." %(sum_jobs))