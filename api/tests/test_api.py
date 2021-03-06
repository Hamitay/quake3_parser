from api.parser_api import parser_app
from api import exception_messages
from ..constants import GAME_PATH_CONFIG
import os
import pytest
import json
from flask import Flask

def buildApp(gamelog):
    """Builds a test instance of the api. This is used before every test."""
    app = Flask(__name__)
    app.config[GAME_PATH_CONFIG] = gamelog
    app.register_blueprint(parser_app)
    app = app.test_client()

    return app

class TestApiGetGames:

    def setup(self):
        abs_path = os.path.dirname(__file__)
        self.game_log_path = abs_path + "/resources/test_games.log"

        response_path = abs_path + "/resources/test_response.json"
        with open(response_path) as response_json:
            self.expected_response = json.load(response_json)
        
        #Sorting, since player order doesn't matter
        for key in self.expected_response:
            self.expected_response[key]["players"].sort()

    @pytest.fixture(scope="class")
    def get_request(self):
        self.setup()
        app = buildApp(self.game_log_path)
        return app.get("/games")

    def test_get_games_status_code(self, get_request):
        assert 200 == get_request.status_code

    def test_get_games_content_type(self, get_request):
        assert "application/json" == get_request.content_type

    def test_data(self, get_request):
        assert self.expected_response == json.loads(get_request.data.decode('utf-8'))

class TestApiGetGameById:
    def setup(self):
        abs_path = os.path.dirname(__file__)
        self.game_log_path = abs_path + "/resources/test_games.log"

        response_path = abs_path + "/resources/test_response_id.json"
        with open(response_path) as response_json:
            self.expected_response = json.load(response_json)
        
        #Sorting, since player order doesn't matter
        self.expected_response["players"].sort()

    @pytest.fixture(scope="class")
    def get_request(self):
        self.setup()
        app = buildApp(self.game_log_path)
        return app.get("/games/9")

    @pytest.fixture(scope="class")
    def get_invalid_request(self):
        app = buildApp(self.game_log_path)
        return app.get("/games/aa")

    @pytest.fixture(scope="class")
    def get_not_found_request(self):
        app = buildApp(self.game_log_path)
        return app.get("/games/999")

    def test_get_games_by_id_status_code(self, get_request):
        assert 200 == get_request.status_code

    def test_get_games_by_id_content_type(self, get_request):
        assert "application/json" == get_request.content_type

    def test_get_games_by_id_response(self, get_request):
        assert self.expected_response == json.loads(get_request.data.decode('utf-8'))

    def test_bad_request_status_code(self, get_invalid_request):
        assert 400 == get_invalid_request.status_code

    def test_bad_request_message(self, get_invalid_request):
        assert exception_messages.BAD_PARAMETER in str(get_invalid_request.data)

    def test_not_found_status_code(self, get_not_found_request):
        assert 404 == get_not_found_request.status_code

    def test_not_found_message(self, get_not_found_request):
        assert exception_messages.GAME_NOT_FOUND_MESSAGE in str(get_not_found_request.data)

