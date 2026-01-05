# train.py

from model import ModelWithPreprocessing
from sklearn.linear_model import LinearRegression
from db_connection import df
import joblib

X = df[['gender','attendance_percentage',
        'study_hours_per_week','assignments_completed',
        'previous_gpa']].values
y = df['final_score'].values

model = ModelWithPreprocessing(LinearRegression())
model.fit(X, y)

joblib.dump(model, "model.joblib")
print("Saved model.joblib")
