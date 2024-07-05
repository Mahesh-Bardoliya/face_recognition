#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from flask.cli import AppGroup

from .. import models
from ..database import init_database
from ..extensions import db

app_cli = AppGroup("app", help="Perform application-specific actions.")


def make_shell_context():
    """Prepare shell context."""
    context = {
        # the current app is automatically added to context as app
        "db": db,
        "models": models,
    }
    print()
    print(
        "Available functions and variables:\n\n%s"
        % "\n".join(["app"] + list(context.keys()))
    )
    print()
    return context


@app_cli.command("init-db")
def init_db():
    """Initialize database."""
    init_database()


@app_cli.command("drop-db")
def drop_db():
    """Drop all database tables."""
    if click.confirm("Are you sure you want to completely delete database?"):
        db.drop_all()
        db.session.commit()