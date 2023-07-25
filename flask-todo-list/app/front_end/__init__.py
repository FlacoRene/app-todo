from flask import Blueprint

front_end = Blueprint("front_end", __name__)

from . import views
