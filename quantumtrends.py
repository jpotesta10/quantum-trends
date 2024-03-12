# Import necessary libraries
from dotenv import load_dotenv
import requests
import os

# Load environment variables
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv('API_KEY')  # Ensure this matches your .env file's variable name

# Define the endpoint and parameters for the request
url = "https://newsapi.org/v2/everything"
params = {
    'q': 'tesla',
    'from': '2024-02-12',
    'sortBy': 'publishedAt',
    'apiKey': api_key
}

# Make the request to NewsAPI
response = requests.get(url, params=params)
data = response.json()

# Extract and print article titles, descriptions, and urls
for article in data.get('articles', []):
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print(f"URL: {article['url']}\n")
