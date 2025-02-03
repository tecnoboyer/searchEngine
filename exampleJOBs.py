import os
import requests

current_directory = os.path.dirname(os.path.abspath(__file__))
api_key_file_path = os.path.abspath(os.path.join(current_directory, '..', 'API_KEY.txt'))
EngineID_file_path = os.path.abspath(os.path.join(current_directory, '..', 'EngineID.txt'))

api_key = open(api_key_file_path).read().strip()
EngineID = open(EngineID_file_path).read().strip()

search_query = 'software engineer'  
url = 'https://www.googleapis.com/customsearch/v1'

params = {
    'q': search_query,
    'key': api_key,
    'cx': EngineID,
    'filter': '0',  # Ensures the results are more relevant
    'num': 10,  # Adjust the number of search results to retrieve
    'siteSearch': 'careers',  # Focus on job posting sites
}

response = requests.get(url, params=params)
results = response.json()

# Print all job posting links from the results
for item in results.get('items', []):
    print(item['link'])
