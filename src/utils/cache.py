"""
In-memory cache with TTL for API responses.

This module provides a simple cache system that stores API responses in memory
with a time-to-live (TTL) value. This can help reduce the number of requests
made to the API and improve performance.

Usage:
    from src.utils.cache import cache

    @cache(ttl=60)  # cache for 1 minute
    def get_api_response(url):
        # make API request and return response
        pass
"""

import time
from functools import wraps

class Cache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value, ttl):
        expiry = time.time() + ttl
        self.cache[key] = (value, expiry)

cache_instance = Cache()

def cache(ttl):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            cached_value = cache_instance.get(key)
            if cached_value is not None:
                return cached_value
            else:
                value = func(*args, **kwargs)
                cache_instance.set(key, value, ttl)
                return value
        return wrapper
    return decorator

# Example usage:
# @cache(ttl=60)  # cache for 1 minute
# def get_api_response(url):
#     # make API request and return response
#     pass

# Test the cache
def test_cache():
    @cache(ttl=10)  # cache for 10 seconds
    def add(a, b):
        time.sleep(2)  # simulate API request
        return a + b

    print(add(2, 3))  # should take 2 seconds
    print(add(2, 3))  # should return immediately from cache
    time.sleep(11)  # wait for cache to expire
    print(add(2, 3))  # should take 2 seconds again

if __name__ == "__main__":
    test_cache()