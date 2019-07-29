###########################################
# The purpose of this script is to get traffic data from Iowa DOT API
# Data is updated every five minutes
# Author: Eric Becerril-Blas
###########################################

# This library is used for API requests
# Do `pip install requests` to use requests library
import requests
from requests.exceptions import HTTPError

# Libraries for JSON and CSV manipulation
import pandas as pd
import json
import csv
import ijson

###########################################
# Get the JSON response from the query url and create a JSON file from the response called iowa_output.json
# This part works fine
###########################################
response = requests.get('https://services.arcgis.com/8lRhdTsQyJpO52F1/arcgis/rest/services/RWIS_Traffic_Data_View/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

# Print the status code
if response:
    #status code is 200
    print('Success! Status code is ', response.status_code)
else:
    #status code is 404 or something else.
    print('An error has occurred. Status code is ',response.status_code)

#The response headers can give you useful information, such as the content type of the response payload and a time limit on how long to cache the response. To view these headers, access .headers
print(response.headers) #TEST

# The following just shows the content type
print(response.headers['Content-Type']) #TEST

# outputting and wrting  the JSON file
JSON_output = open('iowa_output.json','w')
JSON_output.write(response.text)
JSON_output.close()


###########################################
# Converting JSON to CSV in the following code... Not quite working yet
###########################################
json_response = response.json() #Converting response to a dictionary with Keys

print(json_response['attributes'][0])

'''
## COMMENTED THE WHOLE CHUNK OUT BELOW BECAUSE THIS WAS STUFF I TRIED IN THE PAST THAT CAME CLOSE TO WORKING
#json_response = response.json()

JSONtraffic_data = response.json()

json_response = json.dumps(JSONtraffic_data)

traffic_data_parsed = json.loads(json_response)

traffic_data = open('traffic.csv', 'w')

csvwriter = csv.writer(traffic_data)

#csvwriter.writerow(data[0].keys())  # header row
print(response.request.body)

#another way?
filename = "iowa_output.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)
print(columns[0])

good_columns = [
 "OBJECTID",
 "STATUS",
 "OCCUPANCY",
 "UNIQUE_ID",
 "SITE_NUMBER",
 "RPUID",
 "SENSOR_NAME",
 "TOWNSHIP",
 "SECTION",
 "RANGE",
 "RPUID_NAME",
 "NWS_ID",
 "LATITUDE",
 "LONGITUDE",
 "GPS_ALTITUDE",
 "COUNTY_NAME",
 "ROUTE_NAME",
 "MILE_POST",
 "COST_CENTER",
 "GARAGE_NAME",
 "DISTRICT_NO",
 "COUNTY_NO",
 "DATA_LAST_UPDATED",
 "REST_EDITED",
 "NORMAL_VOLUME",
 "LONG_VOLUME",
 "AVG_SPEED",
 "AVG_HEADWAY",
 "LANE_ID",
 "UTC_OFFSET"
]
data = []
with open(filename, 'r') as f:
    objects = ijson.items(f, 'data.item')
    for row in objects:
        selected_row = []
        for item in good_columns:
            selected_row.append(row[column_names.index(item)])
            data.append(selected_row)
print(data[0])
'''
