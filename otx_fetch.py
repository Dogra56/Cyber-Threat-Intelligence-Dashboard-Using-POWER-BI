import requests
import pandas as pd

# ✅ Your OTX API Key
api_key = "16ab1f7591b292be468adb2d04d6a2eaf5097b4e8d19fe694bc45270f4061a15"
headers = {
    "X-OTX-API-KEY": api_key
}

# ✅ Replace this with any domain, IP or hash you want to test
indicator_type = "domain"   # other options: "IPv4", "file", etc.
indicator_value = "google.com"

# ✅ API URL
url = f"https://otx.alienvault.com/api/v1/indicators/{indicator_type}/{indicator_value}/general"

# ✅ Request and Response Handling
response = requests.get(url, headers=headers)

# ✅ Save Output to CSV
if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data)
    df.to_csv("otx_output.csv", index=False)
    print("✅ Data saved to otx_output.csv")
else:
    print("❌ Error:", response.status_code, response.text)
