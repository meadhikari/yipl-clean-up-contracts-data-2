import pandas as pd
def latlong(location):
    import urllib2
    import json
    content = json.loads(urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address="+location+"%20District&sensor=false%22").read())["results"][0]["geometry"]["location"]
    return str(content["lat"])+","+str(content["lng"])


a = pd.read_csv("contracts.csv")
b = pd.read_csv("awards.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='contractname')
merged['latlon'] = merged['awardeeLocation'].map(lambda x: latlong(x))
merged.to_csv("output.csv", index=False)
print "Total Amount of closed contracts: "+str(merged[merged.status == "Closed"]["Amount"].sum())

