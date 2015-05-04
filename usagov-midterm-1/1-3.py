import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
countries = 'China', 'South Africa', 'Tajikistan'
total = 0
for country in countries:
    atts = {"Country": country, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    jobs = data['TotalJobs']
    total += int(jobs)
    print("%s has %s job listings." % (country, jobs))
    
print("Together, they have %s job listings." %  total )