from flask import Blueprint
from .api import home_scope

api_scope = Blueprint("api", __name__, url_prefix="/api")
api_scope.register_blueprint(home_scope)
