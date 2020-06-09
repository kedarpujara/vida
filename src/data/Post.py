import mongoengine


class Post(mongoengine.Document):
    user_id = mongoengine.ObjectIdField()
    music_account_id = mongoengine.ObjectIdField()
    post_metadata_id = mongoengine.ObjectIdField()

    meta = {
        'db_alias': 'core',
        'collection': 'posts'
    }
