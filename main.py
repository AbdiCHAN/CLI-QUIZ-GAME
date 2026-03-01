# main.py
from models.game import Game
from rich import print

def main():
    game = Game()

    while True:
        print("\n[bold]CLI Quiz Game[/bold]")
        print("1. Register")
        print("2. Login")
        print("3. Play Quiz")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            game.register(username, password)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            game.login(username, password)

        elif choice == "3":
            game.play_quiz()

        elif choice == "4":
            print("[bold green]Goodbye![/bold green]")
            break

        else:
            print("[red]Invalid choice.[/red]")

if __name__ == "__main__":
    main()