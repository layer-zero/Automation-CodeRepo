import json

with open("arista_interfaces.json") as f:
    data = json.load(f)

mgmt1 = data["interfaces"]["Management1"]
ip = mgmt1["interfaceAddress"]["ipAddr"]["address"]
status = mgmt1["interfaceStatus"]
protocol = mgmt1["lineProtocolStatus"]
mtu = mgmt1["mtu"]

print(f"Interface: Management1")
print(f"IP Address: {ip}")
print(f"Status: {status}, Protocol: {protocol}")
print(f"MTU: {mtu}")
