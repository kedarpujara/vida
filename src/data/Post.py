import mongoengine


class Post(mongoengine.EmbeddedDocument):
    user_id = mongoengine.ObjectIdField()
    music_account_id = mongoengine.ObjectIdField()
    post_metadata_id = mongoengine.ObjectIdField()


