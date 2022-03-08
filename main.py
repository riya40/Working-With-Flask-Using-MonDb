import flask
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.errors import BulkWriteError
"""
Working with Crud Operations Using Flask and Mongodb
"""

app = Flask(__name__, template_folder='template')
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/contacts_db")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb://localhost:27017/contacts_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route("/")
def hello():
    return "Hello World! Working With MongoDb and Flask"


if __name__ == '__main__':
    app.run(debug=True)
