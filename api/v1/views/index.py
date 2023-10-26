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
