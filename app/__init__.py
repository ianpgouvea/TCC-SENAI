from flask_mysqldb import MySQL
from flask_script import Manager
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

db = MySQL(app)

manager = Manager(app)

from app.controller import default
from app.models import form
