from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import numpy as np
import joblib
from typing import List
import uvicorn

from model import RegressionModel,ClassificationModel
from schemas import PredictionInput, PredictionOutput, StudentOut
from db import get_db
from tables import Student, Academic, Performance


regressor = joblib.load("regressor.joblib")
classifier = joblib.load("classifier.joblib")

app = FastAPI(title="Student Final Score Predictor API")



@app.post("/predict", response_model=PredictionOutput)
def predict(input: PredictionInput, db: Session = Depends(get_db)):

    X_raw = np.array([[
        input.gender,
        input.attendance_percentage,
        input.study_hours_per_week,
        input.assignments_completed,
        input.previous_gpa
    ]], dtype=object)

    X_encoded = regressor.preprocess(X_raw, fit=False)
    X_encoded = X_encoded.astype(float)

    score_arr = regressor.model.predict(X_encoded).reshape(-1, 1)
    final_score = float(score_arr[0])

    X_classifier = np.hstack((X_encoded, score_arr))
    pass_status = int(classifier.predict_classifier(X_classifier)[0])

    try:
        student = Student(
            student_id=input.student_id,
            age=input.age,
            gender=input.gender,
            parent_education=input.parent_education
        )
        db.merge(student)
        db.flush()

        academic = Academic(
            student_id=input.student_id,
            attendance_percentage=input.attendance_percentage,
            study_hours_per_week=input.study_hours_per_week,
            previous_gpa=input.previous_gpa,
            assignments_completed=input.assignments_completed
        )
        db.merge(academic)

        performance = Performance(
            student_id=input.student_id,
            final_score=final_score,
            pass_status=pass_status
        )
        db.merge(performance)

        db.commit()

    except Exception:
        db.rollback()
        raise

    return {
        "student_id": input.student_id,
        "final_score": final_score,
        "pass_status": pass_status
    }


@app.get("/students", response_model=List[StudentOut])
def student_details(db: Session = Depends(get_db)):
    return db.query(Student).all()

if __name__ == "__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=4000,reload=True)