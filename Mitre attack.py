import os
import json

folder_path = 'D:/capstone project/otx_fetch.py/cti/enterprise-attack/attack-pattern'

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            # Parse objects inside JSON bundle
            for obj in data.get('objects', []):
                if obj.get('type') == 'attack-pattern':
                    print(obj.get('name'), obj.get('id'))
import csv

with open('attack_patterns.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Attack Pattern ID'])  # Header

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for obj in data.get('objects', []):
                    if obj.get('type') == 'attack-pattern':
                        writer.writerow([obj.get('name'), obj.get('id')])
df = pd.DataFrame(data)

# Export to Excel
df.to_excel("mitre_attack_output.xlsx", index=False)

print("✅ mitre_attack_output.xlsx file generated successfully!")
