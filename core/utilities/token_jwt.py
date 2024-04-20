#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright ChatControlCenter Team

import datetime

import jwt

from config import Session


def encode_jwt() -> str:
    payload = dict(
        exp=datetime.datetime.now(tz=datetime.timezone.utc)
        + datetime.timedelta(seconds=Session.config.JWT_TOKEN_EXPIRES)
    )

    return jwt.encode(payload, Session.config.TOKEN_SECRET, algorithm="HS256")


def decode_jwt(token):
    try:
        payload = jwt.decode(token, Session.config.TOKEN_SECRET, algorithms=["HS256"])
        # Get the expiration timestamp from the payload
        expiration_time = datetime.datetime.fromtimestamp(payload['exp'], tz=datetime.timezone.utc)
        # Check if token is expired
        if datetime.datetime.now(datetime.timezone.utc) > expiration_time:
            return False, "Token expired"
        # If all goes well, return True and the token payload
        return True, payload
    except jwt.ExpiredSignatureError:
        return False, "Token expired"
    except jwt.InvalidTokenError:
        return False, "Invalid token"