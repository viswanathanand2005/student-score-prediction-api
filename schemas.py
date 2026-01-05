from pydantic import BaseModel,Field

class PredictionInput(BaseModel):
    student_id: int = Field(...,example=101)
    age: int = Field(...,example=20)
    gender: str = Field(...,example='Male')
    parent_education: str = Field(...,example='Bachelor')
    attendance_percentage: float = Field(...,example=90.00)
    study_hours_per_week: float = Field(...,example=12.1)
    previous_gpa: float = Field(...,example=3.45)
    assignments_completed: bool = Field(...,example=False)

class PredictionOutput(BaseModel):
    student_id: int
    final_score: float
    pass_status: bool

class StudentOut(BaseModel):
    student_id: int
    age: int
    gender: str
    parent_education: str

    class Config:
        from_attributes = True