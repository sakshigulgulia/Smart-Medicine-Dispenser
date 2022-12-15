# Import the request module
import requests
from time import sleep
for i in range(14):
    queries = {"api_key": "0KKK3VB4GKNVPQQF",
                   "field1": 16-i,
                   "field2": 15-i,
                   "field3": 14-i,
                   "field4": 17-i}
    r = requests.get('https://api.thingspeak.com/update', params=queries)
    if r.status_code == requests.codes.ok:
        print("Data Received!")
    else:
        print("Error Code: " + str(r.status_code))
    sleep(4)
