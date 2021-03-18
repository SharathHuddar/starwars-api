from flask import Blueprint, current_app, request
from werkzeug.local import LocalProxy
from planets_module import state_machine as psm
from starwars_service import helpers

logger = LocalProxy(lambda: current_app.logger)

planets_resources = Blueprint(
    'planets_resources',
    __name__
)

@planets_resources.route('', methods=['GET'])
def get():
    name = request.args.get('name')
    planet_names = psm.get(name)
    return {'results': planet_names}

@planets_resources.route('', methods=['POST'])
def post():
    payload = request.json
    helpers.assert_true('name' in payload, 'name is required')
    planet_names = psm.set(payload['name'])
    return {'results': planet_names}