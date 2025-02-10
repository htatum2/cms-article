"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

#Add any logging levels and handlers with app.logger
logging.basicConfig(level=logging.WARNING)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views


# Example log messages for each log level
log = 'info'
if log:
    if log == 'info':
        app.logger.info('No issue.')
    elif log == 'warning':
        app.logger.warning('Warning occurred.')
    elif log == 'error':
        app.logger.error('Error occurred.')
    elif log == 'critical':
        app.logger.critical('Critical error occurred.')

# Log that the application has started
app.logger.warning('Flask application has started.')