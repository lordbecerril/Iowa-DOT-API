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

# Used to convert UTC timestamp to its rfc3339 equivalent
import datetime

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

# outputting and wrting  the JSON file
JSON_output = open('iowa_output.json','w')
JSON_output.write(response.text)
JSON_output.close()

###########################################
# Converting JSON to CSV in the following code
###########################################
json_response = response.json() #Converting response to a dict with keys

#Another way to write the json as a dict
with open('iowa_output.json') as json_data:
    data = json.load(json_data)


goodColumns =[]

for item in range(len(json_response["fields"])):
    goodColumns.append(json_response['fields'][item]['alias'])

data = []
for item in range(len(json_response["features"])):
    entry = []
    entry.append(json_response['features'][item]['attributes']['OBJECTID'])
    entry.append(json_response['features'][item]['attributes']['STATUS'])
    entry.append(json_response['features'][item]['attributes']['OCCUPANCY'])
    entry.append(json_response['features'][item]['attributes']['UNIQUE_ID'])
    entry.append(json_response['features'][item]['attributes']['SITE_NUMBER'])
    entry.append(json_response['features'][item]['attributes']['RPUID'])
    entry.append(json_response['features'][item]['attributes']['SENSOR_NAME'])
    entry.append(json_response['features'][item]['attributes']['TOWNSHIP'])
    entry.append(json_response['features'][item]['attributes']['SECTION'])
    entry.append(json_response['features'][item]['attributes']['RANGE'])
    entry.append(json_response['features'][item]['attributes']['RPUID_NAME'])
    entry.append(json_response['features'][item]['attributes']['NWS_ID'])
    entry.append(json_response['features'][item]['attributes']['LATITUDE'])
    entry.append(json_response['features'][item]['attributes']['LONGITUDE'])
    entry.append(json_response['features'][item]['attributes']['GPS_ALTITUDE'])
    entry.append(json_response['features'][item]['attributes']['COUNTY_NAME'])
    entry.append(json_response['features'][item]['attributes']['ROUTE_NAME'])
    entry.append(json_response['features'][item]['attributes']['MILE_POST'])
    entry.append(json_response['features'][item]['attributes']['COST_CENTER'])
    entry.append(json_response['features'][item]['attributes']['GARAGE_NAME'])
    entry.append(json_response['features'][item]['attributes']['DISTRICT_NO'])
    entry.append(json_response['features'][item]['attributes']['COUNTY_NO'])
    utc_timestamp = json_response['features'][item]['attributes']['DATA_LAST_UPDATED']
    utc_timestamp = datetime.datetime.utcnow()
    entry.append(utc_timestamp.isoformat("T") + "Z")
    utc_timestamp = json_response['features'][item]['attributes']['REST_EDITED']
    utc_timestamp = datetime.datetime.utcnow()
    entry.append(utc_timestamp.isoformat("T") + "Z")
    entry.append(json_response['features'][item]['attributes']['NORMAL_VOLUME'])
    entry.append(json_response['features'][item]['attributes']['LONG_VOLUME'])
    entry.append(json_response['features'][item]['attributes']['AVG_SPEED'])
    entry.append(json_response['features'][item]['attributes']['AVG_HEADWAY'])
    entry.append(json_response['features'][item]['attributes']['LANE_ID'])
    entry.append(json_response['features'][item]['attributes']['LANE_ID'])
    data.append(entry)

df = pd.DataFrame(data, columns = goodColumns)
df.to_csv("traffic.csv",index = False)

data = pd.read_csv("traffic.csv")

#df_occupancy = data[['OBJECTID','Sensor Status (1=Active 0=Inactive)','Occupancy','Unique ID','RWIS Site Number','RWIS RPU ID','Sensor Name','PLSS Township','PLSS Section','PLSS Range','RWIS Name','NWS ID','Latitude','Longitude','Altitude','County Name','Route Name','Mile Post','Cost Center','Garage Name','DOT District','County Number','Data Last Pulled from RWIS Sensor (UTC)', 'REST Service Last Updated (UTC)', 'Normal Volume', 'Long Volume', 'Average Speed (MPH)','Average Headway','Lane ID', 'UTC Offset']]
df_occupancy = data[['Data Last Pulled from RWIS Sensor (UTC)', 'REST Service Last Updated (UTC)','OBJECTID','Sensor Status (1=Active 0=Inactive)','Occupancy','Unique ID','RWIS Site Number','RWIS RPU ID','Sensor Name','PLSS Township','PLSS Section','PLSS Range','RWIS Name','NWS ID','Latitude','Longitude','Altitude','County Name','Route Name','Mile Post','Cost Center','Garage Name','DOT District','County Number','Average Headway','Lane ID', 'UTC Offset']]
df_occupancy.to_csv("IowaOccupancy.csv",index = False)

df_speed = data[['Data Last Pulled from RWIS Sensor (UTC)', 'REST Service Last Updated (UTC)','OBJECTID','Sensor Status (1=Active 0=Inactive)','Unique ID','RWIS Site Number','RWIS RPU ID','Sensor Name','PLSS Township','PLSS Section','PLSS Range','RWIS Name','NWS ID','Latitude','Longitude','Altitude','County Name','Route Name','Mile Post','Cost Center','Garage Name','DOT District','County Number', 'Average Speed (MPH)','Average Headway','Lane ID', 'UTC Offset']]
df_speed.to_csv("IowaSpeed.csv",index = False)

df_volume = data[['Data Last Pulled from RWIS Sensor (UTC)', 'REST Service Last Updated (UTC)','OBJECTID','Sensor Status (1=Active 0=Inactive)','Unique ID','RWIS Site Number','RWIS RPU ID','Sensor Name','PLSS Township','PLSS Section','PLSS Range','RWIS Name','NWS ID','Latitude','Longitude','Altitude','County Name','Route Name','Mile Post','Cost Center','Garage Name','DOT District','County Number', 'Normal Volume', 'Long Volume', 'Average Headway','Lane ID', 'UTC Offset']]
df_volume.to_csv("IowaVolume.csv",index = False)
