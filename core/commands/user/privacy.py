#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, MessageHandler

from core.decorators import delete_command, on_update, set_handler_update
from core.utilities import filters
from core.utilities.message import message
from core.utilities.telegram_update import TelegramUpdate
from languages import get_lang


@on_update(filters=filters.command(["privacy"]) & filters.group & ~filters.reply)
@set_handler_update(MessageHandler)
@delete_command
async def source(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_lang(update)

    await message(
        update,
        context,
        "Privacy Info",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Privacy",
                        url="https://chatcontrolcenter.it/privacy",
                    )
                ]
            ]
        ),
    )
