#!/bin/bash

export FLASK_APP=src/app.py
if [[ $1 == "dev" ]]; then
    export FLASK_ENV=development
elif [[ $1 == "prod" ]]; then
    export FLASK_ENV=production
else
    echo "Usage: ./run.sh <dev/prod>"
    exit
fi

if [[ ! $PORT ]]; then
    export PORT=3000
fi

flask run -p $PORT