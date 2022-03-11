from flask import Flask, jsonify, request
from flask_restful import Api,Resource
from flask_mongoengine import MongoEngine
from models import User

"""
Working with Crud Operations Using Flask and Mongodb
"""

app = Flask(__name__)
api = Api(app)
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


class Operation(Resource):
    @app.route("/_contact/", methods=['POST'])
    def contact_adding(self):
        """ Adding The First Contact"""
        details = User(name=request.form["name"], number=request.form['number'],
                   email=request.form['email'])
        details.save()
        return jsonify(message="success"), 201

    @app.route('/get_contacts/')
    def get_all_contacts():
        """Retreiving All contacts"""
        retreiving_contacts = User.objects()
        return jsonify(retreiving_contacts), 200


class OperationName(Resource):
    @app.route('/update/<id>', methods=['PUT'])
    def update_contact(id):
        update_contact = User.objects.get(id=id).first()
        update_contact.update(User(name=request.form["name"], number=request.form['number'],
                   email=request.form['email']))
        return jsonify(str(update_contact.id)), 200

    @app.route('/delete/<id>', methods=['DELETE'])
    def delete_contact(id):
        """Deleting The Contact"""
        contact = User.objects.get(id=id)
        contact.delete()
        return jsonify(str(contact.id)), 200


api.add_resource(Operation, '/get_contacts/')
api.add_resource(OperationName, '/get/<name>')

if __name__ == '__main__':
    app.run(debug=True, port=12345)
