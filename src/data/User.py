import mongoengine
import datetime
from data.Post import Post
from data.UserProfile import UserProfile


# Top level user data
class User(mongoengine.Document):
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    phone = mongoengine.StringField()
    profile_id = mongoengine.EmbeddedDocumentField(UserProfile)
    music_account_ids = mongoengine.ListField()
    posts = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
