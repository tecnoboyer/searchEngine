import os
import requests

current_directory = os.path.dirname(os.path.abspath(__file__))
api_key_file_path = os.path.abspath(os.path.join(current_directory, '..', 'API_KEY.txt'))
EngineID_file_path = os.path.abspath(os.path.join(current_directory, '..', 'EngineID.txt'))

api_key = open(api_key_file_path).read()
EngineID= open(EngineID_file_path).read()

search_query='"electrical engineer" jobs "hamilton" ontario after:2025-02-01'
url = 'https://www.googleapis.com/customsearch/v1'

params={
    'q':search_query,
    'key':api_key,
    'cx': EngineID

}

response = requests.get(url,params=params)
results= response.json()

print(results['items'][1])