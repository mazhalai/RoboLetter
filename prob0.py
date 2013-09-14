import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

result=json.load(response)

row1=result["results"]

for i in range(0,10):
	print i,row1[i]['text']
