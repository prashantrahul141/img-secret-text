import json

list_ = [chr(i) for i in range(32, 127)]
dict_ = json.dumps({"list" : list_})

with open("secret_text.json", "w") as f:
    f.write(dict_)

