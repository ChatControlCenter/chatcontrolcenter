#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from telegram.ext import ContextTypes

from core.decorators import delete_command, on_update
from core.utilities import filters
from core.utilities.enums import Role
from core.utilities.telegram_update import TelegramUpdate


@on_update(
    filters=filters.command(["del"])
    & filters.check_role(Role.OWNER, Role.CREATOR, Role.ADMINISTRATOR)
    & filters.reply
    & filters.group
)
@delete_command
async def init(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_to_message.delete()
