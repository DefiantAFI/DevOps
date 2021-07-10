import xmltodict

with open("xml_sample.xml") as data:
    xml_example = data.read()
print(xml_example)

xml_dict = xmltodict.parse(xml_example)

xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"

print(xmltodict.unparse(xml_dict, pretty=True))

print(type(xml_dict))

with open("xml_sample_update.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))
