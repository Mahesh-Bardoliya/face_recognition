#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from .api.routers import base_blueprint
from .config import CELERY_APP_EXTENSION
from .extensions import api
from .extensions import db
from .extensions import migrate
from .extensions import ma
from .scripts.flask import app_cli
from .scripts.flask import make_shell_context


def create_app(create_app: bool = False, create_cli: bool = False) -> Flask:
    app = Flask(__name__)

    configure_app(app)

    configure_extensions(app, create_app)

    if create_cli:
        configure_flask_cli(app)

    register_blueprints(app, create_app)

    return app


def configure_app(app):
    """Configure flask application."""
    # load default settings
    app.config.from_object("app.config")

    if CELERY_APP_EXTENSION:
        # Configures Celery to use Redis for communication.
        app.config.from_mapping(
            CELERY=dict(
                broker_url=REDIS_URL,
                result_backend=REDIS_URL,
                task_ignore_result=True,
                broker_connection_retry_on_startup=True,
            ),
        )


def configure_extensions(app, create_app: bool):
    """Configure extensions."""
    # flask-sqlalchemy
    db.init_app(app)

    if CELERY_APP_EXTENSION:
        # Celery
        celery_init_app(app)

    # flask-marshmallow
    ma.init_app(app)

    # flask-smorest
    if create_app:
        api.init_app(app)


def register_blueprints(app, create_app):
    """
    Registers Flask blueprints for various API endpoints.

    Args:
        app (Flask): Flask app instance.
    """
    if create_app:
        api.register_blueprint(base_blueprint, url_prefix="/")


def configure_flask_cli(app):
    """Configure flask command line interface."""
    # flask shell context
    app.shell_context_processor(make_shell_context)

    # flask-migrate
    migrate.init_app(app=app, db=db, directory=app.config["ALEMBIC_DIR"])

    # Add app cli command.
    app.cli.add_command(app_cli)


if CELERY_APP_EXTENSION:
    from celery import Celery
    from celery import Task
    from .config import REDIS_URL

    def celery_init_app(app: Flask) -> Celery:
        """Create and configure a Celery app."""

        class FlaskTask(Task):
            def __call__(self, *args: object, **kwargs: object) -> object:
                with app.app_context():
                    return self.run(*args, **kwargs)

        celery_app = Celery(app.name, task_cls=FlaskTask)
        celery_app.config_from_object(app.config["CELERY"])
        celery_app.set_default()
        app.extensions["celery"] = celery_app
        return celery_app