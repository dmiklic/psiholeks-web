# app/__init__.py

import os

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    if os.getenv('FLASK_CONFIG')=="production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)

    migrate = Migrate(app, db)
    
    from app import models

    # Update the database from csv file
    # TODO: A better and more scalable way is to use
    # odo (https://github.com/blaze/odo/)
    # but it's giving me an 'Access denied' error
    # TODO: This  might not be the right place to do
    # initialization
    with app.app_context():
        # TODO: Check here if the table actually exists
        # otherwise, problems appear on new deployments
        # i.e., flask db * commands fail
        # Remove old data
        models.Word.query.delete()
        db.session.commit()
    
        # Populate the database from .csv
        data = pd.read_csv('app/static/data/psiholeks.csv',
                           delimiter=';',
                           index_col='rijec')
        data.to_sql('rijeci', db.engine, if_exists='append')
        
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    return app
