from flask import Flask, render_template
from flask.ext.sqlalchemy import sqlalchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

app = Flask(__name__)
app.config.from_object('punchstarter.default_settings') #let Flask know about the settings file
manager = Manager(app)

db = SQLAlchemy(app)
migrate = Migrate(app)
manager.add_command('db', MigrateCommand)

@app.route("/")
def hello():
    return render_template("index.html")
    # render_template automaticially looks for templates in the templates folder