from flask import Blueprint, current_app
from werkzeug.local import LocalProxy
from movies_module import state_machine as msm
logger = LocalProxy(lambda: current_app.logger)

movies_resources = Blueprint(
    'movies_resources',
    __name__
)

@movies_resources.route('', methods=['GET'])
def get():
    movie_titles = msm.get()
    return {'results': movie_titles}