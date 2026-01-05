from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import numpy as np
import joblib
from typing import List

from model import ModelWithPreprocessing  
from schemas import PredictionInput, PredictionOutput, StudentOut
from db import get_db
from tables import Student, Academic, Performance


model = joblib.load("model.joblib")

app = FastAPI(title="Student Final Score Predictor API")

def create_input_arr(input):
    return np.array([[
        input.gender,
        input.attendance_percentage,
        input.study_hours_per_week,
        input.assignments_completed,
        input.previous_gpa
    ]], dtype=object)

@app.post("/predict", response_model=PredictionOutput)
def predict(input: PredictionInput, db: Session = Depends(get_db)):

    X = create_input_arr(input)
    final_score = float(model.predict(X)[0])

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
            final_score=final_score
        )
        db.merge(performance)

        db.commit()
    except Exception:
        db.rollback()
        raise

    return {
        "student_id": input.student_id,
        "final_score": final_score
    }

@app.get("/students", response_model=List[StudentOut])
def student_details(db: Session = Depends(get_db)):
    return db.query(Student).all()
