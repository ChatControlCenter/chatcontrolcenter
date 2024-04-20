#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from quart import Blueprint, render_template, request
from core.database.models import Groups
from core.database.models import GroupsFilters

filters = Blueprint("filters", __name__, url_prefix="/filters")


@filters.get("/")
async def index():
    # Get Data by URL
    token = request.args.get('token')
    chat_id = request.args.get('chat_id')
    user_id = request.args.get('user_id')

    # Database Variables
    data_filters = await GroupsFilters.get(chat_id=chat_id)
    group = await Groups.get(id_group=chat_id)

    # Group info Transform into Dict
    data_group = {
        'id': group.id_group,
        'name': group.group_name,
        'total_users': group.total_users,
        'group_photo': group.group_photo,
        'language': group.languages,
        'max_warn': group.max_warn
    }

    # Grop Filters Transform into Dict
    filters_dict = {
        "exe": data_filters.exe_filter,
        "gif": data_filters.gif_filter,
        "jpg": data_filters.jpg_filter,
        "docx": data_filters.docx_filter,
        "apk": data_filters.apk_filter,
        "compress": data_filters.compress_filter
    }

    # Test Print
    print("Token:", token)
    print("Chat ID:", chat_id)
    print("User ID:", user_id)

    return await render_template("filters.html", group_data=data_group, group_filters=filters_dict)
