from flask import Flask, render_template
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.user import user_ns
from views.auth import auth_ns

api = Api(title="Flask Course Project 3", doc="/docs")


def create_app(config_object):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return render_template('index.html')

    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config)
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)


