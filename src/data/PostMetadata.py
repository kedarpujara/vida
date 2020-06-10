import mongoengine
import datetime

POST_TYPE = ('SONG', 'PODCAST')


class PostMetadata(mongoengine.EmbeddedDocument):
    song = mongoengine.StringField()
    artist = mongoengine.StringField()
    album = mongoengine.StringField()
    podcast = mongoengine.StringField()
    post_type = mongoengine.StringField(choices=POST_TYPE)
    genre = mongoengine.StringField()
    length_in_sec = mongoengine.FloatField()
    date_posted = mongoengine.DateTimeField(default=datetime.datetime.now)
    upvotes = mongoengine.IntField()
