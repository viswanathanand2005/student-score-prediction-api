# 🎓 Student Final Score Prediction System

## 🧾 Overview

This project implements an end-to-end **Machine Learning–powered prediction system** that estimates a student’s **final academic score** based on demographic and academic factors.  
The system exposes the trained model through a **REST API** and persistently stores prediction-related data in a **relational database**.

The project demonstrates how a machine learning model can be taken beyond experimentation and integrated into a **production-style backend system**.

---

## 📁 Dataset Description

The model is trained on structured student data collected across three related entities:

- **students**
  - Demographic information such as age, gender, and parental education

- **academic**
  - Academic indicators including attendance percentage, study hours, previous GPA, and assignment completion status

- **performance**
  - Final academic outcomes used as the prediction target

The data is stored in a **normalized MySQL database** and joined during training to form the model input.

---

## 🎯 Objectives

- Build a regression model to predict student final scores
- Integrate preprocessing directly with the trained model
- Expose predictions through a RESTful API
- Persist inputs and predictions in a relational database
- Maintain data integrity using foreign-key constraints
- Demonstrate real-world ML system design beyond notebooks

---

## ⚙️ Running the Project

### 1️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   

```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Configure environment variables
```bash
HOST=localhost
PORT=3306
USER=root
PASSWORD=your_mysql_password
DB=ml_project
```
### 4️⃣ Train the model
```bash
python train.py
```
This generates the serialized model file:
model.joblib

### 5️⃣ Start the API server
```bash
python -m uvicorn main:app --reload
```
- The API will be available at: http://127.0.0.1:8000/docs

## 🧪 System Workflow

### ✔ Data Handling
- Data fetched from a relational MySQL database
- Proper joins across multiple tables
- Feature selection and type handling for model training

### ✔ Model Development
- Regression-based predictive modeling
- Categorical feature encoding
- Model serialization using Joblib

### ✔ API Integration
- FastAPI-based inference endpoint
- Input validation using Pydantic schemas
- Transaction-safe database inserts

---

## 🔍 Key Observations

- Academic factors such as **attendance, prior GPA, and study hours** strongly influence final score predictions.
- Categorical attributes (e.g., gender) require careful preprocessing for stable model performance.
- Enforcing database constraints ensures consistency between demographic, academic, and performance records.
- Separating training, inference, and persistence logic improves system reliability and maintainability.

---

## 🛠 Tools & Technologies

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **MySQL**
- **scikit-learn**
- **Pandas & NumPy**
- **Joblib**
- **Pydantic**
- **Uvicorn**

---

## 🚀 Future Work

- Model performance evaluation and monitoring
- Batch prediction support
- Automated retraining pipeline
- CI/CD integration for deployment
- Feature importance and explainability analysis

---

## 📌 Conclusion

This project showcases a practical approach to deploying a machine learning model as a backend service.  
By combining model training, API-based inference, and relational data persistence, it highlights the skills required to build **production-ready ML systems**.

The system serves as a strong portfolio example of applied machine learning engineering.
