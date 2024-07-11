from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.routes import main
    app.register_blueprint(main.bp)

    from app.routes import auth
    app.register_blueprint(auth.bp)

    return app

from app.models.user import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))