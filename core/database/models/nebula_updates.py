#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from tortoise import fields
from tortoise.models import Model


class NebulaUpdates(Model):
    id = fields.IntField(pk=True)
    update_id = fields.BigIntField(unique=True)
    message_id = fields.BigIntField()
    tg_group_id = fields.BigIntField()
    tg_user_id = fields.BigIntField()
    date = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "nebula_updates"
