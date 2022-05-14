from flask import Blueprint
from .predict import predictions_scope

api_scope = Blueprint("api", __name__, url_prefix="/api")
api_scope.register_blueprint(predictions_scope)
