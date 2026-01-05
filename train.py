import numpy as np
from model import RegressionModel, ClassificationModel
from sklearn.linear_model import LinearRegression, LogisticRegression
from db_connection import df
import joblib

X = df[['gender',
        'attendance_percentage',
        'study_hours_per_week',
        'assignments_completed',
        'previous_gpa']].values

y_score = df['final_score'].values
y_pass = df['pass'].values


regressor = RegressionModel(LinearRegression())
regressor.fit_regressor(X, y_score)

X_encoded = regressor.preprocess(X, fit=False)


predicted_score = regressor.model.predict(X_encoded).reshape(-1, 1)


X_classifier = np.hstack((X_encoded, predicted_score))

classifier = ClassificationModel(LogisticRegression(max_iter=1000))
classifier.fit_classifier(X_classifier, y_pass)


joblib.dump(regressor, "regressor.joblib")
joblib.dump(classifier, "classifier.joblib")

print("Saved both models successfully")
