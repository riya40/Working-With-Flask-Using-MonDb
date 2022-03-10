import mongoengine as mongoengine


class User(mongoengine.Document):
    id = mongoengine.StringField()
    name = mongoengine.StringField()
    number = mongoengine.StringField()
    email = mongoengine.StringField()
