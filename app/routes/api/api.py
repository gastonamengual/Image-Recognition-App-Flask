from flask import Blueprint, redirect, request, url_for, flash
from ...controllers import controller

home_scope = Blueprint("home_scope", __name__, url_prefix="/home")


@home_scope.post("/file_image_recognition")
def file_image_recognition():

    if "image" not in request.files:
        flash("No image was uploaded")
        return redirect(request.url)

    image_file = request.files["image"]

    filename = controller.detect_object(image_file)

    return redirect(url_for("views.home_views.show_object_detection", filename=filename))


@home_scope.post("/real_time")
def real_time():
    controller.real_time()
    return redirect(url_for("views.home_views.main"))
