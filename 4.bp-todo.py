# Import libraries for making API requests, handling JSON and working with files/folders
import requests
import json
import os
from datetime import datetime

# API endpoint we want to extract data from
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder for our extracted data if it doesn't already exist
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Create a timestamp so each extract gets a unique filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

# set up a retry settings in case the API fails



# Keep trying until the maximum number of attempts is reached


# Send a GET request to the API
response = requests.get(url)
# Get Status
status = response.status_code

# Write an if statement based on the status code
if 200 <= status < 300:
    # Convert the JSON response into Python variable
    data = response.json()

    # Open the output file and write the API data to it as JSON
    with open(filename, 'w') as file:
        json.dump(data, file)


# Print the success comment
    print(f'File {filename} was successfully saved')
# add break

    # Retry for client-side errors or server errors
elif status < 200 or status >= 500:
    print(f'Status code {status}')
    # Wait before retrying to avoid repeatedly hitting the API

    # For other errors, don't retry because the issue needs to be fixed
else:
    print(f'Error. Status code {status}. Fix it.')
# add break