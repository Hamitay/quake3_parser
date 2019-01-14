from parser import parser
from flask import jsonify, Blueprint
from flask import current_app as app
from . import exception, exception_messages
from .constants import GAME_PATH_CONFIG

parser_app = Blueprint("parser_api", __name__)

@parser_app.route("/games")
def get_all_games():
    response_data = parser.parse(app.config[GAME_PATH_CONFIG])
    return jsonify(response_data)

@parser_app.route("/games/<id>")
def get_game_by_id(id):
    try:
        #Validates the game id
        id = int(id)
        if id < 0: raise ValueError

        game_key = parser.build_game_key(id)
        response_data = parser.parse(app.config[GAME_PATH_CONFIG])[game_key]

    except(ValueError):
        raise exception.BadParam(exception_messages.BAD_PARAMETER)

    except(KeyError):
        raise exception.ResourceNotFound(exception_messages.GAME_NOT_FOUND_MESSAGE)

    return jsonify(response_data)

@parser_app.errorhandler(exception.ApiException)
def handle_game_not_found(error):
    """Error handler method for all of the API exceptions."""
    response = jsonify(error.message)
    response.status_code = error.status_code
    return response