#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from core.decorators import on_update
from core.utilities import filters
from core.utilities.menu import build_menu
from core.utilities.message import message
from core.utilities.telegram_update import TelegramUpdate
from core.utilities.text import Text
from languages import get_lang


@on_update(filters=filters.command(["help"]))
async def init(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    buttons = [
        InlineKeyboardButton(
            text="📖 Command List",
            url="https://chatcontrolcenter.it",
        ),
        InlineKeyboardButton(
            text="🆓 Source", url="https://github.com/ChatControlCenter/chatcontrolcenter"
        ),
        InlineKeyboardButton("🔔 Logs Channel", url="https://t.me/chatcontrolcenter_logs"),
        InlineKeyboardButton("📣 News Channel", url="https://t.me/chatcontrolcenternews"),
        #TODO Create Page Blacklist
        #InlineKeyboardButton(
            #text="🚷 BlackList", url="https://squirrel-network.online/knowhere"
        #),
        InlineKeyboardButton(
            text="📑 API Docs",
            url="https://api.chatcontrolcenter.it",
        ),
        InlineKeyboardButton("Close 🗑", callback_data="close"),
    ]
    params = {"name": f"@{bot.username}"}

    await message(
        update,
        context,
        (await get_lang(update))["HELP_COMMAND"].format_map(Text(params)),
        reply_markup=InlineKeyboardMarkup(build_menu(buttons, 2)),
    )
