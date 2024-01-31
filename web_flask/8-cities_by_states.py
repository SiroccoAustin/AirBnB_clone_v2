#!/usr/bin/python3
"""Starts a Flask web application."""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    """Displays an HTML page with a list of all states and related cities."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def closedown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
