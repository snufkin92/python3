import memcache

memcache_db = memcache.Client({"localhost:11211"})

memcache_db.set('key1', 'value1')

# value1
print(memcache_db.get('key1'))

# dbmと異なり、数値もOK
memcache_db.set('key2', 2)

# 2
print(memcache_db.get('key2'))

# 値を1増やしたい場合
memcache_db.incr('key2', 1)
print(memcache_db.get('key2'))

# 辞書型で取得
memcache_db.set("key3", '{"aaa":1, "bbb":"so good!"}')

import json

aaa = json.loads(memcache_db.get('key3'))

# <class 'dict'>
print(type(aaa))

# {'aaa': 1, 'bbb': 'so good!'}
print(aaa)

# キャッシュへの生存時間を制御
import time

memcache_db.set('key4', "alive", time=1)

### sleep before = alive
print("### sleep before =", memcache_db.get('key4'))
time.sleep(2)

### sleep after= None
# print("### sleep after=", memcache_db.get('key4'))
