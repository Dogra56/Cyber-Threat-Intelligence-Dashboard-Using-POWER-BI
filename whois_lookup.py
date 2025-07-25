import requests

# ✅ Your API Key
api_key = 'at_CIxsglVUadLldIy94dPQpRnGZoJnb'
domain = 'google.com'  # 👈 Change this to any domain you want

# WHOIS API URL
url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService"

# Parameters for the API request
params = {
    "apiKey": api_key,
    "domainName": domain,
    "outputFormat": "JSON"
}

# Make the request
response = requests.get(url, params=params)

# Show response status
print(f"Status Code: {response.status_code}")

# Parse and print WHOIS data
try:
    data = response.json()
    print("\n📄 WHOIS Info:")
    print(f"Domain Name     : {data['WhoisRecord']['domainName']}")
    print(f"Created Date    : {data['WhoisRecord']['createdDate']}")
    print(f"Updated Date    : {data['WhoisRecord']['updatedDate']}")
    print(f"Registrar       : {data['WhoisRecord']['registrarName']}")
    print(f"Registrant Email: {data['WhoisRecord'].get('contactEmail', 'N/A')}")
except Exception as e:
    print("\n❌ Error parsing response:", e)
    print("🔻 Raw Response:")
    print(response.text)
import requests
import csv

api_key = 'at_CIxsglVUadLldIy94dPQpRnGZoJnb'
domain = "google.com"

url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService"
params = {
    "apiKey": api_key,
    "domainName": domain,
    "outputFormat": "JSON"
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()

    whois_data = data.get("WhoisRecord", {})
    result = {
        "Domain Name": whois_data.get("domainName", ""),
        "Created Date": whois_data.get("createdDate", ""),
        "Updated Date": whois_data.get("updatedDate", ""),
        "Registrar": whois_data.get("registrarName", ""),
        "Registrant Email": whois_data.get("contactEmail", "")
    }

    # ✅ Save to CSV
    with open("whois_output.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=result.keys())
        writer.writeheader()
        writer.writerow(result)

    print("✅ Saved to whois_output.csv")

else:
    print("❌ Error:", response.status_code)
