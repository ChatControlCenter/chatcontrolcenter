#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

import sys
import logging

from dotenv import load_dotenv
from loguru import logger
from quart import Quart
from telegram import Update
from telegram.ext import Application
from telegram.ext._application import DEFAULT_GROUP
from tortoise import run_async

from config import Config, Session
from core.database import init_db
from core.database.models import OwnerList, WhitelistTable
from core.utilities.functions import get_owner_list
from core.utilities.scheduler import start_scheduler
from core.utilities.loader import load_plugins
from core.webapp import routes
from languages import load_languages

# if version < 3.10, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 10:
    logger.error(
        "You MUST have a python version of at least 3.10! Multiple features depend on this. Bot quitting."
    )
    quit(1)

PLUGINS_PATHS = ["callback_query", "commands", "handlers"]
FMT = (
    "<green>[{time}]</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:"
    "<cyan>{line}</cyan> - <level>{message}</level>"
)
HANDLER_OFFSET = 2


fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

fh = logging.FileHandler("db.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(fmt)

logger_db_client = logging.getLogger("tortoise.db_client")
logger_db_client.setLevel(logging.DEBUG)
logger_db_client.addHandler(fh)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(fh)


async def separate_handlers(app: Application):
    app.handlers = {
        (i + HANDLER_OFFSET): [x]
        for i, x in enumerate(
            sorted(
                app.handlers[DEFAULT_GROUP],
                key=lambda x: x.callback.priority,
                reverse=True,
            )
        )
    }


async def main() -> None:
    # Configure loguru
    logger.configure(
        handlers=[
            {"sink": sys.stdout, "format": FMT},
            {"sink": "file.log", "format": FMT},
        ]
    )

    logger.info("Application started")

    # Load .env file
    logger.info("Load .env file")
    load_dotenv()

    # Load the Config
    conf = Session.config = Config()

    # Load languages
    logger.info("Load languages")
    load_languages()

    # Load database
    logger.info("Start database (tortoise)")
    await init_db()

    # Add owner
    logger.info("Add owner in database if not exist")

    await OwnerList.get_or_create(
        tg_id=conf.OWNER_ID, tg_username=conf.OWNER_USERNAME.lower()
    )

    await WhitelistTable.get_or_create(
        tg_id=conf.OWNER_ID, tg_username=conf.OWNER_USERNAME.lower()
    )

    # Get owner ids
    Session.owner_ids = await get_owner_list()

    # Start the bot.
    # Create the Application and pass it your bots token.
    application = Application.builder().token(conf.BOT_TOKEN).build()
    Session.bot = application.bot

    load_plugins(application, PLUGINS_PATHS)

    await separate_handlers(application)

    # Webapp
    app = Quart(
        __name__,
        template_folder="core/webapp/templates",
        static_folder="core/webapp/static",
    )

    app.register_blueprint(routes.filters)
    app.register_blueprint(routes.home)
    app.register_blueprint(routes.user_commands)
    app.register_blueprint(routes.privacy)

    # Scheduler
    start_scheduler()

    async with application:
        await application.start()
        await application.updater.start_polling(allowed_updates=Update.ALL_TYPES)

        await app.run_task(debug=conf.DEBUG, port=conf.WEBAPP_PORT)

        await application.updater.stop()
        await application.stop()


if __name__ == "__main__":
    run_async(main())
