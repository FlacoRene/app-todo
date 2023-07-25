from flask import render_template

from app.models import Todo
from . import front_end


@front_end.route("/")
def index():
    all_todos = Todo.query.all()
    return render_template("index.html", todos=all_todos)
