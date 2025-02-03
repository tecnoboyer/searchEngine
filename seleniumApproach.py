import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Path to ChromeDriver (adjust as needed)
chromedriver_path = '/path/to/chromedriver'  # Replace with your path

# Initialize the browser (Chrome)
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Function to scrape job details, including the 'Show More' content
def scrape_full_snippet(job_link):
    try:
        # Open the job page in the browser
        driver.get(job_link)
        
        # Wait for the page to load
        time.sleep(3)  # Wait for 3 seconds (adjust if needed)
        
        # Try to click the 'Show More' button (if it exists)
        try:
            show_more_button = driver.find_element(By.XPATH, "//button[contains(text(),'Show more')]")
            show_more_button.click()
            time.sleep(2)  # Wait for the content to load
        except:
            print("No 'Show more' button found or button not clickable.")
        
        # Now that the content is fully loaded, scrape the snippet
        snippet_element = driver.find_element(By.XPATH, "//div[contains(@class, 'snippet-class')]")  # Adjust the XPath accordingly
        full_snippet = snippet_element.text if snippet_element else "Snippet not available."
        
        return full_snippet
    except Exception as e:
        print(f"Error scraping {job_link}: {e}")
        return 'Error scraping job'
    finally:
        # Close the browser window after scraping
        driver.quit()

# Example usage
job_link = 'https://example.com/job-page'  # Replace with actual job link
full_snippet = scrape_full_snippet(job_link)
print(full_snippet)
