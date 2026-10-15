import json

nested_json_data = '''
{
  "cars": [
    {
      "make": "Toyota",
      "model": "Camry",
      "year": 2020,
      "features": {
        "safety": ["ABS", "Airbags"],
        "entertainment": ["Bluetooth", "Navigation"]
      }
    },
    {
      "make": "Honda",
      "model": "Civic",
      "year": 2019,
      "features": {
        "safety": ["ABS", "Lane Assist"],
        "entertainment": ["Bluetooth"]
      }
    }
  ]
}
'''

data = json.loads(nested_json_data)

for car in data['cars']:
    if 'Bluetooth' in car['features']['entertainment']:
        print(f"{car['make']} {car['model']} has Bluetooth")
