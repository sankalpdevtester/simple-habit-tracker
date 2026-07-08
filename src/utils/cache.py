import time
from typing import Any, Dict

class Cache:
    def __init__(self, ttl: int = 60):
        """
        Initialize the cache with a time-to-live (TTL) in seconds.

        Args:
        ttl (int): The time-to-live for each cache entry in seconds. Defaults to 60.
        """
        self.cache: Dict[str, Any] = {}
        self.ttl = ttl

    def get(self, key: str) -> Any:
        """
        Get a value from the cache.

        Args:
        key (str): The key to retrieve from the cache.

        Returns:
        Any: The cached value if it exists and is not expired, otherwise None.
        """
        if key in self.cache:
            value, expires = self.cache[key]
            if time.time() < expires:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any) -> None:
        """
        Set a value in the cache.

        Args:
        key (str): The key to store in the cache.
        value (Any): The value to store in the cache.
        """
        expires = time.time() + self.ttl
        self.cache[key] = (value, expires)

    def delete(self, key: str) -> None:
        """
        Delete a key from the cache.

        Args:
        key (str): The key to delete from the cache.
        """
        if key in self.cache:
            del self.cache[key]

# Create a cache instance with a TTL of 1 minute
cache = Cache(ttl=60)

def cache_api_response(key: str, func, *args, **kwargs):
    """
    Cache the response of a function call.

    Args:
    key (str): The cache key.
    func: The function to call.
    *args: The positional arguments to pass to the function.
    **kwargs: The keyword arguments to pass to the function.

    Returns:
    Any: The cached or computed response.
    """
    cached_response = cache.get(key)
    if cached_response is not None:
        return cached_response
    else:
        response = func(*args, **kwargs)
        cache.set(key, response)
        return response

# Example usage:
def example_api_call():
    # Simulate an API call
    time.sleep(1)
    return "API response"

# Cache the API response for 1 minute
key = "example_api_call"
response = cache_api_response(key, example_api_call)
print(response)

# Subsequent calls will return the cached response
response = cache_api_response(key, example_api_call)
print(response)