import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# ✅ Step 1: Load CSV file
try:
    file_path = r"C:\Users\Shaniya\Downloads\final_labeled_threat_data.csv"
    df = pd.read_csv(file_path)
    print("✅ File Loaded Successfully!")
except Exception as e:
    print(f"❌ Error loading file: {e}")
    exit()

# ✅ Step 2: Show columns for verification
print("\n📌 Columns in dataset:", df.columns.tolist())
print(df.head())

# ✅ Step 3: Prepare your data
# Check if the correct column is present (e.g., 'severity_label')
if 'severity_label' not in df.columns:
    print("❌ Column 'severity_label' not found in file.")
    exit()

label_map = {'Low': 0, 'Medium': 1, 'High': 2}
df['label_encoded'] = df['severity_label'].map(label_map)

# Only keeping numeric features (update if needed)
X = df.select_dtypes(include=['int64', 'float64']).drop('label_encoded', axis=1, errors='ignore')
y = df['label_encoded']

# ✅ Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Step 5: Train Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ Step 6: Predict & Evaluate
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Step 7: Save model (optional)
import joblib
joblib.dump(model, 'threat_severity_model.pkl')
print("\n✅ Model Saved as threat_severity_model.pkl")
