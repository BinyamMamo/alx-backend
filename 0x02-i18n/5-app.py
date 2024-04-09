#!/usr/bin/env python3
"""
Task 5. Basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Config class.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


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


def get_user(login_as: int) -> dict:
    """
    Get user object from users dict by id.

    Args:
        login_as (int): id of user to retrieve

    Returns:
        User object if id found, else None
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """
    Execute before each request to set user object.
    """
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale() -> str:
    """
    Determine best match locale from supported languages.

    Looks at URL arguments, request headers, and config.
    Returns best match locale or default config locale.
    """
    locale: str = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello() -> str:
    """
    Render template for root route.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
