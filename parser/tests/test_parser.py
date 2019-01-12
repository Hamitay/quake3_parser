from .. import parser
import os
import json

class TestParser:
    def setup(self):
        abs_path = os.path.dirname(__file__)
        log_path = abs_path + "/resources/test_games.log"
        response_path = abs_path + "/resources/test_response.json"

        self.game_log = parser.open_log_file(log_path)

        with open(response_path) as response_json:
            self.expected_response = json.load(response_json)

        #Sorting, since player order doesn't matter
        self.expected_response["game_1"]["players"].sort()
        self.expected_response["game_2"]["players"].sort()
        self.expected_response["game_3"]["players"].sort()

    def test_split_games(self):
        games = parser.split_games(self.game_log)
        assert len(self.expected_response) == len(games)

    def test_get_players(self):
        games = parser.split_games(self.game_log)
        players = [parser.get_players(game) for game in games]

        assert self.expected_response["game_1"]["players"] == players[0]
        assert self.expected_response["game_2"]["players"] == players[1]
        assert self.expected_response["game_3"]["players"] == players[2]

    def test_players_kills(self):
        game = parser.split_games(self.game_log).pop()
        players = parser.get_players(game)
        kills = [parser.get_player_kills(game, player) for player in players] 
        
        expected_response = [0, 2, 2, 3]
        kills.sort()

        assert expected_response == kills

    def test_players_suicide(self):
        game = parser.split_games(self.game_log).pop()
        players = parser.get_players(game)
        suicides = [parser.get_player_suicides(game, player) for player in players] 
        
        expected_response = [0, 0, 0, 2]
        suicides.sort()

        assert expected_response == suicides

    def test_players_world_deaths(self):
        game = parser.split_games(self.game_log).pop()
        players = parser.get_players(game)
        world_deaths = [parser.get_player_world_deaths(game, player) for player in players] 
        
        expected_response = [0, 0, 1, 4]
        world_deaths.sort()

        assert expected_response == world_deaths

    def test_total_kills(self):
        game = parser.split_games(self.game_log).pop()
        players = parser.get_players(game)
        total_kills = parser.get_total_kills(game, players)

        expected_total = self.expected_response["game_3"]["total_kills"]
        expected_kills = self.expected_response["game_3"]["kills"]

        assert expected_total == total_kills[0]
        assert expected_kills == total_kills[1]

    def test_build_game_output(self):
        games = parser.split_games(self.game_log)
        output = [parser.build_game_output(game) for game in games]

        assert output[0] == self.expected_response["game_1"]
        assert output[1] == self.expected_response["game_2"]
        assert output[2] == self.expected_response["game_3"]
