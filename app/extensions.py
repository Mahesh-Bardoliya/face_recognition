#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup extensions here"""

from flask_migrate import Migrate
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
api = Api()
migrate = Migrate()
ma = Marshmallow()
