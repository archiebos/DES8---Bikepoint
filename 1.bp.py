import requests
import json
import os
from datetime import datetime

url = 'https://api.tfl.gov.uk/BikePoint/'

response = requests.get(url)

print(response.status_code)