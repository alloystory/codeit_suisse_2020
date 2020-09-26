#!/bin/bash

if [[ $1 == "dev" ]]; then
    export FLASK_APP=src/app.py
    export FLASK_ENV=development
    flask run -h 127.0.0.1 -p 3000
elif [[ $1 == "prod" ]]; then
    export FLASK_APP=src/app.py
    export FLASK_ENV=production
    flask run -h 0.0.0.0 -p $PORT
else
    echo "Usage: ./run.sh <dev/prod>"
    exit
fi
