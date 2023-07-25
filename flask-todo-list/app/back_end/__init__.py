from flask import Blueprint

back_end = Blueprint("back_end", __name__)

from . import views
