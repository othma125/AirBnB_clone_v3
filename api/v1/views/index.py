#!/usr/bin/python3
"""
App views for AirBnB_clone_v3 API v1
we will use the blueprint app_views
to group all these views
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """ returns status OK """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def count():
    """ returns number of each objects by type """
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    return jsonify({classes[cls]: storage.count(cls)
                    for cls in classes})
