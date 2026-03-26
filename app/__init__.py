from flask import Flask

def create_app():
    route = Flask(__name__)

    from .routes import home
    route.add_url_rule("/", view_func=home, methods=["GET", "POST"])
    
    return route