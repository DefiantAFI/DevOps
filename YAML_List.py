import yaml

with open("yaml_list.yaml") as data:
    yaml_sample = data.read()

yaml_list = yaml.load(yaml_sample, Loader=yaml.FullLoader)

print(yaml_list)