import json

f = open("Dummy.json", "r")
data = json.load(f)
print(data)
f.close()

f = open("hoge.json", "w")
data = {'KANTO': {'TOKYO': 50, 'URAWA': 999}, 'KANSAI': {'OOSAKA': 30, 'KYOTO': 20}}

json.dump(data, f, indent=4)
f.close()
