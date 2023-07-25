import os
from app import my_app

config_name = os.getenv("FLASK_CONFIG")
app = my_app(config_name)


# @app.route("/")
# def hello_world_app():
#     return "Hello World! This is my lame app."


if __name__ == "__main__":
    app.run()
