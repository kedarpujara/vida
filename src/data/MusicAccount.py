import mongoengine


class MusicAccount(mongoengine.EmbeddedDocument):
    primary_platform = mongoengine.IntField()
    platforms_added = mongoengine.ListField()
