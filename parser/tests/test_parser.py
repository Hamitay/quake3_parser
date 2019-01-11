from .. import parser

PLAYERS_0 = ["Mocinha", "Zeh", "Isgalamido", "Dono da Bola"]
PLAYERS_1 = ["Zeh", "Isgalamido", "Assasinu Credi", "Dono da Bola"]
PLAYERS_2 = ["Isgalamido", "Zeh" , "Assasinu Credi", "Dono da Bola"]

class TestParser:

    def setup(self):
        self.game_log = parser.open_log_file("resources/test_games.log")

    def test_split_games(self):
        games = parser.split_games(self.game_log)
        assert 3 == len(games)

    def test_get_players(self):
        games = parser.split_games(self.game_log)
        players = [parser.get_players(game) for game in games]

        assert PLAYERS_0.sort() == players[0].sort()
        assert PLAYERS_1.sort() == players[1].sort()
        assert PLAYERS_2.sort() == players[2].sort()
