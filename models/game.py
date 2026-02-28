# models/game.py
# Handles the Game logic of CLI Quiz Game

from models.user import User
from utils.fileio import load_json, save_json


class Game:

    def __init__(self):
        # Load users and questions
        self.users = load_json("data/users.json")
        self.questions = load_json("data/questions.json")
        self.current_user = None

    def register(self, username, password):
        # Check if username already exists
        for user in self.users:
            if user["username"] == username:
                print("Username already exists.")
                return

        new_user = User(username, password)
        self.users.append(new_user.to_dict())
        save_json("data/users.json", self.users)
        print("Registration successful.")

    def login(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                self.current_user = user
                print("Login successful.")
                return
        print("Invalid username or password.")

    def play_quiz(self):
        if not self.current_user:
            print("Please login first.")
            return

        score = 0  # Initialize score

        # Loop through all 7 questions
        for question in self.questions:
            print("\n" + question["question"])
            for option in question["options"]:
                print(option)
            answer = input("Enter answer (A/B/C/D): ").upper()
            if answer == question["answer"]:
                score += 1

        print(f"Your score: {score} / {len(self.questions)}")  # Display score out of 7

        # Save score to user's record
        self.current_user["scores"].append(score)
        save_json("data/users.json", self.users)