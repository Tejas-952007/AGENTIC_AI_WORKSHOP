import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("gemini_api_key")
if api_key.startswith('"') and api_key.endswith('"'):
    api_key = api_key[1:-1]

model = "gemini-2.5-flash-lite"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
headers = {'Content-Type': 'application/json'}
data = {
    "contents": [{
        "parts": [{"text": "Hello, how are you?"}]
    }]
}

response = requests.post(url, headers=headers, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
