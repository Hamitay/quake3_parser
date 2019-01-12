from api import parser_api
import pytest
from pytest_mock import mocker
import json

class TestApi:

    @pytest.fixture(scope="module")
    def get_games_request(self):
        app = parser_api.app.test_client()
        return app.get("/games")

    def test_get_games_status_code(self, get_games_request):
        assert 200 == get_games_request.status_code

    def test_get_games_content_type(self, get_games_request):
        assert "application/json" == get_games_request.content_type
