from flask import Flask
from flask_session import Session


def create_app():
  app = Flask(__name__, static_url_path="/static")

  app.config['SECRET_KEY'] = "rrjjek3mr4rfko"
  app.config['SESSION_PERMANENT'] = False
  app.config['SESSION_TYPE'] = "filesystem"

  Session(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix="/")
  app.register_blueprint(auth, url_prefix="/")

  return app
