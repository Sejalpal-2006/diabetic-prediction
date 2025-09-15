# 🩺 Diabetes Prediction Model using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange)
![Streamlit](https://img.shields.io/badge/WebApp-Streamlit-brightgreen)

---

## 📖 Project Overview
This project predicts the likelihood of diabetes in patients based on various medical attributes such as glucose level, BMI, blood pressure, insulin level, and age.  
The model is built using **machine learning algorithms** and can assist in **early detection of diabetes risk**.

---

## 📊 Dataset
- **Name:** Pima Indians Diabetes Dataset  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  
- **Features:** Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age  
- **Target:** 0 = Non-Diabetic, 1 = Diabetic  

---

## 🛠️ Technologies Used
- **Programming Language: Python  
- **Libraries: Pandas, NumPy, Matplotlib, Seaborn, scikit-learn  
- **Deployment (optional): Streamlit   

---

 🚀 Usage
Input patient details: Glucose, Blood Pressure, BMI, Insulin, Age, etc.
The model outputs:
0 → Non-Diabetic
1 → Diabetic

🤖 Model Training & Evaluation
Algorithms used: SVM & its hyperparameter
Best performing model: Random Forest
Accuracy Achieved: 78%
Evaluation Metrics: Confusion Matrix, Precision, Recall, F1-score

📈 Results
Feature importance analysis
ROC curve & Confusion Matrix
Example prediction:
Input: Glucose=120, BMI=32, Age=45 → Prediction: Diabetic ✅

🔮 Future Improvements
Add more medical data for better accuracy
Implement deep learning (ANN)
Deploy model to cloud (AWS / Heroku / GCP)
Build a mobile-friendly UI

👩‍💻 Contributors
Sejal Pal
