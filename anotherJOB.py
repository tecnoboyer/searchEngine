import requests
from bs4 import BeautifulSoup

# Define the job search parameters
JOB_TITLE = "software engineer"
LOCATION = "Canada"
BASE_URL = "https://www.indeed.com/jobs"

# Prepare query parameters
params = {
    "q": JOB_TITLE,
    "l": LOCATION,
}

# Send GET request to Indeed
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(BASE_URL, params=params, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find job postings (modify based on the site's structure)
    job_cards = soup.find_all("div", class_="job_seen_beacon")

    for job in job_cards[:5]:  # Get first 5 jobs
        title = job.find("h2").text.strip() if job.find("h2") else "No title"
        company = job.find("span", class_="companyName").text.strip() if job.find("span", class_="companyName") else "No company"
        location = job.find("div", class_="companyLocation").text.strip() if job.find("div", class_="companyLocation") else "No location"
        
        print(f"Job Title: {title}\nCompany: {company}\nLocation: {location}\n")

else:
    print("Failed to retrieve job postings.")
    print(response)
