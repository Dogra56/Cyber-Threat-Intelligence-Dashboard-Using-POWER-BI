import pandas as pd

# Sample dataframe (replace this with your real 'ioc_data')
ioc_data = pd.read_csv("merged_ioc_data.csv")  # Or your real IOC CSV file

def explain_threat(row):
    explanation = []
    if row.get('abuse_score', 0) > 90:
        explanation.append("Highly abusive IP (AbuseIPDB)")
    if row.get('virus_total_score', 0) > 5:
        explanation.append("Detected by many AVs (VirusTotal)")
    if 'phishing' in str(row.get('tags', '')).lower():
        explanation.append("Tagged as phishing")
    if row.get('ttp', '') in ['T1059', 'T1071']:
        explanation.append("Mapped to MITRE TTP")
    return " | ".join(explanation)

# Apply the explanation logic
ioc_data['explanation'] = ioc_data.apply(explain_threat, axis=1)

# Save result to new file
ioc_data.to_csv("explained_threats.csv", index=False)

print("✅ Explanations added and saved to 'explained_threats.csv'")
