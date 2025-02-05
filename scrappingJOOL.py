import http.client
import os
import csv
import json
import requests
from bs4 import BeautifulSoup

# Get the path to the API key
current_directory = os.path.dirname(os.path.abspath(__file__))
JOOL_API_KEY_file_path = os.path.abspath(os.path.join(current_directory, '..', 'joobleAPI_KEY.txt'))

# Read the API key
JOOL_API_KEY = open(JOOL_API_KEY_file_path).read().strip()

# Set up the connection and the query
host = 'jooble.org'
connection = http.client.HTTPConnection(host)
headers = {"Content-type": "application/json"}

# Query to search for jobs (keywords and location)
body = '{"keywords": "buyer", "location": "Ontario"}'
connection.request('POST', '/api/' + JOOL_API_KEY, body, headers)

# Get the response
response = connection.getresponse()
data = response.read().decode()

# Parse the response as JSON
job_data = json.loads(data)

# Extract the job listings
jobs = job_data.get("jobs", [])

# Define CSV file path
csv_file_path = os.path.join(current_directory, 'job_listings.csv')

# Function to scrape job details from the job link
def scrape_job_details(job_link):
    try:
        # Fetch the job page
        response = requests.get(job_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract job details (customize based on the job site structure)
        # Example: Find the job description
        description = soup.find('div', {'class': 'job-description'})  # Adjust selector based on actual structure
        if description:
            description_text = description.get_text(strip=True)
        else:
            description_text = 'Description not available'
        
        return description_text
    except Exception as e:
        print(f"Failed to scrape {job_link}: {e}")
        return 'Error scraping job'

# Open CSV file in write mode
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "location", "snippet", "salary", "source", "type", "company", "updated", "link", "description"])
    
    # Write header row
    writer.writeheader()
    
    # Write job rows with scraped description
    for job in jobs:
        job_link = job.get("link", "")
        job_description = scrape_job_details(job_link)  # Scrape the job page
        
        writer.writerow({
            "title": job.get("title", ""),
            "location": job.get("location", ""),
            "snippet": job.get("snippet", ""),
            "salary": job.get("salary", ""),
            "source": job.get("source", ""),
            "type": job.get("type", ""),
            "company": job.get("company", ""),
            "updated": job.get("updated", ""),
            "link": job.get("link", ""),
            "description": job_description
        })

# Output a message when the CSV is written
print(f"Job listings saved to {csv_file_path}")
