# import packages
import requests
import json
import os
from datetime import datetime

# Define url variable
url = 'https://api.tfl.gov.uk/BikePoint/'

# Send a GET request to the API
response = requests.get(url)

# Print response
print(response.status_code)





