from flask import Blueprint, render_template

home_scope = Blueprint("home_views", __name__)


@home_scope.route("/")
@home_scope.route("/main/")
def main():
    return render_template("home.html")


@home_scope.route("/show_image/<prediction>")
def show_image(prediction: str):
    return render_template("home.html", prediction=prediction)
