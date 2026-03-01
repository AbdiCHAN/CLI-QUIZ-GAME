from models.game import Game


def test_game_loads_users():
    game = Game()
    assert isinstance(game.users, list)