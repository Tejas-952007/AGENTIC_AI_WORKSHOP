import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("gemini_api_key")
if api_key.startswith('"') and api_key.endswith('"'):
    api_key = api_key[1:-1]

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
response = requests.get(url)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
