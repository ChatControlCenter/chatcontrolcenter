#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from telegram.ext import CallbackQueryHandler, ContextTypes

from core.decorators import check_settings, on_update, set_handler_update
from core.utilities import filters
from core.utilities.enums import Role
from core.utilities.telegram_update import TelegramUpdate


@on_update(filters=filters.check_role(Role.OWNER, Role.CREATOR, Role.ADMINISTRATOR))
@set_handler_update(CallbackQueryHandler, r"^settings\|night$")
@check_settings
async def settings_night(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Work in progress!")
