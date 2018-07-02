# coding=utf-8
import pymongo


def set_mongo(arr_):
    print()
    mongo = pymongo.MongoClient('localhost:27017')
    http = mongo['http']
    api = http['api']
    api.insert_one(arr_)
