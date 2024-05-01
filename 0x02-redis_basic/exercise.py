#!/usr/nin/env python3
""" Cache class """
from typing import Union
from uuid import uuid4

from redis import Redis


class Cache:
    def __init__(self):
        """Constructor"""
        self._redis = Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
