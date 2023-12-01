import json
import pprint

from models import Car

print("Examining Car...")
junk_car_object = Car("Nonya", "Sedan", 2019)
# `json.dumps()` converts a Python object to a JSON string
junk_car_json_string = json.dumps(junk_car_object.__dict__)
print("junk_car_object:", type(junk_car_object), junk_car_object)
print("junk_car_json_string:", type(junk_car_json_string), junk_car_json_string)

# `json.loads()` converts a JSON string to a Python object
parsed_junk_car_string = json.loads(junk_car_json_string)
print(
    "parsed_junk_car_string:",
    type(parsed_junk_car_string),
)
pprint.pprint(parsed_junk_car_string),
