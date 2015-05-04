import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
state_name_1 = 'California'
state_name_2 = 'Florida'
state_name_3 = 'New York'
state_name_4 = 'Maryland'
atts_1 = {"CountrySubdivision": state_name_1, 'NumberOfJobs': 1}
resp_1 = requests.get(BASE_USAJOBS_URL, params = atts_1)
data_1 = resp_1.json()
atts_2 = {"CountrySubdivision": state_name_2, 'NumberOfJobs': 1}
resp_2 = requests.get(BASE_USAJOBS_URL, params = atts_2)
data_2 = resp_2.json()
atts_3 = {"CountrySubdivision": state_name_3, 'NumberOfJobs': 1}
resp_3 = requests.get(BASE_USAJOBS_URL, params = atts_3)
data_3 = resp_3.json()
atts_4 = {"CountrySubdivision": state_name_4, 'NumberOfJobs': 1}
resp_4 = requests.get(BASE_USAJOBS_URL, params = atts_4)
data_4 = resp_4.json()


stuff = {state_name_1:data_1['TotalJobs'], state_name_2:data_2['TotalJobs'], state_name_3:data_3['TotalJobs'], state_name_4:data_4['TotalJobs']}
print(stuff)
