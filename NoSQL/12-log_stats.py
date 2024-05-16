#!/usr/bin/env python3

"""Provides some stats about Nginc logs stored in MongodDB"""

from pymongo import MongoClient


def nginx_stats(mongo_collection):
    """Provides stats on Nginx logs stored in mongo_collection"""

    document_count = mongo_collection.count_documents({})
    method_get_count = len(list(mongo_collection.find({"method": "GET"})))
    method_post_count = len(list(mongo_collection.find({"method": "POST"})))
    method_put_count = len(list(mongo_collection.find({"method": "PUT"})))
    method_patch_count = len(list(mongo_collection.find({"method": "PATCH"})))
    method_delete_count = len(list(mongo_collection.find(
        {"method": "DELETE"})))
    status_path_count = len(list(mongo_collection.find({"path": "/status"})))

    print("{} logs".format(document_count))
    print("Methods:")
    print("{} method GET: {}".format("\t", method_get_count))
    print("{} method POST: {}".format("\t", method_post_count))
    print("{} method PUT: {}".format("\t", method_put_count))
    print("{} method PATCH: {}".format("\t", method_patch_count))
    print("{} method DELETE: {}".format("\t", method_delete_count))
    print("{} status check".format(status_path_count))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    nginx_stats(nginx_collection)

# Tests
# if __name__ == "__main__":
#     client = MongoClient('mongodb://127.0.0.1:27017')
#     nginx_collection = client.logs.nginx

#     nginx_stats(nginx_collection)
