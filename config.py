import os

CSRF_ENABLED = True
SECRET_KEY = 'dreamcatcher_secret_key'

#DB configuration
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dreamcatcher.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

