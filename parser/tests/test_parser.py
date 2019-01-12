from .. import parser
import json

class TestParser:

    def setup(self):
        self.game_log = parser.open_log_file("resources/test_games.log")

        with open("resources/test_response.json") as response_json:
            self.expected_response = json.load(response_json)

    def test_split_games(self):
        games = parser.split_games(self.game_log)
        assert len(self.expected_response) == len(games)

    def test_get_players(self):
        games = parser.split_games(self.game_log)
        players = [parser.get_players(game) for game in games]

        assert self.expected_response["game_1"]["players"].sort() == players[0].sort()
        assert self.expected_response["game_2"]["players"].sort() == players[1].sort()
        assert self.expected_response["game_3"]["players"].sort() == players[2].sort()
