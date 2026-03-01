import argparse
from models.game import Game


def main():
    parser = argparse.ArgumentParser(description="CLI Quiz Game")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("register")
    subparsers.add_parser("login")
    subparsers.add_parser("play")

    args = parser.parse_args()
    game = Game()

    if args.command == "register":
        username = input("Username: ")
        password = input("Password: ")
        game.register(username, password)

    elif args.command == "login":
        username = input("Username: ")
        password = input("Password: ")
        game.login(username, password)

    elif args.command == "play":
        game.play_quiz()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
