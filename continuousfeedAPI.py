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

#Another way to write the json as a dict
with open('iowa_output.json') as json_data:
    data = json.load(json_data)

# using the from_dict load function. Note that the 'orient' parameter
# is not using the default value (or it will give the error "ValueError: arrays must all be the same length")
# We transpose the resulting df and set index column as its index to get this result
#pd.DataFrame.from_dict(data, orient='index').T.set_index('index')
df = pd.DataFrame.from_dict(json_response, columns = ['features'],orient='index')# I added the "orient ='index' " because without it I get
print(df,"\n")

# Transpose the dataframe
df_transposed = df.T
print("Transposed dataframe:")
print(df_transposed)

# Export dataframe to CSV file
df_transposed.to_csv("traffic.csv")
