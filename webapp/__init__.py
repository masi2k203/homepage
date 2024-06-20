import os

from flask import Flask

from webapp.blueprints import home, link


def create_app(test_config=None):
    """Flaskアプリケーションを作成"""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello World"

    app.register_blueprint(home.bp)
    app.register_blueprint(link.bp)

    return app
