import pandas as pd

def latlong(location):
    import urllib2
    import json
    try:
        content = json.loads(urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address="+location+"%20District&sensor=false%22").read())["results"][0]["geometry"]["location"]
        return str(content["lat"])+","+str(content["lng"])
    except:
        return ""


a = pd.read_csv("contracts.csv")
b = pd.read_csv("awards.csv")
#merged = pd.concat([a,b],keys=["contractname"],how='left')
merged = a.merge(b,on="contractname",how='left')
merged['latlon'] = merged['awardeeLocation'].map(lambda x: latlong(x) if x != "NaN" else "")
print "Total Amount of closed contracts: "+str(merged[merged.status == "Closed"]["Amount"].sum())
merged.fillna("", inplace=True)
merged.to_csv("output.csv", index=False)





