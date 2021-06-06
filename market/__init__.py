from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt  import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../market.db'
app.config['SECRET_KEY'] = '32nrfes90j980423-0rfjwopty9043'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginmanager = LoginManager(app)
loginmanager.login_view = "login_page"
loginmanager.login_message_category = "info"
from market import routes