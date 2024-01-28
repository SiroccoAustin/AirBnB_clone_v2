#!/usr/bin/python3
"""Starts Flask web framework"""

from flask import Flask, render_template
from flask import abort

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def greet_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def another_page():
    """Displays 'HBNB'."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of <text>."""
    return 'C {}'.format(text.replace('_', ' '))

@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays 'Python' followed by the value of <text>."""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Displays 'Python' followed by the value of <text>."""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays 'Python' followed by the value of <text>."""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
