# import packages
import requests
import json
import os
from datetime import datetime

# Define url variable
url = 'https://api.tfl.gov.uk/BikePoint/'

# Create a folder for our extracted data if it doesn't already exist



# Create a timestamp so each extract gets a unique filename




# Send a GET request to the API
response = requests.get(url)

# Convert the JSON response into Python variable


# Open the output file and write the API data to it as JSON






