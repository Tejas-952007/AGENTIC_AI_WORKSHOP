import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("gemini_api_key")
# Remove quotes if they are literal
if api_key.startswith('"') and api_key.endswith('"'):
    api_key = api_key[1:-1]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
headers = {'Content-Type': 'application/json'}
data = {
    "contents": [{
        "parts": [{"text": "Hello, how are you?"}]
    }]
}

response = requests.post(url, headers=headers, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
