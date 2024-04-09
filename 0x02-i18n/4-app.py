#!/usr/bin/env python3
"""
Task 4. Force locale with URL parameter
Implement a way to force a particular locale by
passing the locale=fr parameter to your app's URLs.
"""

import babel
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
def get_locale() -> str:
    """
    Get locale from request

    Detect if the incoming request contains locale
    argument and if its value is a supported locale,
    return it
    """
    locale: str = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Render hello world template

    Renders the 4-index.html template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
