import pandas as pd

file_path = r"C:\Users\Shaniya\Downloads\merge csv file.csv"

try:
    df = pd.read_csv(file_path, sep=',', encoding='utf-8', engine='python', on_bad_lines='skip')
    print("✅ File loaded successfully!")
    
    # Example: Create severity label
    def get_severity(row):
        try:
            detection_count = int(row.get("detection_count", 0))
            abuse_score = int(row.get("abuse_score", 0))
        except:
            return "Unknown"
        
        if detection_count > 20 or abuse_score > 80:
            return "High"
        elif detection_count > 5:
            return "Medium"
        else:
            return "Low"

    df["severity_label"] = df.apply(get_severity, axis=1)

    # Save the final labeled dataset
    df.to_csv("final_labeled_threat_data.csv", index=False)
    print("✅ Saved: final_labeled_threat_data.csv")

except Exception as e:
    print("❌ Error loading file:", e)
