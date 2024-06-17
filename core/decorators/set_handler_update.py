#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

import typing

from telegram.ext import BaseHandler


def set_handler_update(handler: typing.Type[BaseHandler] | str, *args, **kwargs):
    def decorator(func: typing.Callable):
        func.handler = handler
        func.args = args
        func.kwargs = kwargs

        return func

    return decorator
