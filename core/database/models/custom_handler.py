#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from tortoise import fields
from tortoise.models import Model


class CustomHandler(Model):
    id = fields.IntField(pk=True)
    chat_id = fields.BigIntField(unique=True)
    question = fields.CharField(255, unique=True)
    answer = fields.CharField(255)

    class Meta:
        table = "custom_handler"
