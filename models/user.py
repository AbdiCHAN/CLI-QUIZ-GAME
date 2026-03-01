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
