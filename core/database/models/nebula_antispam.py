#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

from tortoise import fields
from tortoise.models import Model


class NebulaAntispam(Model):
    id = fields.IntField(pk=True)
    logic = fields.CharField(255, unique=True)

    class Meta:
        table = "nebula_antispam"
