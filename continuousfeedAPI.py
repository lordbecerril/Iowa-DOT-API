###########################################
# The purpose of this script is to get continuous traffic data from Iowa DOT
# Data is updated every five minutes
# Author: Eric Becerril-Blas
###########################################

# This library is used for API requests
# Do `pip install requests` to use requests
import requests
from requests.exceptions import HTTPError

# Libraries for JSON and CSV manipulation
import pandas as pd
import json
import csv

###########################################
# Get the JSON response from the query url and create a JSON file from the response called iowa_output.json
###########################################
response = requests.get('https://services.arcgis.com/8lRhdTsQyJpO52F1/arcgis/rest/services/RWIS_Traffic_Data_View/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

# Print the status code
if response:
    #status code is 200
    print('Success! Status code is ', response.status_code)
else:
    #status code is 404 or something else.
    print('An error has occurred. Status code is ',response.status_code)

print(response.headers) #TEST

print(response.headers['Content-Type']) #TEST

# outputting the JSON file
JSON_output = open('iowa_output.json','w')
JSON_output.write(response.text)
JSON_output.close()
#TESTS
#print(response.content)
#print(response.text)
#print(response.json())

###########################################
# Converting JSON to CSV in the following code... Not quite working yet
###########################################
#json_response = response.json()

JSONtraffic_data = response.json()

json_response = json.dumps(JSONtraffic_data)

traffic_data_parsed = json.loads(json_response)

traffic_data = open('traffic.csv', 'w')

csvwriter = csv.writer(traffic_data)

df=pd.read_json("iowa_output.json")
