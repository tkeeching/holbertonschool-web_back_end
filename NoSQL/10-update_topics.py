#!/usr/bin/env python3

"""Changes all topics of a school document based on the name"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Updates topics of a school document based on the namme"""

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}})


# Tests
# list_all = __import__('8-all').list_all

# if __name__ == "__main__":
#     client = MongoClient('mongodb://127.0.0.1:27017')
#     school_collection = client.local.school
#     update_topics(
#         school_collection,
#         "Holberton",
#         ["Sys admin", "AI", "Algorithm"])

#     schools = list_all(school_collection)
#     for school in schools:
#         print("[{}] {} {}".format(
#             school.get('_id'),
#             school.get('name'),
#             school.get('topics', "")))

#     update_topics(school_collection, "Holberton", ["iOS"])

#     schools = list_all(school_collection)
#     for school in schools:
#         print("[{}] {} {}".format(
#             school.get('_id'),
#             school.get('name'),
#             school.get('topics', "")))
