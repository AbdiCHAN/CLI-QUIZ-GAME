# models/user.py
# Defines User class for the CLI Quiz Game

class User:
    def __init__(self, username, password):
        self.username = username  # store username
        self.password = password  # store password
        self.scores = []          # store all quiz scores

    def to_dict(self):
        """
        Convert object to dictionary for saving in JSON
        """
        return {
            "username": self.username,
            "password": self.password,
            "scores": self.scores
        }

    def check_password(self, password):
        """
        Returns True if password matches, False otherwise
        """
        return self.password == password