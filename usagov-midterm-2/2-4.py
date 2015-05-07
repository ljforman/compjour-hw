import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())
domesticsorted = sorted(domestic_data)

for d in domesticsorted:
    if d[1] < 100:
        print( '%s,%s'  % (d[0], d[1]) )



