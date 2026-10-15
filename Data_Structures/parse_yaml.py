import yaml

with open("yaml_data.yaml") as f:
    data = yaml.safe_load(f)

for intf in data["interfaces"]:
    if intf["status"] == "up":
        print(f"{intf['name']} is UP")
