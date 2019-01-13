#Set environment variables
export FLASK_APP=api
export GAME_LOG_PATH="games.log"

source env/bin/activate
pip install -r requirements.txt
flask run
deactivate
export FLASK_APP=$TEMPORARY_FLASK_APP
