#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from quart import Blueprint, render_template, request, jsonify, url_for, redirect
from core.database.models import Groups
from core.database.models import GroupsFilters
from core.utilities.token_jwt import decode_jwt
from core.utilities.functions import update_filters

filters = Blueprint("filters", __name__, url_prefix="/filters")

#TODO non funziona il message
@filters.route("/<token>/<chat>", methods=["GET", "POST"])
async def index(token,chat):
    # Decode and validate the token
    valid_token, token_payload = decode_jwt(token)
    if not valid_token:
        return "Invalid token or token expired"

    # Database Variables
    message = None
    data_filters = await GroupsFilters.get(chat_id=chat)
    group = await Groups.get(id_group=chat)

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
        "exe_filter": data_filters.exe_filter,
        "gif_filter": data_filters.gif_filter,
        "jpg_filter": data_filters.jpg_filter,
        "docx_filter": data_filters.docx_filter,
        "apk_filter": data_filters.apk_filter,
        "compress_filter": data_filters.compress_filter
    }
    if request.method == "POST":
        form = await request.form
        filters_selected = {k: bool(v) for k, v in form.items() if k.endswith("_filter")}

        #Check if True or False
        filters_selected = {
            "exe_filter": "exe_filter" in filters_selected,
            "gif_filter": "gif_filter" in filters_selected,
            "jpg_filter": "jpg_filter" in filters_selected,
            "docx_filter": "docx_filter" in filters_selected,
            "apk_filter": "apk_filter" in filters_selected,
            "compress_filter": "compress_filter" in filters_selected
        }

        # Aggiorna i filtri nel database
        await update_filters(chat, filters_selected)

        message = jsonify({"message":"Salvataggio dei Filtri effettuato con successo!"})
        return message
        #return redirect(url_for('filters.index',chat=chat,token=token))

    return await render_template("filters.html", group_data=data_group, group_filters=filters_dict,message=message)
