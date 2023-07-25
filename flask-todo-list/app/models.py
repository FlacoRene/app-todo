from app import db, marsh


class TodoApp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))

    def __init__(self, text):
        self.text = text


class TodoAppSchema(marsh.Schema):
    class Metadata:
        field = ("id", "text")
