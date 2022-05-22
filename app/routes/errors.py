from flask import Blueprint, flash, redirect, url_for

from ..controllers.exceptions import NoImageSelected, WrongFilenameFormat

errors_scope = Blueprint("errors", __name__)


@errors_scope.app_errorhandler(NoImageSelected)
def handle_no_image_selected(NoImageSelected):
    flash("No image selected for uploading")
    return redirect(url_for("views.home_views.main"))


@errors_scope.app_errorhandler(WrongFilenameFormat)
def handle_no_image_selected(WrongFilenameFormat):
    flash("Allowed image types are png, jpg, and jpeg")
    return redirect(url_for("views.home_views.main"))
