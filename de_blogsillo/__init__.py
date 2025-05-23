import os
from flask import Flask

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'deBlogsillo.sqlite'),
  )

  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_pyfile(test_config)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  @app.route('/')
  def hello():
    return '<h1>Hi there! DB</h1>'

  from . import db
  db.init_app(app)
  
  from . import auth
  app.register_blueprint(auth.bp)

  return app
