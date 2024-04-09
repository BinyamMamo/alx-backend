# 🌐 0x02-i18n

## Project Overview 🪶
This project focuses on building a Flask application with internationalization (i18n) support. The purpose of the project is to create a web application that can serve content in multiple languages, handle user authentication, and display time information based on user preferences.

## 🔧 Requirements and Dependencies:
- Python 3.7
- Flask
- Flask-Babel
- pytz

##  📚 Tasks:

### 📝 0. Basic Flask app
---------------------
**📜 Task requirements:** Set up a basic Flask app with a single route and template to display "Welcome to Holberton" as the page title and "Hello world" as the header.

**🗂️ Files:** 
- **[0-app.py](0-app.py)**
- **[templates/0-index.html](templates/0-index.html)**

**🗒️ Description:** This task establishes the foundation of the Flask application by creating a simple route and template.

``` python
# Content of 0-app.py
# Flask app setup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
```

### 📝 1. Basic Babel setup
---------------------
**📜 Task requirements:** Install and configure the Flask-Babel extension to enable language localization.

**🗂️ Files:** 
- **[1-app.py](1-app.py)**

**🗒️ Description:** This task sets up Flask-Babel and configures it to support English and French languages.

``` python
# Content of 1-app.py
# Flask app setup with Babel configuration
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']

app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
```

### 📝 2. Get locale from request
---------------------
**📜 Task requirements:** Create a function to determine the locale based on the request's language preferences.

**🗂️ Files:** 
- **[2-app.py](2-app.py)**

**🗒️ Description:** This task implements a function to extract the user's preferred locale from the request headers.

``` python
# Content of 2-app.py
# Function to get locale from request
from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run()
```

### 📝 3. Parametrize templates
---------------------
**📜 Task requirements:** Use message IDs and translations to internationalize templates.

**🗂️ Files:** 
- **[3-app.py](3-app.py)**
- **[babel.cfg](babel.cfg)**
- **[translations/en/LC_MESSAGES/messages.po](translations/en/LC_MESSAGES/messages.po)**
- **[translations/fr/LC_MESSAGES/messages.po](translations/fr/LC_MESSAGES/messages.po)**
- **[templates/3-index.html](templates/3-index.html)**

**🗒️ Description:** This task involves setting up translations for template messages and parametrizing them using Flask-Babel.

``` python
# Content of 3-app.py
# Flask app with template parametrization
# Implementation continues from Task 2
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run()
```

### 📝 4. Force locale with URL parameter
---------------------
**📜 Task requirements:** Implement a way to force a particular locale via URL parameters.

**🗂️ Files:** 
- **[4-app.py](4-app.py)**
- **[templates/4-index.html](templates/4-index.html)**

**🗒️ Description:** This task adds functionality to force a specific locale by passing a `locale` parameter in the URL.

``` python
# Content of 4-app.py
# Implementation continues from Task 3
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run()
```

### 📝 5. Mock logging in
---------------------
**📜 Task requirements:** Emulate user login behavior and display personalized messages based on the logged-in user.

**🗂️ Files:** 
- **[5-app.py](5-app.py)**
- **[templates/5-index.html](templates/5-index.html)**

**🗒️ Description:** This task involves creating a mock user login system and displaying personalized messages based on the logged-in user.

``` python
# Content of 5-app.py
# Implementation continues from Task 4
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    user_id = request.args.get('login_as')
    return users.get(int(user_id)) if user_id and int(user_id) in users else None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    if g.user and g.user['locale']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('5-index.html', user=g.user)

if __name__ == '__main__':
    app.run()
```

### 📝 6. Use user locale
---------------------
**📜 Task requirements:** Change the locale detection to use the user's preferred locale if available.

**🗂️ Files:** 
- **[6-app.py](6-app.py)**
- **[templates/6-index.html](templates/6-index.html)**

**🗒️ Description:** This task modifies the locale detection mechanism to prioritize the user's preferred locale.

``` python
# Content of 6-app.py
# Implementation continues from Task 5
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

def get_user():
    user_id = request.args.get('login_as')
    return users.get(int(user_id)) if user_id and int(user_id) in users else None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    if g.user and g.user['locale']:
        return g.user['locale']
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('6-index.html', user=g.user)

if __name__ == '__main__':
    app.run()
```

### 📝 7. Infer appropriate time zone
---------------------
**📜 Task requirements:** Define a function to infer the appropriate time zone based on user preferences.

**🗂️ Files:** 
- **[7-app.py](7-app.py)**
- **[templates/7-index.html](templates/7-index.html)**

**🗒️ Description:** This task involves implementing logic to determine the appropriate time zone for the user.

``` python
# Content of 7-app.py
# Implementation continues from Task 6
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)

def get_timezone():
    user_timezone = g.user['timezone'] if g.user and g.user['timezone'] else None
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return 'UTC'

@babel.timezoneselector
def get_timezone():
    return get_timezone()

@app.route('/')
def index():
    return render_template('7-index.html', user=g.user)

if __name__ == '__main__':
    app.run()
```

### 📝 8. Display the current time (Advanced)
---------------------
**📜 Task requirements:** Display the current time in the appropriate format based on the inferred time zone and language.

**🗂️ Files:** 
- **[app.py](app.py)**
- **[translations/en/LC_MESSAGES/messages.po](translations/en/LC_MESSAGES/messages.po)**
- **[translations/fr/LC_MESSAGES/messages.po](translations/fr/LC_MESSAGES/messages.po)**
- **[templates/index.html](templates/index.html)**

**🗒️ Description:** This advanced task involves displaying the current time in the appropriate format based on the user's language and time zone preferences.

``` python
# Content of app.py
# Implementation continues from Task 7
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

def get_timezone():
    user_timezone = g.user['timezone'] if g.user and g.user['timezone'] else None
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return 'UTC'

@babel.timezoneselector
def get_timezone():
    return get_timezone()

@app.route('/')
def index():
    current_time = datetime.now(pytz.timezone(get_timezone())).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', user=g.user, current_time=current_time)

if __name__ == '__main__':
    app.run()
```

## 🎓 Key Takeaways

- Developed a Flask application with internationalization (i18n) support using Flask-Babel.

- Implemented language localization to serve content in multiple languages based on user preferences.
- Handled user authentication by emulating a user login system and displaying personalized messages.
- Determined the appropriate time zone for users and displayed the current time accordingly.

## 📫 Contact Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BinyamMamo)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:binyammamo01@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/binyammamo)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](#)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://binyammamo.github.io)

<pre id="banner" style="color: #449999" align="center">


 █████╗ ██╗     ██╗  ██╗    ███████╗██╗    ██╗███████╗
██╔══██╗██║     ╚██╗██╔╝    ██╔════╝██║    ██║██╔════╝
███████║██║      ╚███╔╝     ███████╗██║ █╗ ██║█████╗  
██╔══██║██║      ██╔██╗     ╚════██║██║███╗██║██╔══╝  
██║  ██║███████╗██╔╝ ██╗    ███████║╚███╔███╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚══╝╚══╝ ╚══════╝
                                                      
</pre>