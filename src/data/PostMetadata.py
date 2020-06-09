import mongoengine
import datetime


class PostMetadata(mongoengine.EmbeddedDocument):
    song = mongoengine.StringField()
    artist = mongoengine.StringField()
    album = mongoengine.StringField()
    podcast = mongoengine.StringField()
    post_type = mongoengine.IntField()
    genre = mongoengine.StringField() # if its a song
    length_in_sec = mongoengine.FloatField()
    date_posted = mongoengine.DateTimeField(default=datetime.datetime.now())
    upvotes = mongoengine.IntField()
