import time
from typing import Any, Dict

class Cache:
    def __init__(self, ttl: int = 60):
        """
        Initialize the cache with a time-to-live (TTL) value.

        Args:
        ttl (int): The time-to-live value in seconds. Defaults to 60.
        """
        self.cache: Dict[str, Any] = {}
        self.ttl = ttl

    def get(self, key: str) -> Any:
        """
        Get a value from the cache.

        Args:
        key (str): The key to retrieve from the cache.

        Returns:
        Any: The cached value or None if not found or expired.
        """
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
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
        expiry = time.time() + self.ttl
        self.cache[key] = (value, expiry)

    def delete(self, key: str) -> None:
        """
        Delete a key from the cache.

        Args:
        key (str): The key to delete from the cache.
        """
        if key in self.cache:
            del self.cache[key]

# Create a cache instance with a TTL of 30 seconds
cache = Cache(ttl=30)

def cache_response(ttl: int = 30):
    """
    Decorator to cache API responses.

    Args:
    ttl (int): The time-to-live value in seconds. Defaults to 30.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            cached_response = cache.get(key)
            if cached_response is not None:
                return cached_response
            response = func(*args, **kwargs)
            cache.set(key, response)
            return response
        return wrapper
    return decorator

# Example usage:
# @cache_response(ttl=60)
# def get_habits(user_id: int) -> List[Habit]:
#     # API call to retrieve habits for the user
#     habits = Habit.objects.filter(user_id=user_id)
#     return habits