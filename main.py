import os


current_directory = os.path.dirname(os.path.abspath(__file__))
api_key_file_path = os.path.abspath(os.path.join(current_directory, '..', 'API_KEY.txt'))
EngineID_file_path = os.path.abspath(os.path.join(current_directory, '..', 'EngineID.txt'))

api_key = open(api_key_file_path).read()
EngineID= open(EngineID_file_path).read()

print(api_key)
print(EngineID)
