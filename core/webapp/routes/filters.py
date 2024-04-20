#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from quart import Blueprint, render_template, request, jsonify
from core.database.models import Groups
from core.database.models import GroupsFilters
from core.utilities.token_jwt import decode_jwt

filters = Blueprint("filters", __name__, url_prefix="/filters")

async def update_filters(chat_id, filters_selected):
    # Recupera il record dei filtri dal database
    filters_record = await GroupsFilters.get(chat_id=chat_id)

    # Itera attraverso i filtri selezionati e aggiorna i valori nel record dei filtri
    for key, value in filters_selected.items():
        setattr(filters_record, f"{key}_filter", value)

    # Salva le modifiche nel database
    await filters_record.save()

#TODO non funziona il salvataggio
@filters.route("/<token>/<chat>", methods=["GET", "POST"])
async def index(token,chat):
    if request.method == "POST":
        form = await request.form
        filters_selected = {key: bool(form.get(key)) for key in form.keys() if key.startswith("filters[")}

        # Aggiorna i filtri nel database
        await update_filters(chat, filters_selected)

        return filters_selected
        # Aggiorna i filtri nel database
        #await update_filters(chat, filters_selected)

    else:
        # Decode and validate the token
        valid_token, token_payload = decode_jwt(token)
        if not valid_token:
            return "Invalid token or token expired"

        # Database Variables
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
            "exe": data_filters.exe_filter,
            "gif": data_filters.gif_filter,
            "jpg": data_filters.jpg_filter,
            "docx": data_filters.docx_filter,
            "apk": data_filters.apk_filter,
            "compress": data_filters.compress_filter
        }

        # Test Print
        print("Token:", token)
        print("Chat ID:", chat)
        #print("User ID:", user_id)

        return await render_template("filters.html", group_data=data_group, group_filters=filters_dict)
