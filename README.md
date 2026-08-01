# 🎓 Student Performance Prediction using Machine Learning

A Machine Learning web application that predicts a student's exam score based on various academic, personal, and environmental factors.

## 📌 Project Overview

This project uses a (Linear Regression model) to predict a student's (Exam Score) using features such as:

- Hours Studied
- Attendance
- Previous Scores
- Motivation Level
- Family Income
- Teacher Quality
- Internet Access
- Sleep Hours
- Physical Activity
- Gender
- And more...

The trained model is deployed using **Flask** with a simple and user-friendly web interface.


## 🚀 Features

- 📊 Student performance prediction
- 🤖 Machine Learning model using Linear Regression
- 📁 Data preprocessing and label encoding
- 📈 Model evaluation using MAE, MSE, and R² Score
- 🌐 Flask web application
- 🎨 Responsive user interface using HTML, CSS, and Bootstrap


## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Web Development
- Flask
- HTML
- CSS
- Bootstrap
- JavaScript


## 📂 Project Structure

```
Student_Prediction_Project/
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── model/
│   └── student_model.pkl
│
├── notebook/
│   └── Student_Performance.ipynb
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```


## 📊 Machine Learning Workflow

1. Import Libraries
2. Load Dataset
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Label Encoding
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Save Model
10. Flask Deployment



## 📈 Model Performance

| Metric | Value |
|--------|------:|
| Mean Absolute Error (MAE) | 1.02 |
| Mean Squared Error (MSE) | 4.40 |
| R² Score | 0.689 |


## ▶️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/maheshwor01/Student-Performance-Prediction.git
```

### Move into the project folder

```bash
cd Student-Performance-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Project Screenshot

(Add a screenshot of your web application here.)

---

## 📚 Dataset

**StudentPerformanceFactors.csv**

Target Variable:
- Exam_Score

---

## 👨‍💻 Author

**Mahesh Mandal**

BSc Information Technology (IT) Student

---

## ⭐ Future Improvements

- Add Random Forest and XGBoost models
- Improve prediction accuracy
- Interactive dashboard
- User authentication
- Cloud deployment
- Data visualization charts

---

## 📄 License

This project is developed for educational and portfolio purposes.