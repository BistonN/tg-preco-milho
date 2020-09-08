from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
db = cliente['tg_bdag']

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
