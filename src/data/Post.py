import mongoengine
from data.PostMetadata import PostMetadata
from data.User import User
from data.MusicAccount import MusicAccount


class Post(mongoengine.Document):
    user_ = mongoengine.ReferenceField(User)
    music_account_id = mongoengine.ObjectIdField()
    post_metadata = mongoengine.EmbeddedDocumentField(PostMetadata)

    meta = {
        'db_alias': 'core',
        'collection': 'posts'
    }
