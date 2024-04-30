#!/usr/bin/env python3
"""
    Provides some stats about Nginx logs stored in MongoDB
    Database: logs
    Collection: nginx
    Display:
        - first line: x logs, x number of documents in collection
        - second line: Methods:
            - method GET: x
            - method POST: x
            - method PUT: x
            - method PATCH: x
            - method DELETE: x
        - third line: with x number of status check
"""
from pymongo import MongoClient

method_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    print(f"{mongo_collection.count_documents({})} logs")

    print("Methods:")
    for method in method_list:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    log_stats(collection)
