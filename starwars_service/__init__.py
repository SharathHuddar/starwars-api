import logging
import os
import traceback
from time import strftime

from flask import Flask, jsonify, request, current_app
from werkzeug.local import LocalProxy

from starwars_service import config

logger = LocalProxy(lambda: current_app.logger)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def create_app(stage=None):
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)
    app.logger.info("App created")
    if not stage:
        stage = os.environ.get('FLASK_ENV', 'development')
    if stage == 'development':
        app.config.from_object(config.DevelopmentConfig)
    elif stage == 'production':
        app.config.from_object(config.ProductionConfig)

    initialize_extensions(app)
    register_blueprints(app)

    return app

def initialize_extensions(app):

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(levelname)s %(asctime)s %(name)s: %(message)s"
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


    @app.errorhandler(Exception)
    def exceptions(e):
        """ Logging after every Exception. """
        ts = strftime('[%Y-%b-%d %H:%M]')
        tb = traceback.format_exc()
        logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                    ts,
                    request.remote_addr,
                    request.method,
                    request.scheme,
                    request.full_path,
                    tb)
        return "Internal Server Error", 500


def register_blueprints(app):
    from movies_module.resources import movies_resources
    app.register_blueprint(
        movies_resources,
        url_prefix='/starwars/movies'
    )

    from planets_module.resources import planets_resources
    app.register_blueprint(
        planets_resources,
        url_prefix='/starwars/planets'
    )