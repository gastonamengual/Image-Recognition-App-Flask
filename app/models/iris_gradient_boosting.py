import numpy as np
from dataclasses import dataclass
from sklearn.ensemble import GradientBoostingClassifier

@dataclass()
class IrisGradientBoosting():

    model = GradientBoostingClassifier()

    def fit(self, X: np.array, y: np.array) -> GradientBoostingClassifier:
        return self.model.fit(X, y)

    def predict(self, X: np.array) -> np.array:
        return self.model.predict(X)

    