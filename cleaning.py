import pandas as pd

# Load each file
vt = pd.read_excel('virustotal_cleaned_single_output.xlsx')
abuse = pd.read_csv('abuseipdb_cleaned.csv')
geo = pd.read_csv('ip_geolocation.csv')
attack = pd.read_csv('attack_patterns_cleaned.csv')

# Check columns
print(vt.columns)
print(abuse.columns)
print(geo.columns)
print(attack.columns)

