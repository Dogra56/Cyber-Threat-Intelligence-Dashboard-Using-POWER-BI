import pandas as pd

# Correct full path to your file
file_path = r'D:\capstone project\otx_fetch.py\attack_patterns_cleaned.csv'

# Load the CSV
df = pd.read_csv(file_path)

# Show top 5 rows (optional)
print("✅ File loaded successfully!")
print(df.head())
# Basic rule-based severity mapping using keywords
def assign_severity(name):
    name = name.lower()
    if 'inject' in name or 'bypass' in name or 'persistence' in name:
        return 'High'
    elif 'schedule' in name or 'archive' in name:
        return 'Medium'
    else:
        return 'Low'

# Apply on your DataFrame
df['severity'] = df['Name'].apply(assign_severity)
label_map = {'Low': 0, 'Medium': 1, 'High': 2}
df['label_encoded'] = df['severity'].map(label_map)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# For simplicity, let’s use length of Name as a feature
df['name_length'] = df['Name'].apply(len)

X = df[['name_length']]  # features
y = df['label_encoded']  # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))
import joblib
joblib.dump(model, 'threat_severity_model.pkl')
df.to_csv('attack_patterns_with_severity.csv', index=False)
print("✅ Final CSV saved as attack_patterns_with_severity.csv")
