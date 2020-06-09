import mongoengine


# User's favorite preferences
class UserProfile(mongoengine.EmbeddedDocument):
    primary_music_account_id = mongoengine.ListField()
    top_tracks = mongoengine.ListField()
    favorite_genre = mongoengine.StringField()
