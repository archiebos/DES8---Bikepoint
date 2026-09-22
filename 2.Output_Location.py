# import packages
import requests
import json
import os
from datetime import datetime

# API endpoint we want to extract data from
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder for our extracted data if it doesn't already exist
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# Create a timestamp so each extract gets a unique filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'


# Send a GET request to the API
response = requests.get(url)

# Convert the JSON response into Python variable
data = response.json()

# Open the output file and write the API data to it as JSON
with open(filename, 'w') as file:
    json.dump(data, file)
