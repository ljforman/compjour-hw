

import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
countries = 'China', 'South Africa', 'Tajikistan'
for country in countries:
	total = 0
	atts = {"Country": country, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	data = resp.json()
	total = total + 'TotalJobs'

	print("%s has %s job listings." % (country, data['TotalJobs']))
	print("Together, they have %s job listings." %(total))


