from flask import Blueprint
from .predict import predictions_scope

views_scope = Blueprint("views", __name__, url_prefix="/")
views_scope.register_blueprint(predictions_scope)
