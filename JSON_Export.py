import json

with open("json_sample.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)
print(json_dict)
json_dict['interface']['enabled'] = 'false'

with open("json_sample_update.json", "w") as fh:
    json.dump(json_dict, fh, indent=4)
