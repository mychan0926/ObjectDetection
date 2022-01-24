import json
f=open('../data/labels/labels.json')
label = json.load(f)

print(label[0]["labels"])
print(label[0]["labels"][0])
