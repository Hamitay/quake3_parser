#Set environment variables
export FLASK_APP=api
export GAME_LOG_PATH="games.log"

#Runs the virtual environment
source env/bin/activate
flask run
deactivate
