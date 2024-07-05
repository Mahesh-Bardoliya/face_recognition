#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .extensions import db


def init_database():
    # Setting up database connection
    db.create_all()
    db.session.commit()
