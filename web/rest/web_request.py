import json

import requests

# requests:urllibより直感的なモジュール(こっちがお薦め）

param = {"para1": "hoge", "para2": "fuga"}

# getメソッド確認
request_get = requests.get("https://httpbin.org/get", params=param, timeout=10)

print(request_get.status_code)
response_get = request_get.json()
print(json.dumps(response_get, indent=4))

# putメソッド確認
request_put = requests.post("https://httpbin.org/post", data=param)

print(request_put.status_code)
response_put = request_put.json()
print(json.dumps(response_put, indent=4))
