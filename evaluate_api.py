
import requests
import joblib
import pandas as pd
from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
from time import time

# Load model to obtain exact feature names
model = joblib.load(
    Path(__file__).parent / "KNN_Intrusion_Detection_Compressed.joblib"
)

feature_names = list(model.feature_names_in_)
categorical_features = ["protocol_type", "service", "flag"]

# Read NSL-KDD test dataset
columns = feature_names + ["label", "difficulty"]

df = pd.read_csv(
    "data/KDDTest+.txt",
    header=None,
    names=columns
)

# Convert actual labels: 0 = Normal, 1 = Attack
y_true = (
    df["label"].astype(str).str.strip().str.lower() != "normal"
).astype(int)

predictions = []

print("Starting API evaluation...")
print("Total records:", len(df))

start_time = time()

# Send records to FastAPI in batches
batch_size = 100

for start in range(0, len(df), batch_size):
    batch = df.iloc[start:start + batch_size]

    payload = []

    for _, row in batch.iterrows():
        features = {}

        for name in feature_names:
            if name in categorical_features:
                features[name] = str(row[name])
            else:
                features[name] = float(row[name])

        payload.append({"features": features})

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload[0] if len(payload) == 1 else None,
            timeout=30
        )

        # Current API accepts one record per request.
        # Send the remaining records individually.
        if len(payload) == 1:
            response.raise_for_status()
            predictions.append(response.json()["prediction"])
        else:
            for item in payload:
                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json=item,
                    timeout=30
                )
                response.raise_for_status()
                predictions.append(response.json()["prediction"])

    except requests.RequestException as error:
        print("API request failed:", error)
        raise

    completed = min(start + len(batch), len(df))
    print(f"Processed {completed}/{len(df)} records")

# Calculate metrics
elapsed = time() - start_time

print("\nMODEL EVALUATION RESULTS")
print("========================")

print("Accuracy :", accuracy_score(y_true, predictions))
print("Precision:", precision_score(y_true, predictions, zero_division=0))
print("Recall   :", recall_score(y_true, predictions, zero_division=0))
print("F1 Score :", f1_score(y_true, predictions, zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, predictions))

print("\nClassification Report:")
print(classification_report(
    y_true,
    predictions,
    target_names=["Normal", "Attack"],
    zero_division=0
))

print(f"\nEvaluation time: {elapsed:.2f} seconds")
