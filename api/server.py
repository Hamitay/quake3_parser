
from flask import Flask
from .constants import *
import os
from .parser_api import parser_app

if __name__ == "__main__":
    app = Flask(__name__)

    #Sets up the config from the environment variable
    app.config[GAME_PATH_CONFIG] = os.environ.get(GAME_PATH_ENV, default=DEFAULT_GAME_PATH)
    
    #Register other endpoints as blueprint
    app.register_blueprint(parser_app)

    #If we are running this from a Docker container, we should serve at 0.0.0.0
    if os.environ.get(CONTAINER_ENV, default=False):
        app.run("0.0.0.0")
    else:
        app.run()