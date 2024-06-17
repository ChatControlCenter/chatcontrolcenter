#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from telegram.ext import CallbackQueryHandler, ContextTypes

from core.decorators import on_update, set_handler_update
from core.utilities.telegram_update import TelegramUpdate


@on_update()
@set_handler_update(CallbackQueryHandler, r"^close$")
async def init(update: TelegramUpdate, _: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.delete()
