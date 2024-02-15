#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from quart import Blueprint, render_template

filters = Blueprint("filters", __name__, url_prefix="/filters")


@filters.get("/")
async def index():
    return await render_template("filters/index.html")
