from flask import Blueprint, render_template

home_scope = Blueprint("home_views", __name__)


@home_scope.route("/")
@home_scope.route("/main/")
def main():
    return render_template("home.html", show_modal=False)


@home_scope.route("/show_object_detection/<filename>")
def show_object_detection(filename: str):
    return render_template("home.html", filename=filename, show_modal=True)
