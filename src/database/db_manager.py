import json

from pymongo import MongoClient
from bson.json_util import dumps, loads

import os


# Now you can perfom any CRUD operations on the DB
# testes
# colecao
class DBManager:
    client = None
    MONGODB_HOST = None
    MONGODB_PORT = None
    MONGODB_PWD = None
    MONGODB_USER = None

    @staticmethod
    def set_var_if_exists(var_name, default):
        if os.environ[var_name] is None:
            return default
        return os.environ[var_name]

    def __init__(self):
        self.MONGODB_HOST = self.set_var_if_exists("MONGODB_HOST", "localhost")
        self.MONGODB_PORT = self.set_var_if_exists("MONGODB_PORT", "27017")
        self.MONGODB_PWD = self.set_var_if_exists("MONGODB_PWD", "root")
        self.MONGODB_USER = self.set_var_if_exists("MONGODB_USER", "root")

        connection_url = "mongodb://" + self.MONGODB_USER + ":" + self.MONGODB_PWD + "@" + self.MONGODB_HOST + ":" + self.MONGODB_PORT
        print(connection_url)
        self.client = MongoClient(connection_url)

    def toJson(self, object):
        return object

    def list_all(self, db_name: str, collection: str):
        db = self.client[db_name]
        collection = db[collection]
        cursor = collection.find()
        list_cur = list(cursor)
        return self.toJson(json.loads(dumps(list_cur)))

    def insert(self, db_name: str, collection: str, data: dict):
        db = self.client[db_name]
        collection = db[collection]
        saved = collection.find_one(data)
        try:
            collection.insert_one(data)
            return self.toJson({'response': 'Saved', 'success': True, 'data': saved})
        except Exception as e:
            print(e)
            return self.toJson({'response': 'Can\'t save', 'success': False})

    def get_last_topic(self, topic: str):
        db = self.client['mqtt']
        collection = db['topics']
        filter = {'topic': topic}
        return json.loads(dumps(collection.find_one(filter)))

    def save_last_topic(self, topic: str, data: dict):
        db = self.client['mqtt']
        collection = db['topics']
        filter = {'topic': topic}
        cursor = collection.find_one(filter)
        if cursor is None:
            try:
                collection.insert_one(data)
                return self.toJson({'response': 'Saved', 'success': True, 'data': data})
            except Exception as e:
                print(e)
                return self.toJson({'response': 'Can\'t save', 'success': False})

        try:
            collection.update_one(filter, {"$set": data})
            return self.toJson({'response': 'Saved', 'success': True, 'data': data})
        except Exception as e:
            print(e)
            return self.toJson({'response': 'Can\'t save', 'success': False})
