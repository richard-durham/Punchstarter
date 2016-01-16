from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
import datetime

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

@app.route("/projects/create/", methods=['GET', 'POST']) # create a project route
def create():
	if request.method == "GET":
		return render_template("create.html")
	if request.method == "POST":
		# Handle form sumbission

		now = datetime.datetime.now()

    	#form returns date as text string - need to convert to proper date/time for database
    	time_end = request.form.get("funding_end_date")
    	time_end = datetime.datetime.strptime(time_end, "%Y-%m-%d")

    	new_project = Project(
    		# member_id would normally take user login details however as we don't have the built
    		# we are hardcoding a single member_id in
    		member_id = 1, # Guest Creator
    		name = request.form.get("project_name"),
    		short_description = request.form.get("short_description"),
    		long_description = request.form.get("long_description"),
    		goal_amount = request.form.get("funding_goal"),
    		time_start = now,
    		time_end = time_end,
    		time_created = now,
    	)

    	db.session.add(new_project)
    	db.session.commit()

    	# to ensure no duplicate post (i.e. user refreshes the page we don't end up duplicating the most recnet submission)
    	return redirect(url_for('create'))