import requests
import pandas as pd

response = requests.get('https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49')

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()

data = response.text
print("Here is the JSON response:")
print(json_response,"\n")

# This data frame works for this API easily
df = pd.DataFrame.from_dict(json_response, orient='index') # I added the "orient ='index' " because without it I get "ValueError: arrays must all be the same length"
print("Here is the original dataframe:")
print(df,"\n")

df_transposed = df.T
print("Here is the dataframe transposed:")
print(df_transposed)
