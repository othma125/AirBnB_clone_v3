#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from api.v1.views import app_views
from flask import Flask
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """teardown"""
    storage.close()


if __name__ == '__main__':
    from os import getenv

    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
