import datetime

import pymongo
from bson.objectid import ObjectId

# mongod --dbpath データの格納先
client = pymongo.MongoClient("mongodb://localhost:27017/")

collection = client["myNewDB"]
docs = collection.stacks

doc_1 = {
    "name": "Mike"
    , "age": 18
    , "hoby": ["soccer", "guiter"]
    , "family": {"father": "aaa", "mother": "bbb", "brother": None, "sister": ""}
    , "last_update": datetime.datetime.utcnow()
}

object_id = ObjectId("60c02e7d1ed47ad419a50a1e")

# 戻り値は　<class 'dict'>
doc = docs.find_one({"_id": object_id})
doc_id = None

if doc:
    doc_id = doc["_id"]
else:
    doc_id = docs.insert_one(doc_1).inserted_id

# 60c02e7d1ed47ad419a50a1e <class 'bson.objectid.ObjectId'>
print(doc_id, type(doc_id))

# {'_id': ObjectId('60c02e7d1ed47ad419a50a1e')
#     , 'name': 'Mike'
#     , 'age': 18
#     , 'hoby': ['soccer', 'guiter']
#     , 'family': {'father': 'aaa'
#                 , 'mother': 'bbb'
#                 , 'brother': None
#                 , 'sister': ''}
#     , 'last_update': datetime.datetime(2021, 6, 9, 2, 59, 9, 996000)
#  }
print(docs.find_one({"_id": doc_id}))
