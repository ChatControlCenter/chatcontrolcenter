#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from telegram.constants import ParseMode
from telegram.ext import CallbackQueryHandler, ContextTypes

from core.decorators import on_update, set_handler_update
from core.utilities.telegram_update import TelegramUpdate


@on_update()
@set_handler_update(CallbackQueryHandler, r"^report\|resolved$")
async def init(update: TelegramUpdate, _: ContextTypes.DEFAULT_TYPE):
    text = update.callback_query.message.text
    text += f"\n<b>Fixed by: @{update.effective_user.username}</b>"

    await update.callback_query.edit_message_text(text, parse_mode=ParseMode.HTML)
