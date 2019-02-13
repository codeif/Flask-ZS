from flask_zs import CustomFlask, register_blueprints, register_error_handlers
from .core import commands, db


def create_app():
    app = CustomFlask(__name__)
    app.config.from_object('demo.config.Config')
    db.init_app(app)

    register_blueprints(app, 'demo.views')

    commands.init_app(app)
    register_error_handlers(app)

    return app
