# Import libraries for making API requests, handling JSON and working with files/folders
import requests
import json
import os
from datetime import datetime
import time

# API endpoint we want to extract data from
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder for our extracted data if it doesn't already exist
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Create a timestamp so each extract gets a unique filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

# set up a retry settings in case the API fails
max_retry = 5
attempt = 0
delay = 10

# Keep trying until the maximum number of attempts is reached
while attempt < max_retry:

    # Send a GET request to the API
    response = requests.get(url)
    # Get Status
    status = response.status_code


    # Write an if statement based on the status code
    if 200 <= status < 300:
        # Convert the JSON response into Python variable
        data = response.json()


        # Check that the API returned data before trying to save it

        # Open the output file and write the API data to it as JSON
        with open(filename, 'w') as file:
            json.dump(data, file)

        # Print new response

        # Handle errors that occur while creating or writing to the file

    # Print the success comment
        print(f'File {filename} was successfully saved')
        break

        # Retry for client-side errors or server errors
    elif status < 200 or status >= 500:
        print(f'Status code {status}')
        # Wait before retrying to avoid repeatedly hitting the API
        time.sleep(delay)
        attempt += 1
        print(f'Status code {status}. Retrying. This was attempt {attempt}')

# For other errors, don't retry because the issue needs to be fixed
    else:
        print(f'Error. Status code {status}. Fix it.')
        break