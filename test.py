import json
import math

obj = {
    'name': 'Tollan',
    'profile': {
        'addr': '1234',
        'phone': 4567
    } 
}

op = obj['profile']['addr']

slack_data = '2023-06-19.json'

import json

# Open the file
with open('test.json', 'r') as file:
    # Read the contents
    data = file.read()

    # Parse the JSON data
    json_data = json.loads(data)

# Now you can work with the parsed JSON data
for item in json_data:
    # Access the properties of each JSON object
    print(item['name'])
    print('age' in item)

import pandas as pd

# Read the file into a pandas DataFrame
df = pd.read_json('test.json')
# print(df)
# Now you can work with the DataFrame
# Access the properties of each JSON object using DataFrame operations
# for index, row in df.iterrows():
#     if math.isnan(row['age']):
#         print( row['age'] )

# create an Empty DataFrame
# object With column names only
df = pd.DataFrame(columns = ['Name', 'Articles', 'Improved'])
print(df)
 
# append rows to an empty DataFrame
df = df.append({'Name' : 'Ankit', 'Articles' : 97, 'Improved' : 2200},
        ignore_index = True)
 
df = df.append({'Name' : 'Aishwary', 'Articles' : 30, 'Improved' : 50},
        ignore_index = True)
 
df = df.append({'Name' : 'yash', 'Articles' : 17, 'Improved' : 220},
      ignore_index = True)
 
df