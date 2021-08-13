from flask import Flask, app

def create_app():

    # from <name_of_blueprint_folders> import <functions>
    from .routes import routes
    app = Flask(__name__)
    # app.register_blueprint
    app.register_blueprint(routes, url_prefix='/')

    return app