import datetime
from colorama import Fore
from dateutil import parser

from infrastructure.switchlang import switch
import infrastructure.state as state
from services import data_service as svc


def run():
    print(' ****************** Welcome host **************** ')
    print()

    show_commands()

    while True:
        action = get_action()
        with switch(action) as s:
            s.case('c', create_account)
            s.case('l', log_into_account)
            s.case('p', create_post)

        if action:
            print()

        if s.result == 'change_mode':
            return


def show_commands():
    print('What action would you like to take:')
    print('[C]reate an account')
    print('[L]ogin to your account')
    print('[F]etch your posts')
    print('Create a [P]ost')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()


def create_account():
    print(' ****************** REGISTER **************** ')

    first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')
    username = input('What would you like your username to be? ').strip().lower()
    email = input('What is your email? ').strip().lower()
    account_exists = svc.find_account_by_email(email)
    if account_exists:
        error_msg(f"ERROR: Account with email {email} already exists.")
        return
    state.active_account = svc.create_account(username, first_name, last_name, email)
    success_msg(f"Created new account with id {state.active_account.id}.")


def log_into_account():
    print(' ****************** LOGIN **************** ')

    email = input('What is your email? ').strip().lower()
    account_exists = svc.find_account_by_email(email)

    if not account_exists:
        error_msg(f'Could not find account with email {email}.')
        return

    state.active_account = account_exists
    success_msg('Logged in successfully')


def create_post():
    if not state.active_account:
        error_msg("You have to login to create a post")
        return

    print(' ****************** CREATE POST **************** ')
    track_type = input('Is it a song or podcast? ').strip().lower()
    print(track_type)
    if track_type != 'song' and track_type != 'podcast':
        error_msg('Track must be either song or podcast');

    if track_type == 'song':
        song = input('What is the song name? ').strip().lower()
        artist = input('What is the artist name? ').strip().lower()
        album = input('What is the album name? ').strip().lower()
        genre = input('What is the genre name? ').strip().lower()
        post = svc.create_post(state.active_account, 0, song, artist, album, genre, '', 0)
        success_msg(f'Post successfully create with id {post.id}')

    if track_type == 'podcast':
        podcast_name = input('What is the podcast name? ').strip().lower()
        post = svc.create_post(state.active_account, '', '', '', '', podcast_name, 0)
        success_msg(f'Post successfully create with id {post.id}')





def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.first_name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)