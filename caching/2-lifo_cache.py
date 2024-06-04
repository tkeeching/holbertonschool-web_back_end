#!/usr/bin env python3
"""
LIFOCache module that inherits from BaseCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache module
    """
    def __init__(self):
        super().__init__()
        self.queue = []  # List to maintain insertion order

    def put(self, key, item):
        """
        - Must assign to the dictionary 'self.cache_data' the 'item'
          value for the key 'key'.
        - If 'key' or 'item' is 'None', this method should not do anything.
        - If the number of items in 'self.cache_data' is higher that
          'BaseCaching.MAX_ITEMS':
            - you must discard the last item put in cache (LIFO algorithm)
            - you must print 'DISCARD:' with the 'key' discarded and
              following by a new line
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.queue.pop()
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """
        - Must return the value in 'self.cache_data' linked to 'key'.
        - If 'key' is 'None' or if the 'key' doesn’t exist in
          'self.cache_data', return 'None'.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]


# Tests
# my_cache = LIFOCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
