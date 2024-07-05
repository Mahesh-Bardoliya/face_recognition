#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()
env_variables = []

PROJECT_TITLE = "Flask Boilerplate" # TODO: Change project name.

# Disable or enable celery extension
CELERY_APP_EXTENSION = False  # TODO: If you have background jobs in the project then you can set it True.

# Flask-migrates
ALEMBIC_DIR = "migrations"

# Flask-smorest
API_TITLE = PROJECT_TITLE
API_VERSION = "v1"
OPENAPI_VERSION = "3.0.3"

# DB Credentials.
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

# DB URI
SQLALCHEMY_DATABASE_URI = "sqlite:///master.db"
# REDIS Credentials.
if CELERY_APP_EXTENSION:
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    REDIS_USERNAME = os.getenv("REDIS_USERNAME")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

    # REDIS URl
    REDIS_URL = f"redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"
