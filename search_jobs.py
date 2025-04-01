import requests
import csv

API_URL = "https://jooble.org/api/ad755797-6f99-4d72-afd6-080f5e8a9e72"
payload = {
    "keywords": "data engineer",
    "location": "New York",
    "datePosted": "1"  # last 24 hours if supported
}

response = requests.post(API_URL, json=payload)
data = response.json()

with open('jooble_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Location', 'Date', 'URL'])
    for job in data.get('jobs', []):
        writer.writerow([
            job['title'],
            job['company'],
            job['location'],
            job['updated'],
            job['link']
        ])
