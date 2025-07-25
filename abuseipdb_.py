import requests
import json

API_KEY = 'caa0b9123a2ec594f8af47ea926f25cc80864981eb5ef2971908a909e8c323ccaed77847edfff153'
ip = "8.8.8.8"

url = "https://api.abuseipdb.com/api/v2/check"
querystring = {
    "ipAddress": ip,
    "maxAgeInDays": "90"
}

headers = {
    "Accept": "application/json",
    "Key": API_KEY
}

response = requests.request(method="GET", url=url, headers=headers, params=querystring)

# Handle response safely
try:
    data = response.json()

    # Save output
    with open('abuseipdb_output.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("✅ AbuseIPDB data saved to 'abuseipdb_output.json'")

except Exception as e:
    print("❌ Error parsing response:", e)
    print("Raw response:", response.text)
