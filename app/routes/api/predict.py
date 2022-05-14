from flask import Blueprint, redirect, request, url_for

from ...controllers import predictions_controller

predictions_scope = Blueprint("predictions_api", __name__, url_prefix="/predictions")


@predictions_scope.post("/predict")
def predict():
    data = request.form

    prediction = predictions_controller.predict(data)

    return redirect(
        url_for("views.predictions_views.write_predicted_flower", prediction=prediction)
    )
