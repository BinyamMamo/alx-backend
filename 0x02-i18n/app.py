#!/usr/bin/env python3
"""
Task 8. Display the current time
Based on the inferred time zone, display the
current time on the home page in the default format
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions
from typing import Dict, Optional


class Config(object):
    """
    Config class
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """
    Returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed
    """
    login_id: Optional[str] = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Executes before each request"""
    user: Optional[Dict] = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Locale getter to determine best match
    based on user, request headers, query params
    """
    locale: Optional[str] = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Select and return appropriate timezone
    based on user, query params, or default
    """
    tzone: Optional[str] = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    default_tz: str = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_tz


@app.route('/')
def index() -> str:
    """
    Render the index page template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
