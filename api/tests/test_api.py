from api import parser_api
import pytest
from pytest_mock import mocker
import json

class TestApiGetGames:

    @pytest.fixture(scope="class")
    def get_request(self):
        app = parser_api.app.test_client()
        return app.get("/games")

    def test_get_games_status_code(self, get_request):
        assert 200 == get_request.status_code

    def test_get_games_content_type(self, get_request):
        assert "application/json" == get_request.content_type

class TestApiGetGameById:

    @pytest.fixture(scope="class")
    def get_request(self):
        app = parser_api.app.test_client()
        return app.get("/games/9")

    def test_get_games_by_id_status_code(self, get_request):
        assert 200 == get_request.status_code

    def test_get_games_by_id_content_type(self, get_request):
        assert "application/json" == get_request.content_type
