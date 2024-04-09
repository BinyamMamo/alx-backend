#!/usr/bin/env python3
"""
0. Basic Flask app
setup a basic Flask app in 0-app.py
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """
    renders the home page
    """
    return render_template("0-index.html")
