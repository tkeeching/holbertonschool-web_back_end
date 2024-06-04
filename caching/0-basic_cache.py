#!/usr/bin env python3

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        - Must assign to the dictionary 'self.cache_data' the 'item'
          value for the key 'key'.
        - If 'key' or 'item' is 'None', this method should not do anything.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

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
# my_cache = BasicCache()
# my_cache.print_cache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# print(my_cache.get("D"))
# my_cache.print_cache()
# my_cache.put("D", "School")
# my_cache.put("E", "Battery")
# my_cache.put("A", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
