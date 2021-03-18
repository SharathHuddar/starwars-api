import requests
import pickle
import os
from flask import current_app

USER_PLANETS_FILE = 'user_added_planets.pickle'


def update_planet_file(data):
    with open(USER_PLANETS_FILE, 'wb') as f:
        pickle.dump(data, f)

def read_planet_file():
    user_added_planets = []
    if os.path.isfile(USER_PLANETS_FILE):
        with open(USER_PLANETS_FILE, 'rb') as f:
            user_added_planets = pickle.load(f)
    return user_added_planets

def get(name=None):
    SW_API_BASE_URL = current_app.config['SW_API_BASE_URL']
    params = {}
    if name:
        params['search'] = name
    resp = requests.get(f'{SW_API_BASE_URL}/planets', params=params)
    planets = resp.json()
    planet_names = [m['name'] for m in planets['results']]
    user_added_planets = read_planet_file()
    planet_names.extend(user_added_planets)
    if name:
        planet_names = [p for p in planet_names if p == name]
    return planet_names

def set(name):
    user_added_planets = read_planet_file()
    # Avoid creating duplicates
    if name not in user_added_planets:
        user_added_planets.append(name)
    update_planet_file(user_added_planets)
    return get()
