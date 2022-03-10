from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from models import User

"""
Working with Crud Operations Using Flask and Mongodb
"""

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'addressbook_db',
    'host': 'localhost',
    'port': 27017
}

app.config['MONGODB_SETTINGS'] = {
'host': 'mongodb://localhost/addressbook_db'
}
db = MongoEngine(app)
db = MongoEngine()
db.init_app(app)




@app.route("/welcome/")
def hello():
    return "Hello World! Working With MongoDb and Flask"


@app.route("/_contact/", methods=['POST'])
def contact_adding():
    """ Adding The First Contact"""
    details = User(name=request.form["name"], number=request.form['number'],
                   email=request.form['email'])
    details.save()
    return jsonify(message="success"), 201


@app.route('/movies/<id>', methods=['PUT'])
def update_contact(id):
    body = request.get_json()
    update_contact = User.objects.get(id=id)
    update_contact.update(**body)
    return jsonify(str(update_contact.id)), 200


@app.route('/delete/<id>', methods=["DELETE"])
def delete_contact(id):
    """Deleting The Contact"""
    contact = User.objects.get(id=id)
    contact.delete()
    return jsonify(str(contact.id)), 200


@app.route('/get_contacts/')
def get_all_contacts():
    """Retreiving All contacts"""
    retreiving_contacts = User.objects()
    return jsonify(retreiving_contacts), 200


if __name__ == '__main__':
    app.run(debug=True)
