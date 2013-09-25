from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

dreamcatcher = Flask(__name__)
dreamcatcher.config.from_object('config')
db = SQLAlchemy(dreamcatcher)

from dreamcatcher import views, models


