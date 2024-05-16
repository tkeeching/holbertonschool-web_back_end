#!/usr/bin/env python3

"""Lists all documents in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all document in mongo_collection"""

    documents = list(mongo_collection.find())

    return documents


# Tests
# if __name__ == "__main__":
#     client = MongoClient('mongodb://127.0.0.1:27017')
#     school_collection = client.local.school
#     schools = list_all(school_collection)
#     for school in schools:
#         print("[{}] {}".format(school.get('_id'), school.get('name')))