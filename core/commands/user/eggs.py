#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from telegram.ext import ContextTypes, MessageHandler

from core.decorators import delete_command, on_update, set_handler_update
from core.utilities import filters
from core.utilities.message import message
from core.utilities.telegram_update import TelegramUpdate
from languages import get_lang


@on_update(filters=filters.command(["lost"]) & filters.group)
@set_handler_update(MessageHandler)
@delete_command
async def lost_command(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    await message(update, context, "<code>4 8 15 16 23 42</code>")


@on_update(filters=filters.command(["fiko"], ".") & filters.group)
@set_handler_update(MessageHandler)
async def fiko_command(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_lang(update)
    animation = "https://i.imgur.com/LP23P90.gif"

    await message(update, context, lang["FIKO_EGGS"], type="animation", img=animation)


@on_update(filters=filters.command(["nanachi"], "") & filters.group)
@set_handler_update(MessageHandler)
async def nanachi_command(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    msg = "Naaaa~~ 🐾"
    animation = "https://i.imgur.com/P9HXqM8.mp4"

    await message(update, context, msg, type="animation", img=animation)
