import os
from flask import Flask
from .constants import GAME_PATH_CONFIG, GAME_PATH_ENV

#Setting up the server and reading variables from the environment
app = Flask(__name__)
app.config[GAME_PATH_CONFIG] = os.environ.get(GAME_PATH_ENV, default=False)

import api.parser_api