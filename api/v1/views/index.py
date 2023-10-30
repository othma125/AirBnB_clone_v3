#!/usr/bin/python3
"""
App views for AirBnB_clone_v3
"""

from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ returns status """
    return {"status": "OK"}


@app_views.route('/stats')
def count():
    """ returns number of each objects by type """
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    return {classes.get(cls): storage.count(cls)
            for cls in classes}
