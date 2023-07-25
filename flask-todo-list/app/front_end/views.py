from flask import render_template

from app.models import TodoApp
from . import front_end


@front_end.route("/")
def index():
    all_todos = TodoApp.query.all()
    return render_template("index.html", todos=all_todos)
