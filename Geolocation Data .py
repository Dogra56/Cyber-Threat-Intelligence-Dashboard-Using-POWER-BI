import requests
import pandas as pd

ip_list = ['8.8.8.8', '1.1.1.1']  # replace with your real IPs

def get_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

geo_data = [get_geolocation(ip) for ip in ip_list]
df = pd.DataFrame(geo_data)
df.to_csv("ip_geolocation.csv", index=False)
