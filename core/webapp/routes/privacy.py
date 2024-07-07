#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from quart import Blueprint, render_template

privacy = Blueprint("privacy", __name__)


@privacy.route("/privacy", methods=["GET"])
async def privacy_info():
    return await render_template("privacy.html")
