#!/bin/ash

# fail if migration or any other step fails
set -e

# Delete older .pyc files
find . -name "*.pyc" -exec rm -rf {} \;

# Run server
if [ $FLASK_ENV == "development" ]
then
  gunicorn "starwars_service:create_app()" --reload
else
  gunicorn "starwars_service:create_app()"
fi


