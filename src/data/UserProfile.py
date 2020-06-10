import mongoengine
from data.MusicAccount import MusicAccount


# User's favorite preferences
class UserProfile(mongoengine.EmbeddedDocument):
    primary_music_account_id = mongoengine.ObjectIdField()
    top_tracks = mongoengine.ListField()
    top_artists = mongoengine.ListField()
    favorite_genre = mongoengine.StringField()
