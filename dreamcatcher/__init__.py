from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

dreamcatcher = Flask(__name__)
dreamcatcher.config.from_object('config')
db = SQLAlchemy(dreamcatcher)

lm = LoginManager()
lm.init_app(dreamcatcher)
lm.login_view = 'signin'

from dreamcatcher import views, models


