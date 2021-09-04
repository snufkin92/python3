import json

humans = {
    "humans":
        [
            {"name": "Mike", "age": 25, "sex": "M"},
            {"name": "Jane", "age": 22, "sex": "F"}
        ]
}

# json出力
with open("human.json", "w") as f:
    json.dump(humans, f, indent=4)

# jsonの解析
with open("human.json", "r") as f:
    json_dict = json.load(f)
    print(type(json_dict))
    print(json_dict)
    print(json_dict["humans"][0]["name"])
