
from pathlib import Path
from typing import Any
import math

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Load the trained KNN pipeline
MODEL_PATH = (
    Path(__file__).parent /
    "KNN_Intrusion_Detection_Compressed.joblib"
)

model = joblib.load(MODEL_PATH)

# Get the exact feature order from the saved model
FEATURE_NAMES = list(model.feature_names_in_)

# Categorical features
CATEGORICAL_FEATURES = [
    "protocol_type",
    "service",
    "flag"
]

# Remaining features are numerical
NUMERIC_FEATURES = [
    feature for feature in FEATURE_NAMES
    if feature not in CATEGORICAL_FEATURES
]


# Create FastAPI application
app = FastAPI(
    title="Network Intrusion Detection API",
    description="ML-based network traffic classification using KNN",
    version="1.0.0"
)


# Request structure
class PredictionRequest(BaseModel):
    features: dict[str, Any]


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Network Intrusion Detection API is running"
    }


# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "KNN"
    }


# Prediction endpoint
@app.post("/predict")
def predict(request: PredictionRequest):

    features = request.features

    # Check missing features
    missing = set(FEATURE_NAMES) - set(features.keys())

    # Check unexpected features
    extra = set(features.keys()) - set(FEATURE_NAMES)

    if missing or extra:
        raise HTTPException(
            status_code=422,
            detail={
                "missing_features": sorted(missing),
                "unexpected_features": sorted(extra)
            }
        )

    # Validate categorical features
    for feature in CATEGORICAL_FEATURES:

        if not isinstance(features[feature], str):
            raise HTTPException(
                status_code=422,
                detail=f"{feature} must be a string"
            )

    # Validate numerical features
    for feature in NUMERIC_FEATURES:

        try:
            value = float(features[feature])

            if not math.isfinite(value):
                raise ValueError("Value must be finite")

            features[feature] = value

        except (TypeError, ValueError):
            raise HTTPException(
                status_code=422,
                detail=f"{feature} must be a valid finite number"
            )

    # Create DataFrame in correct feature order
    input_data = pd.DataFrame(
        [features],
        columns=FEATURE_NAMES
    )

    # Make prediction
    try:
        prediction = int(model.predict(input_data)[0])

    except (ValueError, TypeError) as error:
        raise HTTPException(
            status_code=422,
            detail=f"Prediction failed: {str(error)}"
        )

    # Convert prediction into readable output
    if prediction == 1:
        label = "Attack"
        message = "Potential malicious network traffic detected"

    else:
        label = "Normal"
        message = "Normal network traffic detected"

    return {
        "prediction": prediction,
        "class_label": label,
        "message": message
    }
