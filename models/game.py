from models.user import User
from utils.fileio import load_json, save_json
from rich import print


class Game:
    def __init__(self):
        user_data = load_json("data/users.json")
        self.users = [User(**u) for u in user_data]
        self.questions = load_json("data/questions.json")
        self.current_user = None

    def save_users(self):
        save_json("data/users.json", [u.to_dict() for u in self.users])

    def register(self, username, password):
        if any(u.username == username for u in self.users):
            print("[red]Username already exists.[/red]")
            return

        new_user = User(username, password)
        self.users.append(new_user)
        self.save_users()
        print("[green]Registration successful.[/green]")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                self.current_user = user
                print("[green]Login successful.[/green]")
                return

        print("[red]Invalid username or password.[/red]")

    def play_quiz(self):
        if not self.current_user:
            print("[red]Please login first.[/red]")
            return

        score = 0

        for question in self.questions:
            print(f"\n[bold]{question['question']}[/bold]")
            for option in question["options"]:
                print(option)

            answer = input("Answer (A/B/C/D): ").upper()

            if answer == question["answer"]:
                score += 1

        self.current_user.add_score(score)
        self.save_users()

        print(f"[bold blue]Your score: {score}/{len(self.questions)}[/bold blue]")