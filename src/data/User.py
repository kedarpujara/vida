from mongoengine import *
import datetime
from data.UserProfile import UserProfile


# Top level user data
class User(Document):
    username = StringField(required=True)
    email = StringField(required=True, unique=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    registered_date = DateTimeField(default=datetime.datetime.now)
    phone = StringField()
    user_profile = EmbeddedDocumentField(UserProfile)
    music_account_ids = ListField(ObjectIdField())
    posts = ListField(ObjectIdField())

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
