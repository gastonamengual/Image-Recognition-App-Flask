from flask import Blueprint, render_template

predictions_scope = Blueprint("predictions_views", __name__)


@predictions_scope.route("/")
@predictions_scope.route("/predict_flower/")
def predict_flower():
    return render_template("home.html")

@predictions_scope.route("/write_predicted_flower/<prediction>")
def write_predicted_flower(prediction: str):
    return render_template("home.html", prediction=prediction)