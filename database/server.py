from pymongo import MongoClient
import os
import utils

client = MongoClient('localhost', 27017)
# db = client['tg_bdag']
db = client['prod_tg_bdag']

def db_insert(_collection, _keys=[], _values=[]):
    collection = db[_collection]
    obj = {}
    if len(_keys) == len(_values):
        for idx, val in enumerate(_values):
            obj[_keys[idx]] = val

        collection.insert_one(obj).inserted_id
        print(obj) 
    else:
        print('Numeros de chaves diferentes a de valores!')

def db_select(_collection, _keys=[], _values=[]):
    collection = db[_collection]
    obj = {}
    if len(_keys) == len(_values):
        for idx, val in enumerate(_values):
            obj[_keys[idx]] = val
    results = collection.find_one(obj)
    return results

# def start_scripts():
#     for script_name in utils.scripts_names:
#         os.system('python {}'.format(script_name))

# start_scripts()