from flask import Blueprint
from .home_view import home_scope

views_scope = Blueprint("views", __name__, url_prefix="/")
views_scope.register_blueprint(home_scope)
