import json
import urllib.request
import urllib.error

import joblib
import pandas as pd
from pathlib import Path

# Load the trained model to get its exact feature order
model_path = Path(__file__).parent / "KNN_Intrusion_Detection_Compressed.joblib"
model = joblib.load(model_path)

feature_names = list(model.feature_names_in_)

# NSL-KDD dataset has 41 features + label + difficulty
columns = feature_names + ["label", "difficulty"]

# Read the dataset
df = pd.read_csv(
    "data/KDDTest+.txt",
    header=None,
    names=columns
)

# Select one genuine network traffic record
row = df.iloc[0]

# Convert the record into the API's expected format
categorical_features = ["protocol_type", "service", "flag"]

features = {}

for name in feature_names:
    if name in categorical_features:
        features[name] = str(row[name])
    else:
        features[name] = float(row[name])

# Actual dataset label
actual_label = str(row["label"]).strip().lower()
actual_class = "Normal" if actual_label == "normal" else "Attack"

# Prepare API request
payload = {
    "features": features
}

data = json.dumps(payload).encode("utf-8")

request = urllib.request.Request(
    "http://127.0.0.1:8000/predict",
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

# Send request and display results
print("\nNETWORK INTRUSION DETECTION TEST")
print("--------------------------------")

print("Total dataset records:", len(df))
print("Testing record number: 1")
print("Actual dataset label:", actual_class)

try:
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    print("\nAPI RESPONSE")
    print("--------------------------------")
    print("Predicted class:", result["class_label"])
    print("Message:", result["message"])

    print("\nCOMPARISON")
    print("--------------------------------")
    print("Actual:", actual_class)
    print("Predicted:", result["class_label"])

    if actual_class == result["class_label"]:
        print("Result: Correct prediction")
    else:
        print("Result: Incorrect prediction")

except urllib.error.HTTPError as error:
    print("API Error:", error.code)
    print(error.read().decode("utf-8"))

except Exception as error:
    print("Error:", error)