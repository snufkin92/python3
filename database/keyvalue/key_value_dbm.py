import dbm

with dbm.open('dbm.db', 'c') as kv:
    # 数値は格納できない点に注意
    kv["key1"] = "value1"
    kv["key2"] = "value1"

    # 重複キーは後勝ち
    kv["key1"] = "value3"

    # 辞書型で数値を格納してやれば問題なし
    kv["key3"] = '{"aaa":1, "bbb":"good!"}'

import json

with dbm.open('dbm.db', 'r') as kv:
    print(kv["key1"].decode("utf-8"))
    print(kv["key3"].decode("utf-8"))

    aaa = json.loads(kv["key3"].decode("utf-8"))
    print(type(aaa))
    print(aaa)


# 全てのキーを取得
with dbm.open('cache.db', 'r') as kv:
    k = kv.firstkey()
    while k != None:
        print(k)
        k = kv.nextkey(k)