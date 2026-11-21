# Network Intrusion Detection System Using Machine Learning

## 📌 Project Overview

Network Intrusion Detection System (NIDS) is a Machine Learning-based project designed to identify malicious network traffic and distinguish it from normal network activities.

This project uses the **NSL-KDD dataset** to build a binary classification model that detects whether a network connection is normal or represents a potential cyberattack.

Four machine learning algorithms are implemented and compared to identify the best-performing model.

## 🎯 Project Objectives

- Detect suspicious network traffic using Machine Learning.
- Classify network connections into Normal and Attack categories.
- Compare different classification algorithms.
- Evaluate model performance using multiple evaluation metrics.
- Select the best-performing model for intrusion detection.

## 📊 Dataset

**Dataset:** NSL-KDD

The NSL-KDD dataset is a benchmark dataset used for network intrusion detection research.

| Dataset Information | Details |
|---|---|
| Training records | 125,973 |
| Testing records | 22,544 |
| Input features | 41 |
| Total columns | 42 |
| Problem type | Binary Classification |
| Target classes | Normal / Attack |

**Dataset Source:** [NSL-KDD Dataset](https://www.unb.ca/cic/datasets/nsl.html)

## 🛠️ Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## ⚙️ Project Workflow

1. Dataset Loading
2. Exploratory Data Analysis
3. Data Preprocessing
4. Categorical Feature Encoding
5. Numerical Feature Scaling
6. Machine Learning Model Training
7. Model Performance Evaluation
8. Model Comparison
9. Final Model Selection
10. Prediction and Model Saving

## 🤖 Machine Learning Algorithms

The following algorithms were implemented:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Support Vector Machine (SVM)
4. Random Forest

## 📈 Model Performance Comparison

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

### KNN Performance

K-Nearest Neighbors was selected as the final model based on its highest F1-score among the evaluated algorithms.

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 77.36% |
| Precision | 96.75% |
| Recall | 62.32% |
| F1-Score | 75.81% |
| ROC-AUC | 81.42% |

### Random Forest Performance

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 76.85% |
| Precision | 96.78% |
| Recall | 61.37% |
| F1-Score | 75.11% |
| ROC-AUC | 95.95% |

### Final Model Selection

KNN was selected because it achieved the highest F1-score of **75.81%**.

Although Random Forest achieved a higher ROC-AUC, KNN performed slightly better in F1-score, accuracy, and recall at the evaluated prediction threshold.

## 📂 Repository Structure

```text
Network-Intrusion-Detection/
│
├── NetworkIntrusionDetection.ipynb
├── model_comparison.csv
├── nsl_kdd_random_forest.pkl
├── KNN_Intrusion_Detection_Compressed.joblib
└── README.md
```

## 🚀 How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/anishgore78/Network-Intrusion-Detection.git
```

2. Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

3. Open the notebook using Google Colab or Jupyter Notebook.

4. Upload the NSL-KDD training and testing dataset files.

5. Execute the notebook cells to perform preprocessing, train models, and evaluate performance.

## 🔮 Future Enhancements

- Improve attack detection recall.
- Perform hyperparameter tuning for better performance.
- Experiment with advanced machine learning algorithms.
- Develop a web-based intrusion detection dashboard.
- Extend the system to identify individual attack categories.

## 📝 Conclusion

This project demonstrates the use of Machine Learning in cybersecurity for detecting malicious network traffic.

Four classification algorithms were implemented and compared using the NSL-KDD dataset. KNN achieved the highest F1-score of 75.81% and was selected as the final model.

The project provided practical experience in data preprocessing, model development, evaluation, and applying machine learning techniques to cybersecurity problems.

---

**Developed as a Machine Learning and Cybersecurity Project.**
