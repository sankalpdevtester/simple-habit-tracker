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
        """Get cached value by key."""
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value, ttl):
        """Set cached value by key with TTL."""
        expiry = time.time() + ttl
        self.cache[key] = (value, expiry)

    def delete(self, key):
        """Delete cached value by key."""
        if key in self.cache:
            del self.cache[key]

cache_instance = Cache()

def cache(ttl):
    """Cache decorator with TTL."""
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
# def fetch_data(url):
#     # make API request and return data
#     pass

def clear_cache():
    """Clear entire cache."""
    cache_instance.cache.clear()

def get_cache_stats():
    """Get cache statistics."""
    return {
        "hits": sum(1 for key, (value, expiry) in cache_instance.cache.items() if time.time() < expiry),
        "misses": len(cache_instance.cache) - sum(1 for key, (value, expiry) in cache_instance.cache.items() if time.time() < expiry),
        "size": len(cache_instance.cache)
    }

# Example usage:
# print(get_cache_stats())