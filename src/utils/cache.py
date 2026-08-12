import time
from typing import Any, Dict, Optional

class Cache:
    def __init__(self, ttl: int = 60):  # 1 minute default TTL
        """
        Initialize the cache with a given TTL (time to live) in seconds.
        
        :param ttl: Time to live in seconds
        """
        self.ttl = ttl
        self.cache: Dict[str, Dict[str, Any]] = {}

    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from the cache by key.
        
        :param key: Cache key
        :return: Cached value or None if not found or expired
        """
        if key in self.cache:
            value = self.cache[key]
            if time.time() < value['expires']:
                return value['data']
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any) -> None:
        """
        Set a value in the cache by key.
        
        :param key: Cache key
        :param value: Value to cache
        """
        expires = time.time() + self.ttl
        self.cache[key] = {'data': value, 'expires': expires}

    def delete(self, key: str) -> None:
        """
        Delete a value from the cache by key.
        
        :param key: Cache key
        """
        if key in self.cache:
            del self.cache[key]

# Create a singleton cache instance
cache = Cache(ttl=300)  # 5 minutes TTL

def get_cached_api_response(key: str) -> Optional[Any]:
    """
    Get a cached API response by key.
    
    :param key: Cache key
    :return: Cached API response or None if not found or expired
    """
    return cache.get(key)

def cache_api_response(key: str, value: Any) -> None:
    """
    Cache an API response by key.
    
    :param key: Cache key
    :param value: API response to cache
    """
    cache.set(key, value)

def delete_cached_api_response(key: str) -> None:
    """
    Delete a cached API response by key.
    
    :param key: Cache key
    """
    cache.delete(key)