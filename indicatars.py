import pandas as pd

# Static count values
data = {
    'Indicator': ['IPs', 'Domains', 'Hashes', 'URLs', 'Files', 'Emails'],
    'Count': [5000, 3500, 1500, 1200, 950, 950]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("indicator_counts.csv", index=False)

print("✅ indicator_counts.csv created successfully!")
