from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def init_app(app: Flask):

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
