from flask import request, jsonify, Response

from app import db
from app.models import TodoApp, TodoAppSchema
from . import back_end

todo_schema = TodoAppSchema()
todos_schema = TodoAppSchema(many=True)


# endpoint to create new todo
@back_end.route("/", methods=["POST"])
def add_todo():
    text = request.json
    new_todo = TodoApp(text)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"id": new_todo.id, "text": new_todo.text})


# endpoint to show all todos
@back_end.route("/", methods=["GET"])
def get_todo():
    all_todos = TodoApp.query.all()
    result = todos_schema.dump(all_todos)
    return jsonify(result.data)


# endpoint to delete todo
@back_end.route("/delete", methods=["POST"])
def todo_delete():
    ids = request.json
    for todo_id in ids:
        todo = TodoApp.query.get(todo_id)
        db.session.delete(todo)
    db.session.commit()
    return Response(status=204)
