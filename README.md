# Iowa-DOT-API

The purpose of the scripts in this repo are for querying the Iowa DOT Traffic data found [here](https://data.iowadot.gov/datasets/road-weather-information-system-rwis-traffic-data/data?orderBy=DATA_LAST_UPDATED).<br/>
The Query URL is [here](https://services.arcgis.com/8lRhdTsQyJpO52F1/arcgis/rest/services/RWIS_Traffic_Data_View/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json).

## continuousfeedAPI.py
This script is responsible for calling the JSON data from the Query URL. From there, it turns the JSON data into CSV format (traffic.csv) and then seperates the CSV into 3 respective sources: Occupancy, Volume, and Speed. Each respectively named IowaOccupancy.csv, IowaVolume.csv, and IowaSpeed.csv.
