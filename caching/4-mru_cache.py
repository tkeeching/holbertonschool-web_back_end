#!/usr/bin env python3
"""
MRUCache module that inherits from BaseCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache module
    """
    def __init__(self):
        super().__init__()
        self.mru_queue = []  # To keep track of the order of key usage

    def put(self, key, item):
        """
        - Must assign to the dictionary 'self.cache_data' the 'item'
          value for the key 'key'.
        - If 'key' or 'item' is 'None', this method should not do anything.
        - If the number of items in 'self.cache_data' is higher that
          'BaseCaching.MAX_ITEMS':
            - you must discard the most recently used item (MRU algorithm)
            - you must print 'DISCARD:' with the 'key' discarded and
              following by a new line
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.mru_queue:
                mru_key = self.mru_queue.pop()  # Get the mru key
                del self.cache_data[mru_key]  # Remove it from cache
                print("DISCARD:", mru_key)  # Print discarded key

        self.cache_data[key] = item
        self.mru_queue.append(key)

    def get(self, key):
        """
        - Must return the value in 'self.cache_data' linked to 'key'.
        - If 'key' is 'None' or if the 'key' doesn’t exist in
          'self.cache_data', return 'None'.
        """
        if key is None:
            return None

        # Check if key exists in cache
        if key in self.cache_data:
            # Move the key to the end of the MRU queue
            self.mru_queue.remove(key)
            self.mru_queue.append(key)
            return self.cache_data[key]
        else:
            return None


# Tests
# my_cache = MRUCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# print(my_cache.get("B"))
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
# my_cache.put("H", "H")
# my_cache.print_cache()
# my_cache.put("I", "I")
# my_cache.print_cache()
# my_cache.put("J", "J")
# my_cache.print_cache()
# my_cache.put("K", "K")
# my_cache.print_cache()
