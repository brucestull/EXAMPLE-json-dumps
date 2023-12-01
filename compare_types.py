import json


car_dict = {"brand": "Nonya", "model": "Sedan", "year": 2019}

# Convert Python dictionary to JSON string
car_json_string = json.dumps(car_dict)
print("car_json_string:", type(car_json_string), car_json_string)
print("car_dict:", type(car_dict), car_dict)
