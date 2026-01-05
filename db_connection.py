import pandas as pd
import os
from dotenv import load_dotenv
import mysql.connector

#Loading the environment variables
load_dotenv()

#Creating a connection to the db
conn = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    database = os.getenv("DB")
)

query = """
    SELECT s.student_id,s.age,s.gender,s.parent_education,
    a.attendance_percentage,a.study_hours_per_week,a.assignments_completed,a.previous_gpa,
    p.final_score,p.pass
    FROM STUDENTS s JOIN academic a ON s.student_id = a.student_id
    JOIN performance p ON s.student_id = p.student_id
"""

#Creating a dataframe
df = pd.read_sql(query,conn)
print(df)