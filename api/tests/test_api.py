from api import parser_api
from api import exception_messages
import pytest
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

    @pytest.fixture(scope="class")
    def get_invalid_request(self):
        app = parser_api.app.test_client()
        return app.get("/games/aa")

    @pytest.fixture(scope="class")
    def get_not_found_request(self):
        app = parser_api.app.test_client()
        return app.get("/games/999")

    def test_get_games_by_id_status_code(self, get_request):
        assert 200 == get_request.status_code

    def test_get_games_by_id_content_type(self, get_request):
        assert "application/json" == get_request.content_type

    def test_bad_request_status_code(self, get_invalid_request):
        assert 400 == get_invalid_request.status_code

    def test_bad_request_message(self, get_invalid_request):
        assert exception_messages.BAD_PARAMETER in str(get_invalid_request.data)

    def test_not_found_status_code(self, get_not_found_request):
        assert 404 == get_not_found_request.status_code

    def test_not_found_message(self, get_not_found_request):
        assert exception_messages.GAME_NOT_FOUND_MESSAGE in str(get_not_found_request.data)

