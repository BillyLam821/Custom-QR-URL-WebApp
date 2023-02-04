from flask import Flask
from dotenv import dotenv_values
from flask_login import LoginManager
from src.database import db, User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'siahf*!HE!Ondanu#2)'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    if test_config is None:
        env_config = dotenv_values(".env")
        flask_config = dotenv_values(".flaskenv")
        
        app.config.from_mapping(
            SECRET_KEY = env_config["SECRET_KEY"],
            SQLALCHEMY_DATABASE_URI = flask_config["SQLALCHEMY_DB_URI"],
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            JWT_SECRET_KEY = flask_config["JWT_SECRET_KEY"]
        )

    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)

    from . import urlshort
    from . import auth
    app.register_blueprint(urlshort.bp)
    app.register_blueprint(auth.bp)

    return app