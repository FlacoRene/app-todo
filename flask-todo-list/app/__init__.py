from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import app_config

db = SQLAlchemy()
marsh = Marshmallow()


def my_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config["prod"])
    app.config.from_pyfile("config.py")
    db.init_app(app)
    marsh.init_app(app)

    from .front_end import front_end as front_end_blueprint

    app.register_blueprint(front_end_blueprint)

    from .back_end import back_end as back_end_blueprint

    app.register_blueprint(back_end_blueprint)
    return app
