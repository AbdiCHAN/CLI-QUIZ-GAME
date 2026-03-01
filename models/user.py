class User:
    def __init__(self, username, password, scores=None):
        self.username = username
        self.password = password
        self._scores = scores if scores is not None else []

    @property
    def scores(self):
        return self._scores

    def check_password(self, password):
        return self.password == password

    def add_score(self, score):
        self._scores.append(score)

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "scores": self._scores
        }
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
