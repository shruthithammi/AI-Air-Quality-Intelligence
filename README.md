# 🌿 AI Air Quality Intelligence

An end-to-end **Machine Learning project** that predicts the **Air Quality Index (AQI)** using India's air pollution dataset and provides health recommendations through an interactive **Streamlit dashboard**.

---

## 📌 Project Overview

Air pollution has become one of the biggest environmental challenges in India. This project uses historical air quality data to predict AQI based on pollutant concentrations and engineered temporal features such as city, season, and day of the week.

The project follows a complete Machine Learning workflow—from data cleaning and exploratory data analysis to model training and deployment.

---

## 🎯 Problem Statement

Predict the **Air Quality Index (AQI)** using pollutant measurements collected from different Indian cities and classify the predicted AQI into meaningful air quality categories.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Plotly
* Streamlit
* Joblib

---

## 📂 Project Structure

```text
AI-Air-Quality-Intelligence/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
├── models/
├── notebooks/
└── src/
```

---

## 📊 Dataset

* **Dataset:** Air Quality Data in India
* **Source:** Kaggle
* **Cities Covered:** Hyderabad, Delhi, Bengaluru, Mumbai, Kolkata and other Indian cities.
* **Target Variable:** AQI

### Features Used

* PM2.5
* PM10
* NO
* NO₂
* NOx
* NH₃
* CO
* SO₂
* O₃
* Benzene
* Toluene
* Year
* Month
* Day
* City (Encoded)
* Season (Encoded)
* Day of Week (Encoded)

---

## 🔍 Machine Learning Workflow

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Streamlit Deployment

---

## 🤖 Models Implemented

| Model                       | Purpose                |
| --------------------------- | ---------------------- |
| Linear Regression           | Baseline model         |
| Decision Tree Regressor     | Tree-based regression  |
| Random Forest Regressor     | Final selected model   |
| Gradient Boosting Regressor | Performance comparison |

### ✅ Best Model

**Random Forest Regressor**

Performance Metrics:

* R² Score: **0.91**
* MAE: **20.46**
* RMSE: **39.96**

Random Forest achieved the best performance among all trained models.

---

## 🌐 Streamlit Application Features

* Predict AQI from pollutant values.
* AQI category classification.
* Health recommendations based on AQI.
* Interactive user interface.
* City and seasonal inputs.

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/shruthithammi/AI-Air-Quality-Intelligence.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---


🎥 Project Demo
<img width="1907" height="1060" alt="Animation" src="https://github.com/user-attachments/assets/79842b7b-9079-4887-8c74-331964d35a99" />




## 💡 Future Improvements
* AQI Gauge Visualization.
* Live AQI API Integration.
* City-wise AQI Trend Dashboard.
* AQI Forecasting using Time Series Models.
* Cloud Deployment.

---

## 👩‍💻 Author

**Shruthi Thammi**

B.Tech Computer Science Engineering

Machine Learning & AI Enthusiast

Open to AI / ML Engineer, Data Science and Python Developer opportunities.
