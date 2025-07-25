import requests
import json

ioc = "45.61.136.156"  # Replace with your actual IOC

url = "https://threatfox.abuse.ch/api/v1/"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "query": "search_ioc",
    "search_term": ioc
}

response = requests.post(url, headers=headers, data=data)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)

try:
    result = response.json()
    print("✅ JSON Response Parsed Successfully:")
    print(json.dumps(result, indent=4))
except json.JSONDecodeError as e:
    print("❌ JSON Decode Error:", e)
