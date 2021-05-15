import requests
 #this doesn't work as of 5/14/2021 10pm
url = 'http://localhost:5500/results'
r = requests.post(url,json={'overall':4, 'aroma':3, 'appearance':4, 'palate':2, 'taste':5, 'abv':10})

print(r.json())