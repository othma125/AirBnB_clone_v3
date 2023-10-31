#!/usr/bin/python3
"""
Contains the class DBStorage that
handles all database storage
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_session(exception):
    """teardown session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors that returns a
    JSON-formatted 404 status code"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    """main method"""
    from os import getenv
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if not HBNB_API_PORT else int(HBNB_API_PORT)
    app.run(host=host, port=port, threaded=True, debug=True)
