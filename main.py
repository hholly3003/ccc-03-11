from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    #Registering the db and ma into the app using init_app function
    db.init_app(app)
    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    from marshmallow.exceptions import ValidationError
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    return app