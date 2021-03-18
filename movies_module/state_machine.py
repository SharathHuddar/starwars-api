import requests
from flask import current_app

def get():
    SW_API_BASE_URL = current_app.config['SW_API_BASE_URL']
    resp = requests.get(f'{SW_API_BASE_URL}/films')
    movies = resp.json()
    movie_titles = [m['title'] for m in movies['results']]
    return movie_titles