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
from core.utilities.functions import save_badword


@on_update(
    filters=filters.command(["badword"])
            & filters.check_role(Role.OWNER, Role.CREATOR, Role.ADMINISTRATOR)
)
@set_handler_update(MessageHandler)
@delete_command
async def init(update: TelegramUpdate, context: ContextTypes.DEFAULT_TYPE):
    lang = await get_lang(update)

    word = update.message.text.split(maxsplit=1)
    if len(word) <= 1:
        await message(update, context, lang["BADWORD_ERROR_EXIST"], allow_sending_without_reply=True)
        return

    badword = word[1]
    chat = update.effective_chat
    chat_id = chat.id

    result = await save_badword(chat_id, badword)

    # Rispondi all'utente in base al risultato
    if result == "La badword esiste già per questo gruppo.":
        await message(update, context, lang["BADWORD_DUPLICATE"], allow_sending_without_reply=True)
    elif result == "Badword salvata con successo.":
        await message(update, context, lang["BADWORD_SUCCESS"], allow_sending_without_reply=True)
    else:
        await message(update, context, lang["BADWORD_ERROR"], allow_sending_without_reply=True)
