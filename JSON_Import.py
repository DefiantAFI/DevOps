import json

with open("json_sample.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)

# input('\n\nHello: ')
# print(json_dict['interface']['ipv4']['address'])
# List = json_dict['interface']['ipv4']['address']

print(json_dict)
