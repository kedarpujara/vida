import mongoengine
import datetime


class User(mongoengine.Document):
    first_name = mongoengine.StringField()
    last_name = mongoengine.StringField()
    email = mongoengine.StringField()
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    phone = mongoengine.StringField()

    profile_id = mongoengine.ObjectIdField()
    music_account_id = mongoengine.ObjectIdField()
    post_ids = mongoengine.ListField()
