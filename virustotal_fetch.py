import requests
import json

# ✅ Your VirusTotal API Key
API_KEY = '38bb37f1f3d3ae90a0ae93c77364957884e9fa1a5678b7915d3db48fb5fc9d1d'

# 🔍 IP Address to check
ip_address = '8.8.8.8'  # Change karo if needed

# 🔗 API URL
url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"

# 📩 Headers
headers = {
    "x-apikey": API_KEY
}

# 📡 API Request
response = requests.get(url, headers=headers)

# ✅ Save JSON response to file
data = response.json()
with open('virustotal_output.json', 'w') as f:
    json.dump(data, f, indent=4)

print("✅ VirusTotal data saved to virustotal_output.json")
