import json
from operator import itemgetter
## assumes you've made a copy of this file
# http://stash.compjour.org/files/code/answers/usajobs-midterm/sample-barchart-2.html
# and stashed it at a relative path:
# sample-geochart-2.html
with open("sample-geochart-2.html") as f:
    htmlstr = f.read()
with open("data-hold/intl-jobcount.json") as f:
    data = json.loads(f.read())

sorteddata = sorted(data, key = itemgetter(1), reverse = True)

# Just charting countries with at least one job
chartdata = []
chartdata.append(["Country", "Job Count"])
for c in sorteddata:
    if c[1] > 0:
        chartdata.append(c)

# include all the countries
tablerows = []
for d in sorteddata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)
#
with open("2-8.html", "w") as f:
    htmlstr = htmlstr.replace('#CHART_DATA#', str(chartdata))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    f.write(htmlstr)