import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
countries = 'China', 'South Africa', 'Tajikistan'
for country in countries:
	atts = {"Country": country, 'NumberOfJobs': 1}
	resp = requests.get(BASE_USAJOBS_URL, params = atts)
	data = resp.json()
	

	print("%s has %s job listings." % (country, data['TotalJobs']))
	
state_name_1 = 'China'
state_name_2 = 'South Africa'
state_name_3 = 'Tajikistan'
atts_1 = {"Country": state_name_1, 'NumberOfJobs': 1}
resp_1 = requests.get(BASE_USAJOBS_URL, params = atts_1)
data_1 = resp_1.json()
atts_2 = {"Country": state_name_2, 'NumberOfJobs': 1}
resp_2 = requests.get(BASE_USAJOBS_URL, params = atts_2)
data_2 = resp_2.json()
atts_3 = {"Country": state_name_3, 'NumberOfJobs': 1}
resp_3 = requests.get(BASE_USAJOBS_URL, params = atts_3)
data_3 = resp_3.json()


x = (data_1['TotalJobs'])
y = (data_2['TotalJobs'])
z = (data_3['TotalJobs'])

w = int(x) + int(y) + int(z)

print("Together, they have %s job listings." %(w))