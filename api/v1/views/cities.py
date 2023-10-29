#!/usr/bin/python3
"""
Create a new view for city objects that handles
all default RESTFul API actions
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities_in_state(state_id):
    """get all cities"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(list(city.to_dict()
                        for city in state.cities))


@app_views.route('/cities', methods=['GET'], strict_slashes=False)
def get_cities():
    """get all states"""
    return jsonify(list(city.to_dict()
                        for city in storage.all(City).values()))


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """get a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    city.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """Creates a City"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    data['state_id'] = state_id
    city = City(**data)
    city.save()
    return make_response(jsonify(city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Updates a City object"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data = request.get_json()
    keys = 'id', 'state_id', 'created_at', 'updated_at'
    for key, value in data.items():
        if key in keys:
            continue
        setattr(city, key, value)
    city.save()
    return make_response(jsonify(city.to_dict()), 200)
