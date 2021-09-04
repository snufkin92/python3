import json
import urllib.request

# https://httpbin.org : 簡単な HTTP Requestの送信と Response の確認が行える公開サーバ

# getメソッドの確認
get_param = {"para1": "hoge", "para2": "fuga"}

url = "https://httpbin.org/get" + "?" + urllib.parse.urlencode(get_param)

with urllib.request.urlopen(url) as f:
    print(f.read().decode("utf-8"))

# postメソッドの確認
post_param = json.dumps({"para1": "hoge", "para2": "fuga"}).encode("utf-8")
req = urllib.request.Request("https://httpbin.org/post", data=post_param, method="POST")

with urllib.request.urlopen(req) as f:
    # json.loads で str を dict に変換https://httpbin.org/put
    res = json.loads(f.read().decode("utf-8"))
    print(json.dumps(res, indent=4))
