from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

app = Flask(__name__)
app.config.from_object('punchstarter.default_settings') #let Flask know about the settings file
manager = Manager(app)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

from punchstarter.models import *

@app.route("/") #home page route
def hello():
    return render_template("index.html")
    # render_template automaticially looks for templates in the templates folder

@app.route("/projects/create") # create a project route
def create():
    return render_template("create.html")