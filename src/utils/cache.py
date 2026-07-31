"""
In-memory cache with TTL for API responses.

This module provides a simple cache system that stores API responses in memory
with a time-to-live (TTL) value. This can help reduce the number of requests
made to the API and improve performance.

Usage:
    from src.utils.cache import cache

    @cache(ttl=60)  # cache for 1 minute
    def fetch_data(url):
        # make API request and return data
        pass
"""

import time
from functools import wraps

class Cache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        """Get a value from the cache."""
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value, ttl):
        """Set a value in the cache with a TTL."""
        expiry = time.time() + ttl
        self.cache[key] = (value, expiry)

    def delete(self, key):
        """Delete a value from the cache."""
        if key in self.cache:
            del self.cache[key]

cache_instance = Cache()

def cache(ttl):
    """Cache decorator with TTL."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            value = cache_instance.get(key)
            if value is not None:
                return value
            else:
                value = func(*args, **kwargs)
                cache_instance.set(key, value, ttl)
                return value
        return wrapper
    return decorator

def clear_cache():
    """Clear the entire cache."""
    cache_instance.cache = {}

def delete_cache(key):
    """Delete a specific key from the cache."""
    cache_instance.delete(key)

# Example usage:
# @cache(ttl=60)  # cache for 1 minute
# def fetch_data(url):
#     # make API request and return data
#     pass