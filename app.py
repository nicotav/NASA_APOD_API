import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

# Make a request to the NASA Open APIs endpoint
response = requests.get(
    'https://api.nasa.gov/planetary/apod', params={'api_key': api_key})

# Check if the request was successful
if response.status_code == 200:
    # Extract the data from the response JSON
    datas = response.json()

    # Print the name and description of each mission
    print(datas)


else:
    # If the request failed, print the error message
    print('Error:', response.text)


print("Done")
