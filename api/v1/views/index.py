#!/usr/bin/python3
"""
import app_views from api.v1.views
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/status', strict_slashes=False)
def status():
    """return status"""
    return {"status": "OK"}


@app_views.route('/stats', strict_slashes=False)
def stats():
    """return stats"""
    from models import storage
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    return {"amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)}
