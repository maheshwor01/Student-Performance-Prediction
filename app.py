from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("model/student_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    hours = float(request.form["Hours_Studied"])
    attendance = float(request.form["Attendance"])
    parental = float(request.form["Parental_Involvement"])
    resources = float(request.form["Access_to_Resources"])
    extracurricular = float(request.form["Extracurricular_Activities"])
    sleep = float(request.form["Sleep_Hours"])
    previous = float(request.form["Previous_Scores"])
    motivation = float(request.form["Motivation_Level"])
    internet = float(request.form["Internet_Access"])
    tutoring = float(request.form["Tutoring_Sessions"])
    income = float(request.form["Family_Income"])
    teacher = float(request.form["Teacher_Quality"])
    school = float(request.form["School_Type"])
    peer = float(request.form["Peer_Influence"])
    physical = float(request.form["Physical_Activity"])
    disability = float(request.form["Learning_Disabilities"])
    education = float(request.form["Parental_Education_Level"])
    distance = float(request.form["Distance_from_Home"])
    gender = float(request.form["Gender"])

    features = [[
        hours,
        attendance,
        parental,
        resources,
        extracurricular,
        sleep,
        previous,
        motivation,
        internet,
        tutoring,
        income,
        teacher,
        school,
        peer,
        physical,
        disability,
        education,
        distance,
        gender
    ]]

    prediction = model.predict(features)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Exam Score: {prediction[0]:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)