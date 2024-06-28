#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from quart import Blueprint, render_template

user_commands = Blueprint("user_commands", __name__)


@user_commands.route("/user_commands", methods=["GET"])
async def commands_user():
    return await render_template("user_commands.html")
