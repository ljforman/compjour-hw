# `job` is one of the job listings in the job_data dump
import json
import requests
import os
from datetime import datetime
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
jobs = jdata['jobs']

def get_ca_cities(job):
   cities = job['Locations'].split(";") 
   city_names = []
   for city in cities:        
        if 'California' in city:
            x = city.split(",")
            city_names.append(x[0])

   return city_names                



mylist = []
for job in jobs:
    mylist.extend(get_ca_cities(job))

from collections import Counter
x = Counter(mylist)

 
finalcities = []
finalcities.append(['City', 'Job Count'])
for key, value in x.items():
    finalcities.append([key, value])




with open("California_Google_Geochart.html") as f:
    htmlstr = f.read()



# include all the countries
tablerows = []
for d in finalcities[1:]:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)
#
with open("2-15.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(finalcities))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)





# # 
# <html>
#   <head>
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

#     <script type='text/javascript' src='https://www.google.com/jsapi'></script>

#   </head>
#   <body>

#     <script type='text/javascript'>
#      google.load('visualization', '1', {'packages': ['geochart']});
#      google.setOnLoadCallback(drawMarkersMap);

#       function drawMarkersMap() {
#       var data = #CHART_DATA#;

#       var datatable = google.visualization.arrayToDataTable(data)

#       var options = {
#         region: 'US-CA',
#         resolution: 'provinces',
#         displayMode: 'markers',
#         backgroundColor: {fill: '#A5C5FF', strokeWidth: 2, stroke: '#333'},
#         datalessRegionColor: '#ddeedd',
#         colorAxis: {colors: ['yellow', 'red']}
#       };

#       var chart = new google.visualization.GeoChart(document.getElementById('mychart'));
#       chart.draw(datatable, options);
#     };
#     </script>


#     <div class="container">
#       <div id="mychart" style="width: 900px; height: 500px;"></div>
#       <table class="table table-striped table-condensed">
#         <thead>
#           <tr>
#             <th>City</th>
#             <th>Jobs</th>
#           </tr>
#         </thead>
#         <tbody>
#           #TABLE_ROWS#
#         </tbody>
#       </table>
#     </div>




#   </body>
# </html>

