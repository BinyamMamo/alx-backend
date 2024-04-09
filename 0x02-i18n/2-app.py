#!/usr/bin/env python3
"""
Task 2 - Get locale from request
Create a get_locale function with the babel.localeselector decorator.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get the best match between requested languages and supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """
    renders the home page
    """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(debug=True)
