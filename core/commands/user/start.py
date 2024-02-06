#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from core.decorators import delete_command, on_update
from core.utilities import filters
from core.utilities.menu import build_menu
from core.utilities.message import message
from core.utilities.telegram_update import TelegramUpdate
from core.utilities.text import Text
from languages import get_lang

START_BUTTONS = (
    (
        "Commands",
        "https://chatcontrolcenter.it/#",
    ),
    ("Api", "https://api.chatcontrolcenter.it"),
    ("News", "https://t.me/chatcontrolcenternews"),
    ("Logs", "https://t.me/chatcontrolcenter_logs"),
    ("👥 Add me to a Group", "https://t.me/chatcontrolcenter_bot?startgroup=start"),
)


@on_update(filters=filters.command(["start"]) & filters.private)
@delete_command
async def init(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    buttons = [InlineKeyboardButton(name, url=url) for name, url in START_BUTTONS]
    params = {"name": f"@{context.bot.username}"}

    await message(
        update,
        context,
        (await get_lang(update))["START_COMMAND"].format_map(Text(params)),
        reply_markup=InlineKeyboardMarkup(build_menu(buttons, 3)),
    )
