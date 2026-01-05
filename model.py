from sklearn.preprocessing import OrdinalEncoder

class ModelWithPreprocessing:
    def __init__(self, model):
        self.model = model
        self.encoder = OrdinalEncoder(
            handle_unknown="use_encoded_value",
            unknown_value=-1
        )

    def fit(self, X, y):
        X = X.copy()
        X[:, [0]] = self.encoder.fit_transform(X[:, [0]])
        self.model.fit(X, y)
        return self

    def predict(self, X):
        X = X.copy()
        X[:, [0]] = self.encoder.transform(X[:, [0]])
        return self.model.predict(X)
