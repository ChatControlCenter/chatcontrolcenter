#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from telegram.ext import ContextTypes, MessageHandler

from core.decorators import delete_command, on_update, set_handler_update
from core.utilities import filters
from core.utilities.enums import Role
from core.utilities.message import message
from core.utilities.telegram_update import TelegramUpdate
from core.utilities.text import Text
from languages import get_lang


@on_update(
    filters=filters.command(["chatid"])
    & filters.check_role(Role.OWNER, Role.CREATOR, Role.ADMINISTRATOR)
    & filters.group
)
@set_handler_update(MessageHandler)
@delete_command
async def chat_id(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_lang(update)
    params = {"id": update.effective_chat.id}

    await message(update, context, lang["CHAT_ID_COMMAND"].format_map(Text(params)))
