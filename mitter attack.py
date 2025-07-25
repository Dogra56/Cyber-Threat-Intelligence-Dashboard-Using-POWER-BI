import pandas as pd

# Sample MITRE ATT&CK TTP data
data = [
    {"Tactic": "Initial Access", "Technique Name": "Spearphishing Attachment", "Technique ID": "T1566.001"},
    {"Tactic": "Initial Access", "Technique Name": "Drive-by Compromise", "Technique ID": "T1189"},
    {"Tactic": "Execution", "Technique Name": "PowerShell", "Technique ID": "T1059.001"},
    {"Tactic": "Persistence", "Technique Name": "Registry Run Keys", "Technique ID": "T1547.001"},
    {"Tactic": "Privilege Escalation", "Technique Name": "Exploitation for Privilege Escalation", "Technique ID": "T1068"},
    {"Tactic": "Defense Evasion", "Technique Name": "Obfuscated Files or Information", "Technique ID": "T1027"},
    {"Tactic": "Credential Access", "Technique Name": "Credential Dumping", "Technique ID": "T1003"},
    {"Tactic": "Discovery", "Technique Name": "System Information Discovery", "Technique ID": "T1082"},
    {"Tactic": "Lateral Movement", "Technique Name": "Remote Services", "Technique ID": "T1021"},
    {"Tactic": "Collection", "Technique Name": "Data Staged", "Technique ID": "T1074"},
    {"Tactic": "Command and Control", "Technique Name": "Application Layer Protocol", "Technique ID": "T1071"},
    {"Tactic": "Exfiltration", "Technique Name": "Exfiltration Over C2 Channel", "Technique ID": "T1041"},
    {"Tactic": "Impact", "Technique Name": "Data Destruction", "Technique ID": "T1485"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Export to Excel
df.to_excel("mitre_attack_output.xlsx", index=False)

print("✅ mitre_attack_output.xlsx file generated successfully!")
