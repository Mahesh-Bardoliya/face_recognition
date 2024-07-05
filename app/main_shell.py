#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .factory import create_app

app = create_app(create_app=False, create_cli=True)
