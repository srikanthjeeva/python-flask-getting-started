from flask import Flask
import logging
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

#This config is needed if your URL can contain trailing slash. Example: This URL will not work http://localhost:3000/users/ if the below config is set to true
app.url_map.strict_slashes = False

# passing config 
app.config.from_object(Config)

# for database connection using SQLAlchemy
db = SQLAlchemy(app)

# for creating db tables, updating db schema using migrate  
migrate = Migrate(app, db)

# Using Marshmallow for returning DB schema as JSON in the API  
ma = Marshmallow(app)

# Logrotate will rotate log files if it exceeds certain size. And will backupCount retain last 5 logs. old backup log files will be deleted
handler = RotatingFileHandler('./log/development.log', maxBytes=1000000, backupCount=5)
logger = logging.getLogger('db_service')
logger.setLevel(logging.DEBUG)

#format of the log, if you want to write log in a particular format. Comment below lines if you dont want this. 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',datefmt='[%Y-%m-%dT%H:%M:%S]' )
handler.setFormatter(formatter)
logger.addHandler(handler)

# Import the models, controllers, helpers. 
from app import models, controllers, helpers
