import requests
import json

# ✅ Replace with your actual API key
API_KEY = '77EA5BD6-0163-F011-835D-0EBF96DE670D'

# 🔍 Sample Query: Fetch CVEs related to "Apache"
url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
params = {
    'keywordSearch': 'apache',  # You can change to windows, linux, etc.
    'resultsPerPage': 10        # Number of CVEs to fetch
}

headers = {
    'apiKey': API_KEY
}

response = requests.get(url, headers=headers, params=params)

# ✅ Save result to JSON file
data = response.json()
with open('nvd_cves_output.json', 'w') as f:
    json.dump(data, f, indent=4)

print("✅ NVD CVEs data saved to nvd_cves_output.json")
