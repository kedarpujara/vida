from typing import List

from data.User import User
from data.MusicAccount import MusicAccount
from data.MusicAccount import MUSIC_PLATFORM_TYPES
from data.Post import Post
from data.PostMetadata import PostMetadata


def create_account(username: str, first_name: str, last_name: str, email: str) -> User:
    user = User()
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()
    return user


def find_account_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    return user


def create_music_account(active_account: User, primary_platform: MUSIC_PLATFORM_TYPES,
                         added_platforms) -> MusicAccount:
    music_account = MusicAccount()
    music_account.primary_platform = primary_platform
    music_account.save()

    active_account.music_account_id = music_account.id
    active_account.save()

    return music_account


def create_post(active_account: User, song: str, artist: str, album: str, genre: str,
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

    post.post_metadata = post_metadata
    post.user = active_account

    post.save()
    return post


def fetch_posts(active_account: User) -> List[Post]:
    print("Not implemented yet")
