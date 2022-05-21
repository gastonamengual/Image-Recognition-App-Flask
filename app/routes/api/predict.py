from flask import Blueprint, redirect, request, url_for, flash
from ...controllers import predictions_controller

predictions_scope = Blueprint("predictions_api", __name__, url_prefix="/predictions")

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@predictions_scope.post("/predict")
def predict():

    if "image" not in request.files:
        flash("No image was uploaded")
        return redirect(request.url)

    image = request.files["image"]

    if image.filename == "":
        flash("No image selected for uploading")
        return redirect(url_for("views.predictions_views.predict_flower"))

    if not allowed_file(image.filename):
        flash("Allowed image types are png, jpg, and jpeg")
        return redirect(url_for("views.predictions_views.predict_flower"))

    prediction = predictions_controller.predict(image)

    return redirect(
        url_for("views.predictions_views.write_predicted_flower", prediction=prediction)
    )

    # data = request.form

    # return redirect(
    #     url_for("views.predictions_views.write_predicted_flower", prediction=prediction)
    # )
