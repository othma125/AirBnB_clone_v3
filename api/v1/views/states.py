#!/usr/bin/python3
"""
Develop a new view for State objects that manages
all standard RESTful API operations.
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'],
                 strict_slashes=False)
def get_states():
    """get all states"""
    return jsonify([state.to_dict()
                    for state in storage.all(State).values()])


@app_views.route('/states/<state_id>',
                 methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """get a state by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """delete a state by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'],
                 strict_slashes=False)
def create_state():
    """create a state object"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    data = request.get_json()
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>',
                 methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """update a state object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.is_json:
        abort(400, 'Not a JSON')
    data = request.get_json()
    keys = 'id', 'created_at', 'updated_at'
    for key, value in data.items():
        if key in keys:
            continue
        setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
