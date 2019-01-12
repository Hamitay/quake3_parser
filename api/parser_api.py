from parser import parser
from api import app
from flask import jsonify

@app.route('/games')
def get_all_games():
    response_data = parser.parse("games.log")
    return jsonify(response_data)

@app.route('/games/<id>')
def get_game_by_id(id):
    game_key = parser.build_game_key(id)
    response_data = parser.parse("games.log")[game_key]
    return jsonify(response_data)

