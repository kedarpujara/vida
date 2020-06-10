import mongoengine


MUSIC_PLATFORM_TYPES = {
    'SPOTIFY',
    'APPLE_MUSIC',
    'SOUNDCLOUD',
    'GOOGLE_PLAY'
    'AMAZON_MUSIC',
}


class MusicAccount(mongoengine.EmbeddedDocument):
    primary_platform = mongoengine.StringField(choices=MUSIC_PLATFORM_TYPES)
    platforms_added = mongoengine.ListField(choices=MUSIC_PLATFORM_TYPES)
