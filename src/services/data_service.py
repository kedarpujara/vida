from typing import List, Optional
import datetime
import bson

from data.User import User
from data.MusicAccount import MusicAccount
from data.MusicAccountPlatformTypes import MusicAccountPlatformTypes
from data.Post import Post
from data.PostMetadata import PostMetadata
from data.PostType import PostType


def create_account(name: str, email: str) -> User:
    user = User()
    user.name = name
    user.email = email
    user.save()
    return user


def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user


def create_music_account(active_account: User, primary_platform: MusicAccountPlatformTypes,
                         added_platforms) -> MusicAccount:
    music_account = MusicAccount()
    music_account.primary_platform = primary_platform
    music_account.save()

    active_account.music_account_id = music_account.id
    active_account.save()

    return music_account


def create_post(active_account: User, music_account: MusicAccount, song: str, artist: str, album: str, genre: str,
                podcast: str,
                length_in_sec: float) -> Post:
    post = Post()
    post_metadata = PostMetadata()
    post_metadata.song = song
    post_metadata.artist = artist
    post_metadata.album = album
    post_metadata.genre = genre
    post_metadata.length_in_sec = length_in_sec
    post_metadata.podcast = podcast

    post_metadata.save()

    post.post_metadata_id = post_metadata.id
    post.user_id = active_account.id
    post.music_account_id = music_account.id

    post.save()

    return post


def fetch_posts(active_account: User) -> List[Post]:
    print("Not implemented yet")
