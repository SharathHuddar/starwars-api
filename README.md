# SpotDraft - Star Wars Assignment

A simple REST API wrapper around https://swapi.dev/

## Setup

Install all the python dependencies needed to run this app:
```
pip install -r requirements.txt
```

## Running the app

Once all the dependencies are installed, run the app:
```
bash run.sh
```
## Running tests
Tests are written with postman (newman). `newman` CLI is needed to run the tests:
```
npm install -g newman
```

To run the tests, make sure that the app is running and then run the following command:
```
newman run tests/StarWars-API.postman_collection.json
```

## API Documentation
API documentation can be found here -> https://documenter.getpostman.com/view/85123/Tz5v1Eru