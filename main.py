import os

# Get the directory of the current file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the API_KEY file in the parent directory
api_key_file_path = os.path.abspath(os.path.join(current_directory, '..', 'API_KEY.txt'))

# Open and read the API_KEY file
api_key = open(api_key_file_path).read()

print(api_key)
