from werkzeug.datastructures import ImmutableMultiDict
import numpy as np

from sklearn.datasets import load_iris

from app.models.iris_gradient_boosting import IrisGradientBoosting


def predict(data: ImmutableMultiDict[str, float]) -> str:

    X, y = load_iris(return_X_y=True)
    model = IrisGradientBoosting()
    model = model.fit(X, y)

    X = np.array(list(data.to_dict(flat=True).values())).reshape(1, -1)
    y_pred_int = model.predict(X)[0]

    y_pred = np.choose(y_pred_int, ["Setosa", "Versicolor", "Virginica"])

    return y_pred
