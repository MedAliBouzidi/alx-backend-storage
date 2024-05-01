#!/usr/nin/env python3
""" Cache class """
from typing import Union
from redis import Redis
from uuid import uuid4


class Cache:
    def __init__(self):
        """Constructor"""
        self._redis = Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
