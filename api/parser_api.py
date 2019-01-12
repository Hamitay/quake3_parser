from parser import parser
from api import app
from flask import jsonify

@app.route('/games')
def get_all_games():
    response_data = parser.parse("games.log")
    return jsonify(response_data)
