#Saves current context
export PREV_HAS_VENV=$HAS_VENV

export HAS_VENV=$(pip3 list | grep virtualenv)

if [ -z "$HAS_VENV" ]
then
    echo "Please install virtualenv with \"pip install virtualenv\" " 
else
    echo "Building virtual environment"

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    deactivate

    echo "virtual environment built"
fi

#Restores context
export HAS_VENV=PREV_HAS_VENV