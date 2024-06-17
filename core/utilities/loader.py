#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

import importlib
import pathlib

from telegram.ext import Application, CallbackQueryHandler, ChatMemberHandler, MessageHandler

UPDATE_MAPPING = {
    CallbackQueryHandler: lambda func, *args, **kwargs: CallbackQueryHandler(func, *args, **kwargs),
    ChatMemberHandler: lambda func, *args, **kwargs: ChatMemberHandler(func, *args, **kwargs),
    MessageHandler: lambda func, *args, **kwargs: MessageHandler(None, func, *args, **kwargs),
}


def load_plugins(application: Application, plugins_paths: list[str]):
    core_path = pathlib.Path("core")

    for plugins_dir in plugins_paths:
        full_plugins_dir = core_path / plugins_dir

        if full_plugins_dir.exists() and full_plugins_dir.is_dir():
            for path in sorted(full_plugins_dir.rglob("*.py")):
                module_path = '.'.join(path.parent.parts + (path.stem,))
                module = importlib.import_module(module_path)

                for k, v in vars(module).items():
                    if getattr(v, "handler", False):
                        if v.handler in UPDATE_MAPPING:
                            application.add_handler(UPDATE_MAPPING[v.handler](v, *v.args, **v.kwargs))
                        elif v.handler == "ErrorHandler":
                            application.add_error_handler(v)
