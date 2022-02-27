from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initializing the app
app = Flask(__name__,instance_relative_config = True)

#setting up the configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing flask extensions
bootstrap = Bootstrap(app)

from app import views









#sdf
