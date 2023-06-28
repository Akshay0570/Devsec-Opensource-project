import json
import requests
import sys

#url = 'http://3.135.238.207:8080/api/v2/findings?limit=1000'
url = 'http://192.168.32.128:8080/api/v2/findings/?tags=&test__tags=BUILD_ID'
headers = {'content-type': 'application/json',
           'Authorization': 'Token f5d6cb9c5b0cd0e67ae4e80d329117bea120b252'}
r = requests.get(url, headers=headers, verify=True)# set verify to False if ssl cert is self-signed
#print (r.json())
#y=json.loads(r.json())
test_txt = r.json()
count=0
for i in range(len(test_txt['results'])):
 count+=1
 #print (test_txt['results'][i]['found_by'])

 if ((test_txt['results'][i]['severity']) == 'High' or (test_txt['results'][i]['severity']) == 'Medium') and (test_txt['results'][i]['found_by']) == [73]:
    
    print('severity is High/Medium so pipeline terminated')
    #print(count)
    exit(1)

 else:
    print('there are no high/medium found so pipeline continue' )
    continue

print(count)
#exit(1)
