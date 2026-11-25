# 🛡️ Network Intrusion Detection System

An AI-powered Network Intrusion Detection System that uses Machine Learning to classify network traffic as **Normal** or **Attack**. Built using Python, Scikit-learn, FastAPI, and Streamlit.

## 🚀 Project Overview

Network security is an important aspect of modern computing. This project uses a K-Nearest Neighbors (KNN) classification model to identify potentially malicious network traffic based on network connection features.

The application provides an interactive dashboard where users can enter network traffic details and receive predictions through a deployed REST API.

## ✨ Features

- Machine Learning-based network traffic classification.
- Binary classification: Normal and Attack.
- 41 network traffic input features.
- Data preprocessing using StandardScaler and OneHotEncoder.
- Interactive Streamlit dashboard with a professional light theme.
- FastAPI REST API for model predictions.
- Cloud deployment using Render and Streamlit Community Cloud.
- API health-check endpoint.

## 🧠 Machine Learning Model

The project uses the **K-Nearest Neighbors (KNN)** algorithm.

Dataset: NSL-KDD

The model pipeline includes:
- StandardScaler for numerical features.
- OneHotEncoder for categorical features.
- K-Nearest Neighbors classifier for prediction.

### Model Performance

| Evaluation Metric | KNN |
|---|---:|
| Accuracy | 77.36% |
| Precision | 96.75% |
| Recall | 62.32% |
| F1-Score | 75.81% |
| ROC-AUC | 81.42% |

The KNN model was selected based on its F1-score among the evaluated models.

**Note:** The model is an experimental prototype. It can miss malicious traffic and should not be used as a standalone production security solution.

## 🏗️ System Architecture

```text
        User
         |
         v
  Streamlit Dashboard
         |
         v
    FastAPI REST API
         |
         v
  Data Preprocessing
         |
         v
   KNN Classification
         |
         v
   Prediction Result
     /          \
  Normal       Attack
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Joblib | Model serialization |
| FastAPI | Backend API |
| Uvicorn | API server |
| Streamlit | Interactive frontend |
| Git & GitHub | Version control |
| Render | Backend deployment |
| Streamlit Cloud | Frontend deployment |

## 📂 Project Structure

```text
Network-Intrusion-Detection/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── KNN_Intrusion_Detection_Compressed.joblib
│
├── model_comparison.csv
│
└── NetworkIntrusionDetection.ipynb
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/anishgore78/Network-Intrusion-Detection.git
```

### 2. Navigate to the project folder

```bash
cd Network-Intrusion-Detection
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the environment

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
pip install streamlit requests
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

The Streamlit frontend connects to the deployed FastAPI backend.

## 🌐 Live Deployment


## 🌐 Live Deployment

- **Live Application (Frontend):** (https://anishgore78-network-intrusion-detection-app-zugjep.streamlit.app/)
- **Backend API (Render):** https://network-intrusion-detection-0hoe.onrender.com
- **API Documentation:** [Swagger UI](https://network-intrusion-detection-0hoe.onrender.com/docs)
- **API Health Check:** [Health Status](https://network-intrusion-detection-0hoe.onrender.com/health)


## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Backend health status |
| POST | `/predict` | Predict network traffic class |

## 🔮 Future Improvements

- Real-time network traffic monitoring.
- Integration with live network packet capture.
- Improved attack detection and recall.
- Additional machine learning model comparisons.
- Interactive prediction history and analytics.
- Advanced threat visualization.

## 👨‍💻 Author

**Anish Gore**

Artificial Intelligence and Data Science Engineering Student

[GitHub](https://github.com/anishgore78)

---

⭐ If you find this project interesting, feel free to explore the repository!

**Disclaimer:** This project is developed for educational and experimental purposes. Predictions are not a substitute for professional network security monitoring.

