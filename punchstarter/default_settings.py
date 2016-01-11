import os

#set Base_Dir to be same as path that default_settings.py is in (i.e. this file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"