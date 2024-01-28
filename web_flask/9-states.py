#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States."""
    states = storage.all(State)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """Displays an HTML page with info about <id>"""
    state = storage.get(State, id)
    return render_template("9-states.html", state=state)



@app.teardown_appcontext
def def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)