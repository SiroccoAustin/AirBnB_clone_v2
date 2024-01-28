#!/usr/bin/python3
"""Starts a Flask web application."""

from models import storage
from flask import Flask, render_template
from models import *
from models.state import State

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """Displays an HTML page with a list of all states and related cities."""
    state = storage.all(State)
    return render_template('8-cities_by_states.html', state=state)

@app.teardown_appcontext
def closedown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
