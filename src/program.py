import data.mongo_setup as mongo_setup
from colorama import Fore
import program_users


def main():
    mongo_setup.global_init()

    print_header()

    try:
        while True:
            program_users.run()
    except KeyboardInterrupt:
        return


def print_header():
    print(Fore.WHITE + '****************  Welcome to Vida  ****************')
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to Vida!")
    print("Why are you here?")
    print()


if __name__ == '__main__':
    main()