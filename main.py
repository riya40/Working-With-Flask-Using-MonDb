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


@app.route("/add_one/")
def add_one():
    """
    Adding The First Contact
    """
    db.todos.insert_one({'_id': "1", 'name': "diya", 'number': "94658747"})
    return flask.jsonify(message="success")


@app.route("/add_many/")
def add_many():
    """
    Adding th multiple Contacts if any duplicate value occurred it raises the exception
    """
    try:
        mul= db.todos.insert_many([
            {'_id': "2", 'name': "ari", 'number': "94548456"},
            {'_id': "3", 'name': "jones", 'number': "94658741"},
            {'_id':" 4", 'name': "priyanka", 'number': "946587445"}], ordered=False)
    except BulkWriteError as e:
        return flask.jsonify(message="duplicates encountered and ignored",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])

    return flask.jsonify(message="success", insertedIds=mul.inserted_ids)


@app.route("/retrieve_data/")
def get_data():
    """
    Retrieving all the contacts
    """
    todos = db.todos.find()
    return flask.jsonify([todo for todo in todos])


@app.route("/get_contact/")
def get_one():
    """
    Retrieving the desired contact only
    """
    todos = db.todos.find_one({}, {"_id": 0})
    return todos


@app.route("/update/")
def update_data():
    """
    Updating The Desired Contact Or Replacing The Contact With new One
    """
    response = db.todos.update_one(
        {"name": "diya"},
        {"$set": {"name": "varshi"}}
    )
    return response


@app.route("/delete_todo/")
def delete_todo():
    """
    Removing The Contact Which Is Dont Want to Keep in Records
    """
    remove = db.todos.delete_one({'name': "priyanka"})
    return remove


if __name__ == '__main__':
    app.run(debug=True)
