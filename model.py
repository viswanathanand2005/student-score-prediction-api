from sklearn.preprocessing import OrdinalEncoder
import numpy as np

class RegressionModel:
    def __init__(self, model):
        self.model = model
        self.encoder = OrdinalEncoder(
            handle_unknown="use_encoded_value",
            unknown_value=-1
        )

    def preprocess(self, X, fit=False):
        X = X.copy()
        if fit:
            X[:, [0]] = self.encoder.fit_transform(X[:, [0]])
        else:
            X[:, [0]] = self.encoder.transform(X[:, [0]])
        return X

    def fit_regressor(self, X, y):
        X_enc = self.preprocess(X, fit=True)
        self.model.fit(X_enc, y)
        return self

    def predict_regressor(self, X):
        X_enc = self.preprocess(X, fit=False)
        return self.model.predict(X)


class ClassificationModel:
    def __init__(self, model):
        self.model = model

    def fit_classifier(self, X, y):
        X = X.copy()
        self.model.fit(X, y)
        return self

    def predict_classifier(self, X):
        X = X.copy()
        return self.model.predict(X)
