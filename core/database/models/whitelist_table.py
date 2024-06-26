#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from tortoise import fields
from tortoise.models import Model


class WhitelistTable(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    tg_username = fields.CharField(50, unique=True)

    class Meta:
        table = "whitelist_table"
