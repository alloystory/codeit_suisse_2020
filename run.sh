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

flask run -h 127.0.0.1 -p 3000