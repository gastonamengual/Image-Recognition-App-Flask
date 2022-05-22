from flask import Blueprint, redirect, request, url_for, flash
from ...controllers import predictions_controller

home_scope = Blueprint("home_scope", __name__, url_prefix="/home")

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@home_scope.post("/file_image_recognition")
def file_image_recognition():

    if "image" not in request.files:
        flash("No image was uploaded")
        return redirect(request.url)

    image = request.files["image"]

    if image.filename == "":
        flash("No image selected for uploading")
        return redirect(url_for("views.home_views.home"))

    if not allowed_file(image.filename):
        flash("Allowed image types are png, jpg, and jpeg")
        return redirect(url_for("views.home_views.home"))

    prediction = predictions_controller.predict(image)

    return redirect(url_for("views.home_views.show_image", prediction=prediction))


@home_scope.post("/real_time")
def real_time():
    predictions_controller.real_time()
    return redirect(url_for("views.home_views.main"))
